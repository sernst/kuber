import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.21",
    version="v1.21.0",
    major="1",
    minor="21",
    patch="0",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 4, 26),
    commit_sha="cb303e613a121a29364f75cc67d3d580833a7479",
)
