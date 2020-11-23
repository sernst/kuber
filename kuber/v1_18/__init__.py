import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.18',
    version='v1.18.12',
    major='1',
    minor='18',
    patch='12',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 11, 23),
    commit_sha='7cd5e9086de8ae25d6a1514d0c87bac67ca4a481'
)
