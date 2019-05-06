import json
import os
import typing
import semver


class ApiSpec(typing.NamedTuple):
    """Data structure for high-level API info."""

    # Title from the swagger info object spec.
    title: str
    # Version as specified by the GitHub release name.
    version: str
    # Version from the info object in the Swagger spec. This make not
    # always be accurate in pre-releases as it appears to linger on the
    # last stable version.
    info_version: str
    # Semantic version as specified by the GitHub release name.
    version_info: semver.VersionInfo
    # Paths specified in the swagger definition.
    api_paths: typing.Dict[str, dict]
    # Definitions specified in the swagger definition.
    definitions: typing.Dict[str, dict]
    # The sha commit identifier that contains the swagger definition
    # used to generate this spec
    commit_sha: str


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
    # A special case type-hint specifically for use when specifying a
    # setter function argument type.
    setter_type_hint: str = None


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
    return '.'.join(['kuber', f'{v}', *args])


def directory_of_package(package: str) -> str:
    """..."""
    return os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..',
        *package.split('.')
    ))


def to_kuber_package(version: str, kubernetes_api_path: str) -> str:
    """..."""
    return get_package(version, *_to_kuber_hierarchy(kubernetes_api_path))


def get_path(version, *args) -> str:
    """..."""
    v = version.replace('.', '_')
    return os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'kuber', f'{v}', *args
    ))


def to_kuber_path(version: str, kubernetes_api_path: str) -> str:
    """..."""
    return get_path(version, *_to_kuber_hierarchy(kubernetes_api_path))


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


def load_spec(version: str) -> ApiSpec:
    """..."""
    path = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'specs', f'{version}.json'
    ))
    with open(path, 'rb') as f:
        contents = f.read()
    raw = json.loads(contents)
    return ApiSpec(
        title=raw['info']['title'],
        info_version=raw['info']['version'],
        version=raw['kuber']['name'],
        version_info=semver.parse_version_info(raw['kuber']['version']),
        api_paths=raw['paths'],
        definitions=raw['definitions'],
        commit_sha=raw['kuber']['commit_sha']
    )


def _to_kuber_hierarchy(kubernetes_api_path: str) -> typing.List[str]:
    """..."""
    path = (
        kubernetes_api_path
        .replace('-', '_')
        .replace('io.k8s.api.', '')
        .replace('io.k8s.', '')
        .replace('kube_aggregator.pkg.apis.', '')
        .replace('apimachinery.pkg.apis.', '')
        .replace('apiextensions_apiserver.pkg.apis.', '')
        .replace('pkg.apis.', '')
        .replace('pkg.', '')
    )

    # Remove file extension and split into hierarchy list.
    parts = path.rsplit('.')[:-1]

    # Combine the api versions, `apps, v1` into `apps_v1`.
    combined = '_'.join(parts[-2:])

    return parts[:-2] + [combined]
