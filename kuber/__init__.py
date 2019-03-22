from kuber.helm_management import Chart
from kuber.helm_management import Maintainer
from kuber.management import ResourceBundle
from kuber.management import get_latest_version as _get_latest_version
from kuber import v1_13 as latest

#: kuber library version.
__version__ = '1.0.1'

#: The most recent kubernetes version available within the library, which
#: can be used to avoid hard-coded versions when creating resource bundles.
latest_kube_version = _get_latest_version()


def create_bundle(kubernetes_version: str = None) -> ResourceBundle:
    """
    Creates a `ResourceBundle` instance initialized to define resources from
    the given Kubernetes version.

    :param kubernetes_version:
        Kubernetes version in the form MAJOR.MINOR (no patch) that should be
        used by the bundle when creating and operating on Kubernetes Resource
        objects (e.g. `Deployment`, `Pod`, etc.). If not specified the most
        recent version will be used.
    :return:
        Initialized `ResourceBundle`.
    """
    return ResourceBundle(version=kubernetes_version)


def from_directory(
        directory: str,
        recursive: bool = False,
        kubernetes_version: str = None
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
    :return:
        Initialized `ResourceBundle` populated with all of the Kubernetes
        Resource objects loaded from the specified directory.
    """
    bundle = ResourceBundle(version=kubernetes_version)
    return bundle.add_directory(directory, recursive=recursive)


def from_file(
        path: str,
        kubernetes_version: str = None
) -> ResourceBundle:
    """
    Creates a `ResourceBundle` object and populates it with the Kubernetes
    Resource configuration specified by the `path` argument.

    :param path:
    :param kubernetes_version:
        Kubernetes version in the form MAJOR.MINOR (no patch) that should be
        used by the bundle when creating and operating on Kubernetes Resource
        objects (e.g. `Deployment`, `Pod`, etc.). If not specified the most
        recent version will be used.
    :return:
        Initialized `ResourceBundle` populated with the Kubernetes Resource
        specified by the configuration file of the given `path`.
    """
    bundle = ResourceBundle(version=kubernetes_version)
    return bundle.add_file(path)
