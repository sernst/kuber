import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.16',
    version='v1.16.8',
    major='1',
    minor='16',
    patch='8',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 3, 24),
    commit_sha='ec6eb119b81be488b030e849b9e64fda4caaf33c'
)
