import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.16",
    version="v1.16.15",
    major="1",
    minor="16",
    patch="15",
    pre_release="",
    build="",
    created_at=_datetime.datetime(2021, 1, 7),
    commit_sha="2adc8d7091e89b6e3ca8d048140618ec89b39369",
)
