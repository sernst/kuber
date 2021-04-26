import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.20",
    version="v1.20.6",
    major="1",
    minor="20",
    patch="6",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 4, 26),
    commit_sha="8a62859e515889f07e3e3be6a1080413f17cf2c3",
)
