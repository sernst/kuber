from unittest.mock import MagicMock
from unittest.mock import patch

from kuber import execution
from kuber.tests import utils as test_utils


def test_parse_api_exception():
    """
    Should parse ApiException into a response info object when the exception
    body cannot be parsed.
    """
    resource = MagicMock()
    error = MagicMock()
    error.body = '{"reason": "foo"}'
    response = execution._parse_api_exception(resource, error)
    assert response.reason == 'foo'


def test_parse_api_exception_no_body():
    """
    Should parse ApiException into a response info object when the exception
    body cannot be parsed.
    """
    resource = MagicMock()
    error = MagicMock()
    error.body = '{"a'
    response = execution._parse_api_exception(resource, error)
    assert response.reason == 'UnknownError'


def test_echo_response_normal():
    """Should display message without error when response is normal."""
    response = execution.ResponseInfo(
        resource=MagicMock(),
        symbol='  ',
        reason='Success',
        message='foo'
    )
    execution._echo_response(response)


def test_echo_response_error():
    """Should display message without error when response is an error."""
    response = execution.ResponseInfo(
        resource=MagicMock(),
        symbol='!!',
        reason='Failure',
        message='Error occurred',
        exception=MagicMock()
    )
    execution._echo_response(response)


def test_create_resource():
    """Should create resource successfully when no error is caught."""
    response = execution.create_resource(MagicMock(), echo=True)
    assert response.symbol == '+'
    assert response.reason == 'Created'


def test_create_resource_error():
    """Should handle failed resource creation error."""
    resource = MagicMock()
    resource.create_resource.side_effect = test_utils.MockApiException(
        successful=False
    )
    response = execution.create_resource(resource, echo=True)

    resource.create_resource.assert_called_once()
    assert response.symbol == '!!'
    assert response.reason == 'Testing'


@patch('kuber.execution.patch_resource')
def test_create_resource_exists(patch_resource: MagicMock):
    """Should attempt to patch resource if it already exists."""
    resource = MagicMock()
    resource.create_resource.side_effect = test_utils.MockApiException(
        successful=False,
        reason='AlreadyExists'
    )
    execution.create_resource(resource, echo=True)

    resource.create_resource.assert_called_once()
    patch_resource.assert_called_once()


def test_replace_resource():
    """Should replace resource successfully when no error is caught."""
    response = execution.replace_resource(MagicMock(), echo=True)
    assert response.symbol == '-/+'
    assert response.reason == 'Replaced'


def test_replace_resource_error():
    """Should handle failed resource replacement error."""
    resource = MagicMock()
    resource.replace_resource.side_effect = test_utils.MockApiException(
        successful=False
    )
    response = execution.replace_resource(resource, echo=True)

    resource.replace_resource.assert_called_once()
    assert response.symbol == '!!'
    assert response.reason == 'Testing'


def test_patch_resource():
    """Should patch resource successfully when no error is caught."""
    response = execution.patch_resource(MagicMock(), echo=True)
    assert response.symbol == '~'
    assert response.reason == 'Updated'


def test_patch_resource_error():
    """Should handle failed resource patching error."""
    resource = MagicMock()
    resource.patch_resource.side_effect = test_utils.MockApiException(
        successful=False
    )
    response = execution.patch_resource(resource, echo=True)

    resource.patch_resource.assert_called_once()
    assert response.symbol == '!!'
    assert response.reason == 'Testing'


def test_delete_resource():
    """Should delete resource successfully when no error is caught."""
    response = execution.delete_resource(MagicMock(), echo=True)
    assert response.symbol == '-'
    assert response.reason == 'Deleted'


def test_delete_resource_error():
    """Should handle failed resource deletion error."""
    resource = MagicMock()
    resource.delete_resource.side_effect = test_utils.MockApiException(
        successful=False
    )
    response = execution.delete_resource(resource, echo=True)

    resource.delete_resource.assert_called_once()
    assert response.symbol == '!!'
    assert response.reason == 'Testing'


def test_get_resource_status_error():
    """Should handle failed resource status retrieval error."""
    resource = MagicMock()
    resource.get_resource_status.side_effect = test_utils.MockApiException(
        successful=False
    )
    response = execution.get_resource_status(resource, echo=True)

    resource.get_resource_status.assert_called_once()
    assert response.symbol == '!!'
    assert response.reason == 'Testing'


def test_get_resource_status():
    """Should successfully get status for resource."""
    status = MagicMock()
    status.to_dict.return_value = {'foo': 'bar'}
    resource = MagicMock()
    resource.get_resource_status.return_value = status
    response = execution.get_resource_status(resource, echo=True)

    resource.get_resource_status.assert_called_once()
    assert response.symbol == '*'
    assert response.reason == 'Status'
    assert 'foo' in response.message and 'bar' in response.message


def test_get_resource_status_no_status_object():
    """Should successfully get status for resource."""
    resource = MagicMock()
    resource.get_resource_status.return_value = None
    response = execution.get_resource_status(resource, echo=True)

    resource.get_resource_status.assert_called_once()
    assert response.symbol == '*'
    assert response.reason == 'Status'
