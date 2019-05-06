import typing
from collections import defaultdict

import kuber_maker

TYPES = {
    'string': 'str',
    'array': 'list',
    'object': 'dict',
    'integer': 'int',
    'boolean': 'bool',
    'number': 'float',
    'Time': 'str',
    # IntOrStrings must be integer values because of OpenApi v2
    # validation limitations. See issue for details:
    # https://github.com/kubernetes-client/python/issues/322
    'IntOrString': 'int',
    'Quantity': 'str',
    None: None
}

TYPE_HINTS = {
    'IntOrString': 'typing.Union[str, int, None]',
    'Quantity': 'typing.Union[str, int, None]'
}

TYPE_CONSTRUCTORS = {
    'string': '\'\'',
    'array': '[]',
    'object': '{}',
    'integer': 'None',
    'boolean': 'None',
    'number': 'None',
    'Time': 'None',
    'IntOrString': 'None',
    'Quantity': 'None'
}

QUALIFIED_MAPPINGS = {
    'rbac': 'rbac.authorization.k8s.io',
    'apiregistration': 'apiregistration.k8s.io'
}

PATHS_TO_SKIP = (
    'io.k8s.kubernetes.',
    'io.k8s.apimachinery.pkg.api.resource.',
    'io.k8s.apimachinery.pkg.util.',
)


def parse_definitions(
        version: str,
        definitions: dict
) -> kuber_maker.AllEntities:
    """..."""
    entities = defaultdict(dict)
    for api_path, definition in definitions.items():
        if api_path.startswith(PATHS_TO_SKIP):
            continue
        entity = _create_entity(version, api_path, definition)
        entities[entity.package][entity.class_name] = entity
    return kuber_maker.AllEntities(
        version=version,
        packages={
            k: kuber_maker.EntityPackage(k, v)
            for k, v in entities.items()
        }
    )


def parse_property(
        version: str,
        name: str,
        definition: dict,
        entity_class_name: str
) -> kuber_maker.Property:
    """..."""
    definition = definition.copy()
    return kuber_maker.Property(
        name=name,
        data_type=_get_data_type(version, name, definition, entity_class_name),
        description=definition.get('description', ''),
        source=definition
    )


def _get_qualified_api_version(package: str) -> str:
    """..."""
    # Get the api version parts like (app, v1) from the package.
    api_version_parts = package.rsplit('.', 1)[-1].split('_')
    api_version_parts[0] = QUALIFIED_MAPPINGS.get(
        api_version_parts[0],
        api_version_parts[0]
    )

    return '/'.join(api_version_parts)


def _create_entity(
        version: str,
        api_path: str,
        definition: dict
) -> kuber_maker.Entity:
    """..."""
    class_name = api_path.rsplit('.', 1)[-1]
    package = kuber_maker.to_kuber_package(version, api_path)
    path = kuber_maker.to_kuber_path(version, api_path)

    properties: typing.Dict[str, kuber_maker.Property] = {
        name: parse_property(version, name, value, class_name)
        for name, value in definition.get('properties', {}).items()
        if not name.startswith('$')
    }
    imports = sorted(list(set([
        p.data_type.code_import
        for p in properties.values()
        if p.data_type.code_import
    ])))
    is_resource = (
        ('apiVersion' in properties)
        and ('kind' in properties)
        and ('metadata' in properties)
        and (properties['metadata'].data_type.api_type == 'ObjectMeta')
    )

    return kuber_maker.Entity(
        api_path=api_path,
        class_name=class_name,
        api_version=_get_qualified_api_version(package),
        package=package,
        code_path=f'{path}.py',
        description=definition.get('description', ''),
        properties=properties,
        data_type=TYPES[definition.get('type', 'object')],
        source=definition,
        imports=imports,
        is_resource=is_resource
    )


def _get_data_type(
        version: str,
        name: str,
        property_definition: dict,
        entity_class_name: str
) -> kuber_maker.DataType:
    """..."""
    setter_type_hint = None
    reference = property_definition.get('$ref')
    reference_type = (reference or '').rsplit('.', 1)[-1]
    api_type = property_definition.get('type') or reference_type

    basic_type = TYPES.get(api_type)
    python_type = basic_type or reference_type
    constructor = TYPE_CONSTRUCTORS.get(api_type) or f'{reference_type}()'

    if api_type == 'array':
        items = property_definition.get('items') or {}
        reference = items.get('$ref')
        basic_item_type = TYPES[items.get('type')]
        reference_item_type = (reference or '').rsplit('.', 1)[-1]
        item_type = basic_item_type or reference_item_type
        sub_type_hint = item_type if basic_item_type else f'\'{item_type}\''
        type_hint = f'typing.List[{sub_type_hint}]'
    else:
        item_type = None
        type_hint = TYPE_HINTS.get(
            api_type,
            basic_type or f'\'{reference_type}\''
        )

    code_import = (
        kuber_maker.import_from_reference(version, reference)
        if reference else
        None
    )
    if code_import:
        # When the type is a kuber definition, allow for a dict type as well
        # that can be deserialized into the strict object type instead.
        setter_type_hint = f'typing.Union[{type_hint}, dict]'

    if reference_type == entity_class_name:
        # There are places in the API where recursive relationships exist
        # as properties have the same type as the object in which they are
        # defined. To prevent that, we set the values of those properties to
        # None by default and they have to be added manually instead.
        type_hint = f'typing.Optional[\'{reference_type}\']'
        setter_type_hint = f'typing.Union[\'{reference_type}\', dict, None]'
        constructor = 'None'

    return kuber_maker.DataType(
        api_type=api_type,
        python_type=python_type,
        constructor=constructor,
        type_hint=type_hint,
        code_import=code_import,
        item_type=item_type,
        setter_type_hint=setter_type_hint
    )
