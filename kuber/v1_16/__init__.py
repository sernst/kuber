import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.16',
    version='v1.16.13',
    major='1',
    minor='16',
    patch='13',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 24),
    commit_sha='39a145ca3413079bcb9c80846488786fed5fe1cb'
)
