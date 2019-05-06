import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='pre',
    version='v1.15.0-alpha.2',
    major='1',
    minor='15',
    patch='0',
    pre_release='alpha.2',
    build='',
    created_at=_datetime.datetime(2019, 5, 6),
    commit_sha='306740f81c3b46b745ea85c8c641dcc46e3183cf'
)
