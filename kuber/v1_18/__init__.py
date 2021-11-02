import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.18",
    version="v1.18.18",
    major="1",
    minor="18",
    patch="18",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 11, 2),
    commit_sha="6f6ce59dc8fefde25a3ba0ef0047f4ec6662ef24",
)
