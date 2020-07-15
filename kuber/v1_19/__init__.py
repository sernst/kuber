import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.19',
    version='v1.19.0-rc.1',
    major='1',
    minor='19',
    patch='0',
    pre_release='rc.1',
    build='',
    created_at=_datetime.datetime(2020, 7, 15),
    commit_sha='2cbdfecbbd57dbd4e9f42d73a75fbbc6d9eadfd3'
)
