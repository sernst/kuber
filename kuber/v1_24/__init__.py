import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.24",
    version="v1.24.12",
    major="1",
    minor="24",
    patch="12",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2024, 3, 13),
    commit_sha="ef70d260f3d036fc22b30538576bbf6b36329995",
)
