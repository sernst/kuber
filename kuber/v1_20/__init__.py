import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label="v1.20",
    version="v1.20.0-rc.0",
    major="1",
    minor="20",
    patch="0",
    pre_release="rc.0",
    build="",
    created_at=_datetime.datetime(2020, 12, 8),
    commit_sha="3321f00ed14e07f774b84d3198ede545c1dee697",
)
