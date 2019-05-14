import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.11',
    version='v1.11.10',
    major='1',
    minor='11',
    patch='10',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 5, 13),
    commit_sha='7a578febe155a7366767abce40d8a16795a96371'
)
