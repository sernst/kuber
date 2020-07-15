import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.14',
    version='v1.14.8',
    major='1',
    minor='14',
    patch='8',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 15),
    commit_sha='211047e9a1922595eaa3a1127ed365e9299a6c23'
)
