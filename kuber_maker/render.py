import keyword
import os
import re
import string
import typing

from jinja2 import Environment
from jinja2 import FileSystemLoader

import kuber_maker

LINE_REGEX = re.compile(r'\n{4,}(?!\s+)')
SINGLE_LINE_REGEX = re.compile(r'\n{3,}(?=\s+)')


TEMPLATE_PATH_ROOT = os.path.realpath(os.path.join(
    os.path.dirname(__file__),
    'templates'
))

ENVIRONMENT = Environment(
    loader=FileSystemLoader(TEMPLATE_PATH_ROOT)
)

_PYTHON_BUILTINS = [
    'abs', 'delattr', 'hash', 'memoryview', 'set',
    'all', 'dict', 'help', 'min', 'setattr',
    'any', 'dir', 'hex', 'next', 'slice',
    'ascii', 'divmod', 'id', 'object', 'sorted',
    'bin', 'enumerate', 'input', 'oct', 'staticmethod',
    'bool', 'eval', 'int', 'open', 'str',
    'breakpoint', 'exec', 'isinstance', 'ord', 'sum',
    'bytearray', 'filter', 'issubclass', 'pow', 'super',
    'bytes', 'float', 'iter', 'print', 'tuple',
    'callable', 'format', 'len', 'property', 'type',
    'chr', 'frozenset', 'list', 'range', 'vars',
    'classmethod', 'getattr', 'locals', 'repr', 'zip',
    'compile', 'globals', 'map', 'reversed', '__import__',
    'complex', 'hasattr', 'max', 'round'
]


def _to_snake_case(value: str) -> str:
    """..."""
    if not value:
        return value

    value = value.replace('-', '_')
    if keyword.iskeyword(value) or value in _PYTHON_BUILTINS:
        value = f'{value}_'

    output = []
    for index, character in enumerate(value):
        previous = value[index - 1] if index > 0 else ''
        if character.lower() == character:
            output.append(character)
        elif index == 0 or previous.lower() != previous:
            output.append(character.lower())
        else:
            output.append(f'_{character.lower()}')

    return ''.join(output)


def _printable(value: str) -> str:
    """..."""
    return ''.join(list(filter(lambda x: x in string.printable, value)))


ENVIRONMENT.filters['snake_case'] = _to_snake_case
ENVIRONMENT.filters['printable'] = _printable


def render(template_name: str, **kwargs) -> str:
    """..."""
    return ENVIRONMENT.get_template(template_name).render(**kwargs)


def _get_container_entity(
        all_entities: kuber_maker.AllEntities
) -> kuber_maker.Entity:
    """..."""
    version = all_entities.version.replace('.', '_')
    container_package = f'kuber.v{version}.core.v1'
    return all_entities.packages[container_package].entities['Container']


def _containers_location(
        entity: kuber_maker.Entity,
        all_entities: kuber_maker.AllEntities,
        max_depth: int = 10
) -> typing.List[str]:
    """..."""
    if max_depth < 1:
        return []

    if 'containers' in entity.properties:
        return ['containers']

    for key, value in entity.properties.items():
        data_type = value.data_type
        if not data_type.code_import or data_type.api_type == 'array':
            continue

        child_package = data_type.code_import.package
        child_target = data_type.code_import.target
        child = all_entities.packages[child_package].entities[child_target]
        result = _containers_location(child, all_entities, max_depth - 1)
        if result:
            return [key, *result]

    return []


def render_package(package: str, all_entities: kuber_maker.AllEntities) -> str:
    """..."""
    blocks = []
    entities = all_entities.packages[package].entities
    container_entity = _get_container_entity(all_entities)
    include_container = False
    has_resource = False
    for e in entities.values():
        containers_location = '.'.join(_containers_location(e, all_entities))
        include_container = include_container or bool(containers_location)
        has_resource = has_resource or e.is_resource
        kubernetes_api_class_name = ''.join(
            [p.capitalize() for p in e.api_version.split('/')]
            + ['Api']
        )
        property_ignores = ['apiVersion', 'kind']
        if e.is_resource:
            property_ignores += ['status']

        blocks.append(render(
            'object-class.jinja2',
            entity=e,
            containers=containers_location,
            container_entity=container_entity,
            kubernetes_api_class_name=kubernetes_api_class_name,
            property_ignores=property_ignores
        ))

    data_types = set([
        p.data_type.api_type
        for e in entities.values()
        for p in e.properties.values()
    ])

    extra_imports = []
    if include_container:
        extra_imports.append(container_entity)

    import_skips = ['Time']
    imports = list(set([
        imp
        for e in (list(entities.values()) + extra_imports)
        for imp in e.imports
        if imp.package != package and imp.target not in import_skips
    ]))

    if include_container and package != container_entity.package:
        imports.append(kuber_maker.Import(
            target=container_entity.class_name,
            package=container_entity.package,
            api_path=container_entity.api_path,
            reference=container_entity.api_path
        ))

    import_block = render(
        'module-imports.jinja2',
        imports=sorted(imports),
        data_types=data_types,
        has_resource=has_resource
    )
    blocks.insert(0, import_block)
    lines = '\n'.join(blocks).split('\n')
    lines = [l.rstrip() for l in lines]
    contents = '\n'.join(lines)
    contents = re.sub(LINE_REGEX, '\n\n\n', contents)
    contents = f'{contents.rstrip()}\n'
    return re.sub(SINGLE_LINE_REGEX, '\n\n', contents)
