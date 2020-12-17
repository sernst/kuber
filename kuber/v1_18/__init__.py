import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label="v1.18",
    version="v1.18.13",
    major="1",
    minor="18",
    patch="13",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2020, 12, 17),
    commit_sha="4c00c3c459261e8ff3381c1070ddf798f0131956",
)
