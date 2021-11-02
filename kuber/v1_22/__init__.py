import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.22",
    version="v1.22.3",
    major="1",
    minor="22",
    patch="3",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 11, 2),
    commit_sha="c92036820499fedefec0f847e2054d824aea6cd1",
)
