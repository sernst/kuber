import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='pre',
    version='v1.18.0-alpha.0',
    major='1',
    minor='18',
    patch='0',
    pre_release='alpha.0',
    build='',
    created_at=_datetime.datetime(2019, 10, 31),
    commit_sha='9731b51d2369f10e511d02275327bc0e63c5902c'
)
