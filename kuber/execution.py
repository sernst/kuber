import json
import textwrap
import typing

import yaml
from kubernetes.client.rest import ApiException

from kuber import definitions

CREATE_SYMBOLS = {
    'AlreadyExists': '=',
    'NotFound': '!!'
}

STATUS_SYMBOLS = {
    'NotFound': ' '
}

DELETE_SYMBOLS = {
    'NotFound': ' '
}


class ResponseInfo(typing.NamedTuple):
    """Data structure for parsed ApiExceptions."""

    resource: 'definitions.Resource'
    symbol: str
    reason: str
    message: str = None
    exception: typing.Optional[ApiException] = None
    status: typing.Optional['definitions.Definition'] = None


def _parse_api_exception(
        resource: 'definitions.Resource',
        error: ApiException,
        symbols: dict = None
) -> ResponseInfo:
    """Returns the parsed body of the given error"""
    try:
        body = json.loads(error.body)
    except json.JSONDecodeError:
        body = {}

    reason = body.get('reason', 'UnknownError')
    return ResponseInfo(
        resource=resource,
        symbol=(symbols or {}).get(reason, '!!'),
        reason=reason,
        message='{}'.format(body.get('message', error)),
        exception=error
    )


def _echo_response(response: ResponseInfo):
    """Displays the response for human consumption."""
    resource_id = '{}/{}'.format(
        response.resource.kind,
        response.resource.metadata.name or response.resource.kuber_uid
    )
    wrap = '\n' if response.symbol == '!!' else ''
    print(f'{wrap}[{response.symbol}] {response.reason}: {resource_id}{wrap}')

    if response.symbol not in ('!!', '*'):
        return

    message = '\n'.join(textwrap.wrap(response.message, 70))
    print(textwrap.indent(message, prefix='   '), end='\n\n')

    if response.symbol == '!!':
        print(
            textwrap.indent(response.resource.to_yaml(), prefix='   '),
            end='\n\n'
        )


def create_resource(
        resource: 'definitions.Resource',
        namespace: str = None,
        echo: bool = False
) -> ResponseInfo:
    """..."""
    try:
        status = resource.create_resource(namespace)
        response = ResponseInfo(resource, '+', 'Created', status=status)
    except ApiException as error:
        response = _parse_api_exception(resource, error)

    if response.reason == 'AlreadyExists':
        return patch_resource(resource, namespace, echo)

    if echo:
        _echo_response(response)
    return response


def replace_resource(
        resource: 'definitions.Resource',
        namespace: str = None,
        echo: bool = False
) -> ResponseInfo:
    """..."""
    try:
        status = resource.replace_resource(namespace)
        response = ResponseInfo(resource, '-/+', 'Replaced', status=status)
    except ApiException as error:
        response = _parse_api_exception(resource, error)

    if echo:
        _echo_response(response)
    return response


def patch_resource(
        resource: 'definitions.Resource',
        namespace: str = None,
        echo: bool = False
) -> ResponseInfo:
    """..."""
    try:
        status = resource.patch_resource(namespace)
        response = ResponseInfo(resource, '~', 'Updated', status=status)
    except ApiException as error:
        response = _parse_api_exception(resource, error)

    if echo:
        _echo_response(response)
    return response


def get_resource_status(
        resource: 'definitions.Resource',
        namespace: str = None,
        echo: bool = False
) -> ResponseInfo:
    """Shows statuses of resources in the bundle."""
    try:
        status: definitions.Definition = resource.get_resource_status(
            namespace=namespace
        )
        if status is not None and status.to_dict():
            message = yaml.dump(status.to_dict(), default_flow_style=False)
            response = ResponseInfo(
                resource=resource,
                symbol='*',
                reason='Status',
                message=message,
                status=status
            )
        else:
            status = resource.read_resource(namespace=namespace)
            response = ResponseInfo(
                resource=resource,
                symbol='*',
                reason='Status',
                message='Exists in cluster and is behaving as expected.',
                status=status
            )
    except ApiException as error:
        response = _parse_api_exception(resource, error)

    if echo:
        _echo_response(response)
    return response


def delete_resource(
        resource: 'definitions.Resource',
        namespace: str = None,
        echo: bool = False
) -> ResponseInfo:
    """..."""
    try:
        status = resource.delete_resource(namespace)
        response = ResponseInfo(resource, '-', 'Deleted', status=status)
    except ApiException as error:
        response = _parse_api_exception(resource, error)

    if echo:
        _echo_response(response)
    return response
