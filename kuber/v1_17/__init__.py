import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.17',
    version='v1.17.14',
    major='1',
    minor='17',
    patch='14',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 11, 23),
    commit_sha='f238f5142728be4033c37aa0ad69bf806090beae'
)
