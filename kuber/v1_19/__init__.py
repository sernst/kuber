import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.19",
    version="v1.19.10",
    major="1",
    minor="19",
    patch="10",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 4, 26),
    commit_sha="98d5dc5d36d34a7ee13368a7893dcb400ec4e566",
)
