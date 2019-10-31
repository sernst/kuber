import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='latest',
    version='v1.16.2',
    major='1',
    minor='16',
    patch='2',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 10, 31),
    commit_sha='c97fe5036ef3df2967d086711e6c0c405941e14b'
)
