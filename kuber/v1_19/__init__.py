import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.19',
    version='v1.19.4',
    major='1',
    minor='19',
    patch='4',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 11, 23),
    commit_sha='d360454c9bcd1634cf4cc52d1867af5491dc9c5f'
)
