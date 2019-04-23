import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.13',
    version='v1.13.5',
    major='1',
    minor='13',
    patch='5',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 4, 23),
    commit_sha='2166946f41b36dea2c4626f90a77706f426cdea2'
)
