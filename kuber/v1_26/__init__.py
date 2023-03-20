import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.26",
    version="v1.26.3",
    major="1",
    minor="26",
    patch="3",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2023, 3, 20),
    commit_sha="9e644106593f3f4aa98f8a84b23db5fa378900bd",
)
