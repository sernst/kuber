import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.11',
    version='v1.11.9',
    major='1',
    minor='11',
    patch='9',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 4, 11),
    commit_sha='16236ce91790d4c75b79f6ce96841db1c843e7d2'
)
