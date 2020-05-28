import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.19',
    version='v1.19.0-beta.0',
    major='1',
    minor='19',
    patch='0',
    pre_release='beta.0',
    build='',
    created_at=_datetime.datetime(2020, 5, 28),
    commit_sha='6a0e01880ad7ea4c110040c3be417516c0bf6bca'
)
