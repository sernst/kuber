import typing

from kubernetes import client
from kubernetes import config
from kubernetes.client.rest import ApiException

from kuber import definitions
from kuber import versioning


def load_access_config(in_cluster: bool = False, **kwargs) -> typing.NoReturn:
    """
    Initializes the kubernetes library from either a kube configuration
    file for external access or using mounted configuration data for
    access from within a pod in the cluster.

    :param in_cluster:
        Whether or not to initialize access within the cluster or not. By
        default the access will be loaded from a kube config file for
        external access to a cluster.
    :param kwargs:
        Optional arguments to pass ot the external kube-config-based
        initialization process.
    """
    if in_cluster:
        return config.load_incluster_config()
    return config.load_kube_config(**kwargs)


def get_version_from_cluster(
        fallback: typing.Union['versioning.KubernetesVersion', str] = None
) -> versioning.KubernetesVersion:
    """
    Returns the KubernetesVersion object associated with the configured
    cluster. If the cluster version cannot be determined, the specified
    fallback version will be returned instead. If no fallback is specified
    the earliest (oldest) version available in the kuber library installation
    will be used instead.
    """
    versions = versioning.get_all_versions()
    default = fallback or versions[0]
    if not isinstance(default, versioning.KubernetesVersion):
        default = versioning.get_version_data(fallback)

    try:
        response: client.VersionInfo = client.VersionApi().get_code()
        major = response.major
        minor = response.minor.rstrip('+')
    except ApiException:
        return default

    return next(
        (v for v in versions if v.major == major and v.minor == minor),
        default
    )


def execute(
        action: str,
        resource: 'definitions.Resource',
        names: typing.List[str],
        namespace: str = None,
        api_client: client.ApiClient = None,
        api_args: typing.Dict[str, typing.Any] = None
) -> typing.Optional[dict]:
    """
    Executes the specified action on the given resource object using
    the kubernetes API client.

    :param action:
        The CRUD operation to carry out for the given resource.
    :param resource:
        Kuber resource on which to carry out the operation.
    :param names:
        Names of potential kubernetes python client functions that can be
        called to carry out this operation.
    :param namespace:
        Kubernetes namespace in which this execution will take place.
    :param api_client:
        Kubernetes python client API connection to use when carrying out
        the execution.
    :param api_args:
        Keyword arguments to pass through to the kubernetes python client
        execution call.
    """
    api = resource.get_resource_api(api_client=api_client)
    name = next((n for n in names if hasattr(api, n)), None)
    if name is None:
        raise ValueError(
            f'{action.capitalize()} function not found for resource '
            f'{resource.__class__.__name__}'
        )

    func = getattr(api, name)
    func_variables = func.__code__.co_varnames

    args = {**api_args}
    ns = namespace or getattr(resource.metadata, 'namespace', None)
    if ns and 'namespace' in func_variables:
        args['namespace'] = ns

    return getattr(api, name)(**args)


def to_camel_case(source: str) -> str:
    """Converts the specified source string from snake_case to camelCase."""
    parts = source.split('_')
    prefix = parts.pop(0)
    suffix = ''.join([p.capitalize() for p in parts])
    return f'{prefix}{suffix}'


def to_kuber_dict(kube_api_entity) -> dict:
    """
    Converts a Kubernetes client object, or serialized dictionary of
    configuration values to the kuber representation, which enforces
    camelCase and omits any keys with `None` values.

    :param kube_api_entity:
        Either a kubernetes Python client object or a dictionary that
        contains keys and value for a kubernetes resource configuration.
    """
    entity = kube_api_entity
    if hasattr(entity, 'to_dict'):
        entity = entity.to_dict()

    return {
        to_camel_case(k): v
        for k, v in entity.items()
        if v is not None
    }
