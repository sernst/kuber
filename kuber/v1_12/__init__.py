import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.12',
    version='v1.12.8',
    major='1',
    minor='12',
    patch='8',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 5, 13),
    commit_sha='a89f8c11a5f4f132503edbc4918c98518fd504e3'
)
