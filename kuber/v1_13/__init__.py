import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.13',
    version='v1.13.7',
    major='1',
    minor='13',
    patch='7',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 6, 30),
    commit_sha='4683545293d792934a7a7e12f2cc47d20b2dd01b'
)
