import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.11',
    major='1',
    minor='15',
    patch='11',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 3, 24),
    commit_sha='d94a81c724ea8e1ccc9002d89b7fe81d58f89ede'
)
