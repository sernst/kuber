import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='pre',
    version='v1.19.0-alpha.0',
    major='1',
    minor='19',
    patch='0',
    pre_release='alpha.0',
    build='',
    created_at=_datetime.datetime(2020, 3, 24),
    commit_sha='1e12d92a5179dbfeb455c79dbf9120c8536e5f9c'
)
