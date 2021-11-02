import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.21",
    version="v1.21.6",
    major="1",
    minor="21",
    patch="6",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 11, 2),
    commit_sha="d921bc6d1810da51177fbd0ed61dc811c5228097",
)
