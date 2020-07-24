import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.18',
    version='v1.18.6',
    major='1',
    minor='18',
    patch='6',
    pre_release='',
    build='',
    created_at=_datetime.datetime(2020, 7, 24),
    commit_sha='dff82dc0de47299ab66c83c626e08b245ab19037'
)
