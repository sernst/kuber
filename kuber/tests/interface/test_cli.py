import os
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from pytest import mark

import kuber
from kuber import execution
from kuber import interface

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))

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
    resource = MagicMock()
    resource.to_yaml.return_value = ''
    bundle.resources = [resource, resource]
    action = interface.CommandAction(MagicMock(), [], bundle)
    interface.do_render(action)


def test_cli():
    """Should execute a render operation without error."""
    interface.ResourceBundleCli(MagicMock())(['render'])


def test_settings_directory():
    """Should load settings from this test directory."""
    def _callback(action: kuber.CommandAction):
        s = action.bundle.settings
        assert s.foo and s.foo == s.spam
        assert s.bar and s.bar == s.ham
        assert s.baz and s.baz == s.eggs

    cb = MagicMock()
    cb.side_effect = _callback
    kuber.cli(cb, arguments=['render', f'--settings={MY_DIRECTORY}'])
    cb.assert_called_once()


def test_settings_files():
    """Should load settings from this test files."""
    def _callback(action: kuber.CommandAction):
        s = action.bundle.settings
        assert s.foo and s.foo == s.spam
        assert s.bar and s.bar == s.ham
        assert s.baz and s.baz == s.eggs

    cb = MagicMock()
    cb.side_effect = _callback

    kuber.cli(cb, arguments=[
        'render',
        f'--settings={os.path.join(MY_DIRECTORY, "settings.yaml")}',
        f'--settings={os.path.join(MY_DIRECTORY, "settings.json")}',
    ])
    cb.assert_called_once()


def test_settings_error():
    """Should load settings from this test files."""
    cb = MagicMock()

    with pytest.raises(ValueError):
        kuber.cli(cb, arguments=['render', '--settings=foo'])

    cb.assert_not_called()


@patch('kuber.execution.get_resource_status')
def test_targeting_all(get_resource_status: MagicMock):
    """Should target all resources if no target is set on the command line."""
    get_resource_status.return_value = RESPONSE_SCENARIOS[-1]
    bundle = kuber.create_bundle()
    bundle.add('v1', 'Namespace', 'foo')
    bundle.add('v1', 'Namespace', 'bar')
    bundle.add('v1', 'Namespace', 'baz')

    bundle.cli(arguments=['status'])
    assert get_resource_status.call_count == 3


@patch('kuber.execution.get_resource_status')
def test_targeting(get_resource_status: MagicMock):
    """Should target the one matching resource specified in the command."""
    get_resource_status.return_value = RESPONSE_SCENARIOS[-1]
    bundle = kuber.create_bundle()
    bundle.add('v1', 'Namespace', 'foo')
    bundle.add('v1', 'Namespace', 'bar')
    bundle.add('v1', 'Namespace', 'baz')

    bundle.cli(arguments=['status', '--target=namespace/foo'])
    assert get_resource_status.call_count == 1
