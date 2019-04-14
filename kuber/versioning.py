import datetime
import importlib
import os
import typing

_root_directory = os.path.realpath(os.path.dirname(__file__))


class KubernetesVersion(typing.NamedTuple):
    """Data structure with information about a kubernetes installation."""

    #: kuber identifier for the version, e.g. 'v1.14' or 'latest'
    label: str

    #: Full semantic kubernetes version of this version.
    version: str

    #: Major portion of the full semantic kubernetes version.
    major: str

    #: Minor portion of the full semantic kubernetes version.
    minor: str

    #: Patch portion of the full semantic kubernetes version.
    patch: str

    #: Pre-release version portion of the full semantic kubernetes version.
    #: This value will be `None` for stable versions.
    pre_release: str

    #: Build version portion of the full semantic kubernetes version.
    build: str

    #: Commit SHA string for the commit associated with this version tag
    #: in the source kubernetes GitHub repo.
    commit_sha: str

    #: Time at which kuber last processed and generated this version.
    created_at: datetime.datetime

    def __repr__(self):
        name = self.__class__.__name__
        return f'<{name} {self.label} ({self.version})>'


def get_version_data(version_label: str) -> KubernetesVersion:
    """
    Returns the KubernetesVersion object specified in the root subpackage
    of the specified Kubernetes library version.
    """
    version = f'{version_label}'.replace('.', '_')
    needs_prefix = (
        version not in ['pre', 'latest']
        and not version.startswith('v')
    )
    if needs_prefix:
        version = f'v{version}'

    package = '.'.join(['kuber', version])
    loaded_module = importlib.import_module(package)
    return getattr(loaded_module, 'KUBERNETES_VERSION')


def get_all_versions(stable: bool = False) -> typing.List[KubernetesVersion]:
    """
    Returns a list of all Kubernetes version values available within
    this installation of the kuber library.

    :param stable:
        Whether or not to restrict returned versions to stable releases,
        i.e. not pre-releases like alpha and beta versions.
    """
    alternatives = ['latest', 'pre']
    versions: typing.List[KubernetesVersion] = list(set([
        get_version_data(name)
        for name in os.listdir(_root_directory)
        if os.path.isdir(os.path.join(_root_directory, name))
        and (name.startswith('v') or name in alternatives)
    ]))
    versions.sort(key=lambda v: '{}.{}.{}'.format(
        v.major.zfill(3),
        v.minor.zfill(3),
        v.patch.zfill(3)
    ))
    return [v for v in versions if not stable or not v.pre_release]


def get_latest_version(stable: bool = False) -> KubernetesVersion:
    """
    Determines the latest available, stable Kubernetes version within the
    kuber library.
    """
    entries = get_all_versions(stable=stable)
    entries.sort(key=lambda x: 10000 * int(x.major) + int(x.minor))
    return entries[-1]
