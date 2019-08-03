import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='pre',
    version='v1.16.0-alpha.2',
    major='1',
    minor='16',
    patch='0',
    pre_release='alpha.2',
    build='',
    created_at=_datetime.datetime(2019, 8, 3),
    commit_sha='a23fc83fcd6b0602fcc6de017c97fac85251a44f'
)
