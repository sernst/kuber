import datetime as _datetime

from kuber import versioning as _versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = _versioning.KubernetesVersion(
    label="v1.23",
    version="v1.23.0-alpha.3",
    major="1",
    minor="23",
    patch="0",
    pre_release="alpha.3",
    build="",
    created_at=_datetime.datetime(2021, 11, 2),
    commit_sha="90051602459ca81bcdfd91ff3d12ca5bde50a7a7",
)
