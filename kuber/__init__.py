import typing as _typing
import yaml as _yaml

from kuber import versioning as _versioning
from kuber.interface import CommandAction  # noqa
from kuber.definitions import Collection  # noqa
from kuber.definitions import Definition  # noqa
from kuber.definitions import Resource  # noqa
from kuber.kube_api import get_version_from_cluster  # noqa
from kuber.kube_api import load_access_config  # noqa
from kuber.management import ResourceBundle
from kuber.management.creation import from_dict  # noqa
from kuber.management.creation import from_json_file  # noqa
from kuber.management.creation import from_yaml  # noqa
from kuber.management.creation import from_yaml_file  # noqa
from kuber.management.creation import from_yaml_file_multiple  # noqa
from kuber.management.creation import from_yaml_multiple  # noqa
from kuber.management.creation import new_resource  # noqa
from kuber.versioning import KubernetesVersion  # noqa

#: kuber library version.
__version__ = '1.7.4'

#: The loader used when loading yaml via pyyaml. This can be overridden
#: in cases where a different Loader is preferred.
yaml_loader = _yaml.Loader

#: All currently supported versions that exist within this installation
#: of the kuber library.
available_versions: _typing.List[KubernetesVersion] = (
    _versioning.get_all_versions()
)

#: The most recent kubernetes version available within the library, which
#: can be used to avoid hard-coded versions when creating resource bundles.
latest_kube_version: KubernetesVersion = (
    _versioning.get_latest_version(stable=True)
)

#: Type that accepts either a `KubernetesVersion` object or a string
#: representation of that version, e.g. 'v1.14' or 'latest'.
VersionLabel = _typing.Union[KubernetesVersion, str]


def create_bundle(
        kubernetes_version: VersionLabel = None,
        bundle_name: str = None
) -> ResourceBundle:
    """
    Creates a `ResourceBundle` instance initialized to define resources from
    the given Kubernetes version.

    :param kubernetes_version:
        Kubernetes version in the form MAJOR.MINOR (no patch) that should be
        used by the bundle when creating and operating on Kubernetes Resource
        objects (e.g. `Deployment`, `Pod`, etc.). If not specified the most
        recent version will be used.
    :param bundle_name:
        A name to associated with the resource bundle. If not specified, a
        randomized name will be generated instead.
    :return:
        Initialized `ResourceBundle`.
    """
    return ResourceBundle(bundle_name, kubernetes_version)


def from_directory_files(
        directory: str,
        filenames: _typing.Iterable = None,
        kubernetes_version: VersionLabel = None,
        bundle_name: str = None
) -> ResourceBundle:
    """
    Creates a `ResourceBundle` object from all of the resource
    configuration files specified by the ``filenames`` argument from
    within the specified directory.

    :param directory:
        Path of the directory where the Kubernetes Resource configuration files
        to be loaded are stored.
    :param filenames:
        A list of filenames in the given directory and the order in
        which they should be added.
    :param kubernetes_version:
        Kubernetes version in the form MAJOR.MINOR (no patch) that should be
        used by the bundle when creating and operating on Kubernetes Resource
        objects (e.g. `Deployment`, `Pod`, etc.). If not specified the most
        recent version will be used.
    :param bundle_name:
        A name to associated with the resource bundle. If not specified, a
        randomized name will be generated instead.
    :return:
        Initialized `ResourceBundle` populated with all of the Kubernetes
        Resource objects loaded from the specified directory.
    """
    bundle = ResourceBundle(bundle_name, kubernetes_version)
    return bundle.add_directory_files(directory, filenames=filenames)


def from_directory(
        directory: str,
        recursive: bool = False,
        kubernetes_version: VersionLabel = None,
        bundle_name: str = None
) -> ResourceBundle:
    """
    Creates a `ResourceBundle` object from all of the yaml and json
    configuration files within the specified directory.

    :param directory:
        Path of the directory where the Kubernetes Resource configuration files
        to be loaded are stored.
    :param recursive:
        Whether or not to recursively load resources files from descendent
        folders within the specified directory.
    :param kubernetes_version:
        Kubernetes version in the form MAJOR.MINOR (no patch) that should be
        used by the bundle when creating and operating on Kubernetes Resource
        objects (e.g. `Deployment`, `Pod`, etc.). If not specified the most
        recent version will be used.
    :param bundle_name:
        A name to associated with the resource bundle. If not specified, a
        randomized name will be generated instead.
    :return:
        Initialized `ResourceBundle` populated with all of the Kubernetes
        Resource objects loaded from the specified directory.
    """
    bundle = ResourceBundle(bundle_name, kubernetes_version)
    return bundle.add_directory(directory, recursive=recursive)


def from_file(
        path: str,
        kubernetes_version: VersionLabel = None,
        bundle_name: str = None
) -> ResourceBundle:
    """
    Creates a `ResourceBundle` object and populates it with the Kubernetes
    Resource configuration specified by the `path` argument.

    :param path:
        Path to the resource configuration file that should be loaded as a
        resource into the newly created resource bundle.
    :param kubernetes_version:
        Kubernetes version in the form MAJOR.MINOR (no patch) that should be
        used by the bundle when creating and operating on Kubernetes Resource
        objects (e.g. `Deployment`, `Pod`, etc.). If not specified the most
        recent version will be used.
    :param bundle_name:
        A name to associated with the resource bundle. If not specified, a
        randomized name will be generated instead.
    :return:
        Initialized `ResourceBundle` populated with the Kubernetes Resource
        specified by the configuration file of the given `path`.
    """
    bundle = ResourceBundle(bundle_name, kubernetes_version)
    return bundle.add_file(path)


def cli(
        callback: _typing.Callable[['CommandAction'], _typing.Any],
        kubernetes_version: VersionLabel = None,
        bundle_name: str = None,
        arguments: _typing.List[str] = None
) -> 'management.ResourceBundle':
    """
    Creates an empty bundle configured with the optionally specified
    Kubernetes version and bundle name and immediately invokes the command
    line interface for the bundle, but invoking the specified callback before
    executing the command. The callback is the opportunity to configure the
    bundle.

    :param callback:
        Callback that will be executed prior to the command line action
        execution. Use this callback to configure the bundle using input
        from the command line (including custom command arguments) before
        the cli command action is invoked.
    :param kubernetes_version:
        Kubernetes version in the form MAJOR.MINOR (no patch) that should be
        used by the bundle when creating and operating on Kubernetes Resource
        objects (e.g. `Deployment`, `Pod`, etc.). If not specified the most
        recent version will be used.
    :param bundle_name:
        A name to associated with the resource bundle. If not specified, a
        randomized name will be generated instead.
    :param arguments:
        Optional command line arguments to parse and use in the callback
        and then in the cli action execution. If omitted the arguments
        will be parsed from the sys.argv values provided on the command line.
    """
    bundle = create_bundle(
        kubernetes_version=kubernetes_version,
        bundle_name=bundle_name
    )
    bundle.cli.invoke(
        callback=callback,
        arguments=arguments
    )
    return bundle
