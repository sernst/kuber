import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.17',
    version='v1.17.9',
    major='1',
    minor='17',
    patch='9',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 24),
    commit_sha='4fb7ed12476d57b8437ada90b4f93b17ffaeed99'
)
