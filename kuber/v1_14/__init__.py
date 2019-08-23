import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.14',
    version='v1.14.6',
    major='1',
    minor='14',
    patch='6',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 8, 23),
    commit_sha='96fac5cd13a5dc064f7d9f4f23030a6aeface6cc'
)
