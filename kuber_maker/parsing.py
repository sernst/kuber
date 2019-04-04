from collections import defaultdict
import os

import kuber_maker

TYPES = {
    'string': 'str',
    'array': 'list',
    'object': 'dict',
    'integer': 'int',
    'boolean': 'bool',
    'number': 'float',
    'Time': 'str',
    'IntOrString': 'str',
    None: None
}

TYPE_HINTS = {
    'IntOrString': 'typing.Union[str, int]'
}

TYPE_CONSTRUCTORS = {
    'string': '\'\'',
    'array': '[]',
    'object': '{}',
    'integer': 'None',
    'boolean': 'None',
    'number': 'None',
    'Time': 'None',
    'IntOrString': 'None'
}


def parse_definitions(
        version: str,
        definitions: dict
) -> kuber_maker.AllEntities:
    """..."""
    entities = defaultdict(dict)
    for api_path, definition in definitions.items():
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
        definition: dict
) -> kuber_maker.Property:
    """..."""
    definition = definition.copy()
    return kuber_maker.Property(
        name=name,
        data_type=_get_data_type(version, definition),
        description=definition.get('description', ''),
        source=definition
    )


def _get_qualified_api_version(package: str) -> str:
    """..."""
    # Get the api version parts like (app, v1) from the package.
    api_version_parts = package.rsplit('.', 1)[-1].split('_')

    if api_version_parts[0] == 'rbac':
        api_version_parts[0] = 'rbac.authorization.k8s.io'

    return '/'.join(api_version_parts)


def _create_entity(
        version: str,
        api_path: str,
        definition: dict
) -> kuber_maker.Entity:
    """..."""
    package = kuber_maker.to_kuber_package(version, api_path)
    path = kuber_maker.to_kuber_path(version, api_path)

    properties = {
        name: parse_property(version, name, value)
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
        and (api_path.startswith('io.k8s.api.'))
    )

    return kuber_maker.Entity(
        api_path=api_path,
        class_name=api_path.rsplit('.', 1)[-1],
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
        property_definition: dict
) -> kuber_maker.DataType:
    """..."""
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

    return kuber_maker.DataType(
        api_type=api_type,
        python_type=python_type,
        constructor=constructor,
        type_hint=type_hint,
        code_import=code_import,
        item_type=item_type
    )
