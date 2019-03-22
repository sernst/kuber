import json
import os
import typing


class Import(typing.NamedTuple):
    """..."""

    target: str
    package: str
    api_path: str
    reference: str


class DataType(typing.NamedTuple):
    """..."""

    api_type: str
    python_type: str
    constructor: str
    type_hint: str
    code_import: typing.Optional[Import] = None
    item_type: typing.Optional[str] = None


class Property(typing.NamedTuple):
    """..."""

    name: str
    data_type: DataType
    description: str
    source: dict


class Entity(typing.NamedTuple):
    """..."""

    api_path: str
    api_version: str
    package: str
    code_path: str
    class_name: str
    description: str
    properties: typing.Dict[str, Property]
    data_type: str
    source: dict
    imports: typing.List[Import]
    is_resource: bool = False


class EntityPackage(typing.NamedTuple):
    """..."""

    package: str
    entities: typing.Dict[str, Entity]


class AllEntities(typing.NamedTuple):
    """..."""

    version: str
    packages: typing.Dict[str, EntityPackage]


def get_package(version, *args) -> str:
    """..."""
    v = version.replace('.', '_')
    return '.'.join(['kuber', f'v{v}', *args])


def directory_of_package(package: str) -> str:
    """..."""
    return os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..',
        *package.split('.')
    ))


def to_kuber_package(version: str, kubernetes_api_path: str) -> str:
    """..."""
    path = (
        kubernetes_api_path
        .replace('-', '_')
        .replace('io.k8s.api.', '')
        .replace('io.k8s.', '')
    )
    return get_package(version, *path.rsplit('.')[:-1])


def get_path(version, *args) -> str:
    """..."""
    v = version.replace('.', '_')
    return os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'kuber', f'v{v}', *args
    ))


def to_kuber_path(version: str, kubernetes_api_path: str) -> str:
    """..."""
    path = (
        kubernetes_api_path
        .replace('-', '_')
        .replace('io.k8s.api.', '')
        .replace('io.k8s.', '')
    )
    return get_path(version, *path.rsplit('.')[:-1])


def import_from_reference(version: str, reference_path: str) -> Import:
    """..."""
    path = reference_path.replace('#/definitions/', '')
    package = to_kuber_package(version, path)
    return Import(
        target=reference_path.rsplit('.', 1)[-1],
        package=package,
        api_path=path,
        reference=reference_path
    )


def load_spec(version: str) -> dict:
    """..."""
    path = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'specs', f'v{version}.json'
    ))
    with open(path, 'rb') as f:
        contents = f.read()
    return json.loads(contents)
