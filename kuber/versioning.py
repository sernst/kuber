import datetime
import importlib
import os
import typing

_root_directory = directory = os.path.realpath(os.path.dirname(__file__))


class KubernetesVersion(typing.NamedTuple):
    """Data structure with information about a kubernetes installation."""

    label: str
    version: str
    major: str
    minor: str
    patch: str
    pre_release: str
    build: str
    commit_sha: str
    created_at: datetime.datetime


def get_version_data(version_label: str) -> KubernetesVersion:
    """
    Returns the KubernetesVersion object specified in the root subpackage
    of the specified Kubernetes library version.
    """
    package = '.'.join(['kuber', f'{version_label}'])
    loaded_module = importlib.import_module(package)
    return getattr(loaded_module, 'KUBERNETES_VERSION')


def get_all_versions(stable: bool = False) -> typing.List[KubernetesVersion]:
    """Returns Kubernetes version """
    alternatives = ['latest']
    if not stable:
        alternatives.append('pre')

    return [
        get_version_data(f)
        for f in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, f))
        and (f.startswith('v') or f in alternatives)
    ]


def get_latest_version(stable: bool = False) -> KubernetesVersion:
    """
    Determines the latest available, stable Kubernetes version within the
    kuber library.
    """
    entries = get_all_versions(stable=stable)
    entries.sort(key=lambda x: 10000 * int(x.major) + int(x.minor))
    return entries[-1]
