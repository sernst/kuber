import datetime as _datetime

from kuber import versioning

# Information about the kubernetes API library version associated with this
# package and kuber metadata around its creation and labeling within the
# kuber library.
KUBERNETES_VERSION = versioning.KubernetesVersion(
    label='v1.15',
    version='v1.15.0-alpha.1',
    major='1',
    minor='15',
    patch='0',
    pre_release='alpha.1',
    build='',
    created_at=_datetime.datetime(2019, 4, 24),
    commit_sha='84a859fbcfed59cc29d9cf33a0815dcc85348373'
)
