import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.16',
    version='v1.16.0-beta.2',
    major='1',
    minor='16',
    patch='0',
    pre_release='beta.2',
    build='',
    created_at=_datetime.datetime(2019, 9, 10),
    commit_sha='48ca054daba9e610f13c6d6bfcedf6c7de12b138'
)
