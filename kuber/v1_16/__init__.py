import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.16',
    version='v1.16.12',
    major='1',
    minor='16',
    patch='12',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 15),
    commit_sha='17c50ce2d686f4346924935063e3a431360e0db7'
)
