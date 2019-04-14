from unittest.mock import MagicMock
from unittest.mock import patch

from pytest import mark

from kuber import execution
from kuber import interface

RESPONSE_SCENARIOS = [
    execution.ResponseInfo(
        resource=MagicMock(),
        symbol='!!',
        reason='Failure',
        message='Error occurred',
        exception=MagicMock()
    ),
    execution.ResponseInfo(
        resource=MagicMock(),
        symbol='',
        reason='Success',
        message='No error occurred'
    ),
]


@mark.parametrize('response', RESPONSE_SCENARIOS)
@patch('kuber.execution.get_resource_status')
def test_do_status(
        get_resource_status: MagicMock,
        response: execution.ResponseInfo
):
    """Should get statuses of all resources and display them."""
    get_resource_status.return_value = response
    bundle = MagicMock()
    bundle.resources = [MagicMock(), MagicMock()]
    action = interface.CommandAction(MagicMock(), [], bundle)
    interface.do_status(action)
    assert get_resource_status.call_count == 2


@mark.parametrize('response', RESPONSE_SCENARIOS)
@patch('kuber.execution.delete_resource')
def test_do_delete(
        delete_resource: MagicMock,
        response: execution.ResponseInfo
):
    """Should execute a delete of all resources in the bundle."""
    delete_resource.return_value = response
    bundle = MagicMock()
    bundle.resources = [MagicMock(), MagicMock()]
    action = interface.CommandAction(MagicMock(), [], bundle)
    interface.do_delete(action)
    assert delete_resource.call_count == 2


@mark.parametrize('response', RESPONSE_SCENARIOS)
@patch('kuber.execution.create_resource')
def test_do_create(
        create_resource: MagicMock,
        response: execution.ResponseInfo
):
    """Should execute a creation for all resources in the bundle."""
    create_resource.return_value = response
    bundle = MagicMock()
    bundle.resources = [MagicMock(), MagicMock()]
    action = interface.CommandAction(MagicMock(), [], bundle)
    interface.do_create(action)
    assert create_resource.call_count == 2


def test_do_render():
    """Should render all resources in the bundle to the display."""
    bundle = MagicMock()
    bundle.resources = [MagicMock(), MagicMock()]
    action = interface.CommandAction(MagicMock(), [], bundle)
    interface.do_render(action)


def test_cli():
    """Should execute a render operation without error."""
    interface.ResourceBundleCli(MagicMock())(['render'])
