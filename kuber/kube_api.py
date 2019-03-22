import json
import subprocess
import typing

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


def kube_exec(action: str, args: typing.List[str], stdin: str = None):
    """..."""
    cmd = ['kubectl', action, *(args or [])]
    result = subprocess.run(
        cmd,
        input=stdin,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    try:
        data = json.loads(result.stdout or '')
    except json.JSONDecodeError as error:
        data = {}

    return KubectlResponse(
        success=result.returncode == 0,
        action=action,
        args=args,
        input=stdin,
        output=result.stdout,
        error=result.stderr,
        data=data
    )


def create_resource(
        resource: 'definitions.Resource',
        namespace: 'str' = None
) -> KubectlResponse:
    """..."""
    args = ['-f', '-', '--output=json']
    if namespace:
        args += ['--namespace', namespace]
    result = kube_exec('create', args=args, stdin=resource.to_json())
    if not result.success:
        print(result.error)
        raise KubectlError(result, f'Failed to create {resource.kind}')
    return result


def get_resource(
        resource: 'definitions.Resource',
        namespace: 'str' = None
) -> KubectlResponse:
    """..."""
    args = ['-f', '-', '--output=json']
    if namespace:
        args += ['--namespace', namespace]
    result = kube_exec('get', args=args, stdin=resource.to_json())
    if not result.success:
        print(result.error)
        raise KubectlError(result, f'Failed to get {resource.kind}')
    return result


def replace_resource(
        resource: 'definitions.Resource',
        namespace: 'str' = None
) -> KubectlResponse:
    """..."""
    args = ['-f', '-', '--output=json']
    if namespace:
        args += ['--namespace', namespace]
    result = kube_exec('replace', args=args, stdin=resource.to_json())
    if not result.success:
        print(result.error)
        raise KubectlError(result, f'Failed to replace {resource.kind}')
    return result


def delete_resource(
        resource: 'definitions.Resource',
        namespace: 'str' = None
) -> KubectlResponse:
    """..."""
    args = ['-f', '-']
    if namespace:
        args += ['--namespace', namespace]
    result = kube_exec('delete', args=args, stdin=resource.to_json())
    if not result.success:
        print(result.error)
        raise KubectlError(result, f'Failed to delete {resource.kind}')
    return result
