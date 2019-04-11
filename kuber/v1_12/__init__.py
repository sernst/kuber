import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.12',
    version='v1.12.7',
    major='1',
    minor='12',
    patch='7',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 4, 11),
    commit_sha='6f482974b76db3f1e0f5d24605a9d1d38fad9a2b'
)
