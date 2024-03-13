import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.23",
    version="v1.23.17",
    major="1",
    minor="23",
    patch="17",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2024, 3, 13),
    commit_sha="953be8927218ec8067e1af2641e540238ffd7576",
)
