import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.18',
    version='v1.18.0-rc.1',
    major='1',
    minor='18',
    patch='0',
    pre_release='rc.1',
    build='',
    created_at=_datetime.datetime(2020, 3, 24),
    commit_sha='dbbed7806681109f541264ab37284f9a51c87fcc'
)
