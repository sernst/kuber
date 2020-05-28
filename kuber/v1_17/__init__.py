import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.17',
    version='v1.17.6',
    major='1',
    minor='17',
    patch='6',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 5, 28),
    commit_sha='d32e40e20d167e103faf894261614c5b45c44198'
)
