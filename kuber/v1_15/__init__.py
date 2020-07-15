import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.12',
    major='1',
    minor='15',
    patch='12',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 15),
    commit_sha='e2a822d9f3c2fdb5c9bfbe64313cf9f657f0a725'
)
