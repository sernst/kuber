import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.3',
    major='1',
    minor='15',
    patch='3',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 8, 23),
    commit_sha='2d3c76f9091b6bec110a5e63777c332469e0cba2'
)
