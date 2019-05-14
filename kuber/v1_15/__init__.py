import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.0-alpha.3',
    major='1',
    minor='15',
    patch='0',
    pre_release='alpha.3',
    build='',
    created_at=_datetime.datetime(2019, 5, 13),
    commit_sha='95eb3a67020f6eabef08c3e9caf348149f469798'
)
