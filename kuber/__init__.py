import typing

from kuber import versioning as _versioning
from kuber.kube_api import get_version_from_cluster  # noqa
from kuber.kube_api import load_access_config  # noqa
from kuber.management import ResourceBundle
from kuber.management import from_dict  # noqa
from kuber.management import from_json_file  # noqa
from kuber.management import from_yaml  # noqa
from kuber.management import from_yaml_file  # noqa
from kuber.management import from_yaml_file_multiple  # noqa
from kuber.management import from_yaml_multiple  # noqa
from kuber.management import new_resource  # noqa

#: kuber library version.
__version__ = '1.2.5'

#: The most recent kubernetes version available within the library, which
#: can be used to avoid hard-coded versions when creating resource bundles.
latest_kube_version: '_versioning.KubernetesVersion' = (
    _versioning.get_latest_version(stable=True)
)

VersionLabel = typing.Union['_versioning.KubernetesVersion', str]


def create_bundle(
        kubernetes_version: str = None,
        bundle_name: VersionLabel = None
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
