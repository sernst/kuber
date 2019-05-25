import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.16',
    version='v1.16.0-alpha.0',
    major='1',
    minor='16',
    patch='0',
    pre_release='alpha.0',
    build='',
    created_at=_datetime.datetime(2019, 5, 25),
    commit_sha='c85c0e4780e428fdfb33debc31bc88f8095e5831'
)
