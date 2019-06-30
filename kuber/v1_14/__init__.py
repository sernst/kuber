import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.14',
    version='v1.14.3',
    major='1',
    minor='14',
    patch='3',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 6, 30),
    commit_sha='5e53fd6bc17c0dec8434817e69b04a25d8ae0ff0'
)
