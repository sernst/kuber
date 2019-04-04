import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.0-alpha.0',
    major='1',
    minor='15',
    patch='0',
    pre_release='alpha.0',
    build='',
    created_at=_datetime.datetime(2019, 4, 4),
    commit_sha='8d69dc630ba66d05ad95146583a7482ed1eb3f82'
)
