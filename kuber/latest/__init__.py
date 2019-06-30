import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='latest',
    version='v1.15.0',
    major='1',
    minor='15',
    patch='0',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 6, 30),
    commit_sha='e8462b5b5dc2584fdcd18e6bcfe9f1e4d970a529'
)
