import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.19",
    version="v1.19.16",
    major="1",
    minor="19",
    patch="16",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 11, 2),
    commit_sha="e37e4ab4cc8dcda84f1344dda47a97bb1927d074",
)
