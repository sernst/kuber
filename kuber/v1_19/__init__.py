import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.19',
    version='v1.19.0-rc.2',
    major='1',
    minor='19',
    patch='0',
    pre_release='rc.2',
    build='',
    created_at=_datetime.datetime(2020, 7, 24),
    commit_sha='27bb2a4a0a5cb8330178d19e57fa61fffa895c98'
)
