import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.17',
    version='v1.17.0-alpha.0',
    major='1',
    minor='17',
    patch='0',
    pre_release='alpha.0',
    build='',
    created_at=_datetime.datetime(2019, 8, 23),
    commit_sha='ac2295a24d3a8087a1129ff832a42b0ad74f94fc'
)
