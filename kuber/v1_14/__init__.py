import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.14',
    version='v1.14.1',
    major='1',
    minor='14',
    patch='1',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 4, 11),
    commit_sha='b7394102d6ef778017f2ca4046abbaa23b88c290'
)
