import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.5',
    major='1',
    minor='15',
    patch='5',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 10, 31),
    commit_sha='20c265fef0741dd71a66480e35bd69f18351daea'
)
