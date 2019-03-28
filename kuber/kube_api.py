import json
import subprocess
import typing

from kubernetes import client

from kuber import definitions


class KubectlError(Exception):
    """Errors from Kubectl command execution."""

    def __init__(self, result: 'KubectlResponse', message: str):
        super(KubectlError, self).__init__(message)
        self._result = result

    @property
    def result(self) -> 'KubectlResponse':
        """The Kubectl command execution results."""
        return self._result


class KubectlResponse(typing.NamedTuple):
    """Data structure for Kubectl command results."""

    success: bool
    action: str
    output: str
    data: dict = None
    error: str = None
    args: typing.List[str] = None
    input: str = None


def execute(
        action: str,
        resource: 'definitions.Resource',
        names: typing.List[str],
        namespace: str = None,
        api_client: client.ApiClient = None,
        api_args: typing.Dict[str, typing.Any] = None
) -> typing.Optional[dict]:
    """..."""
    api = resource.get_resource_api(api_client=api_client)
    name = next((n for n in names if hasattr(api, n)), None)
    if name is None:
        raise ValueError(
            f'{action.capitalize()} function not found for resource '
            f'{resource.__class__.__name__}'
        )

    args = {**api_args}
    ns = namespace or getattr(resource.metadata, 'namespace', None)
    if ns and 'namespace' in name:
        args['namespace'] = ns

    return getattr(api, name)(**args)


def to_camel_case(source: str) -> str:
    """..."""
    parts = source.split('_')
    prefix = parts.pop(0)
    suffix = ''.join([p.capitalize() for p in parts])
    return f'{prefix}{suffix}'


def to_kuber_dict(kube_api_entity) -> dict:
    """..."""
    entity = kube_api_entity
    if hasattr(entity, 'to_dict'):
        entity = entity.to_dict()

    return {
        to_camel_case(k): v
        for k, v in entity.items()
        if v is not None
    }
