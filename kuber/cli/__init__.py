import argparse
import typing
from pprint import pprint

from kuber import definitions
from kuber import management
from kuber import execution
from kuber.cli import _parsing


class CommandAction(typing.NamedTuple):
    """..."""

    args: argparse.Namespace
    remains: typing.List[str]
    bundle: 'management.ResourceBundle'
    cli: 'ResourceBundleCli'


class ResourceBundleCli:
    """..."""

    def __init__(self, bundle: 'management.ResourceBundle'):
        """..."""
        self._bundle = bundle

    def __call__(self, arguments: typing.Sequence[str] = None):
        """..."""
        args, remains = _parsing.parse_args(self._bundle, arguments)
        command_actions = {
            'create': do_create,
            'delete': do_delete,
            'render': do_render,
            'status': do_status
        }
        command = args.command or 'render'
        if command not in command_actions:
            raise ValueError(f'Unknown command "{command}"')

        action = CommandAction(
            args=args,
            remains=remains,
            bundle=self._bundle,
            cli=self
        )
        return command_actions[command](action)


def do_render(action: CommandAction):
    """..."""
    print(action.bundle.render_yaml_bundle())


def do_create(action: CommandAction):
    """..."""
    namespace = action.args.namespace or action.bundle.namespace
    print(f'\n=== CREATING BUNDLE {action.bundle.name} ===')
    responses = [
        execution.create_resource(resource, namespace, echo=True)
        for resource in action.bundle.resources
    ]
    has_error = any([r.symbol == '!!' for r in responses])
    if has_error:
        print('\nWARNING: One or more resources errored during creation.\n\n')
    else:
        print('\nSUCCESS: The creation is complete.\n\n')


def do_delete(action: CommandAction):
    """..."""
    namespace = action.args.namespace or action.bundle.namespace
    print(f'\n=== DELETING BUNDLE {action.bundle.name} ===')
    responses = [
        execution.delete_resource(resource, namespace, echo=True)
        for resource in action.bundle.resources
    ]
    has_error = any([r.symbol == '!!' for r in responses])
    if has_error:
        print('\nWARNING: One or more resources errored during deletion.\n\n')
    else:
        print('\nSUCCESS: The deletion is complete.\n\n')


def do_status(action: CommandAction):
    """..."""
    namespace = action.args.namespace or action.bundle.namespace
    print(f'\n=== BUNDLE STATUS {action.bundle.name} ===')
    responses = [
        execution.get_resource_status(r, namespace, echo=True)
        for r in action.bundle.resources
    ]
    has_error = any([r.symbol == '!!' for r in responses])
    if has_error:
        print('\nWARNING: Unable to get status of all resources.\n\n')
