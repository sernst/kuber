import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.18',
    version='v1.18.3',
    major='1',
    minor='18',
    patch='3',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 5, 28),
    commit_sha='2e7996e3e2712684bc73f0dec0200d64eec7fe40'
)
