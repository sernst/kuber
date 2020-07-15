import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.20',
    version='v1.20.0-alpha.0',
    major='1',
    minor='20',
    patch='0',
    pre_release='alpha.0',
    build='',
    created_at=_datetime.datetime(2020, 7, 15),
    commit_sha='82baa26905c94398a0d19e1b1ecf54eb8acb6029'
)
