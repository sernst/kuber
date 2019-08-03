import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='latest',
    version='v1.15.1',
    major='1',
    minor='15',
    patch='1',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 8, 3),
    commit_sha='4485c6f18cee9a5d3c3b4e523bd27972b1b53892'
)
