import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='latest',
    version='v1.14.2',
    major='1',
    minor='14',
    patch='2',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2019, 6, 17),
    commit_sha='66049e3b21efe110454d67df4fa62b08ea79a19b'
)
