import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.13',
    version='v1.13.10',
    major='1',
    minor='13',
    patch='10',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 9, 10),
    commit_sha='37d169313237cb4ceb2cc4bef300f2ae3053c1a2'
)
