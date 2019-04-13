import argparse
import typing

from kuber import execution
from kuber import management
from kuber.cli import _parsing


class CommandAction(typing.NamedTuple):
    """Data structure for CLI command invocations."""

    #: Arguments parsed for the Kuber CLI to use during command execution.
    args: argparse.Namespace
    #: Unparsed arguments that are available in invocation callbacks to
    #: further customize the bundle.
    custom_args: typing.List[str]
    #: The resource bundle on which to operate.
    bundle: 'management.ResourceBundle'


class ResourceBundleCli:
    """Manages command line interface actions for ResourceBundles."""

    def __init__(self, bundle: 'management.ResourceBundle'):
        """Creates a ResourceBundleCli for the given ResourceBundle."""
        self._bundle = bundle

    def __call__(self, arguments: typing.Sequence[str] = None):
        """
        Invokes the command line interface for the bundle.

        :param arguments:
            Optional command line arguments to parse for the cli action
            execution. If omitted the arguments will be parsed from the
            sys.argv values provided on the command line.
        """
        return self.invoke(arguments=arguments)

    def invoke(
            self,
            callback: typing.Callable[[CommandAction], typing.Any] = None,
            arguments: typing.List[str] = None
    ):
        """
        Invokes the command line interface for the bundle, but calls the given
        callback before executing the cli command. The callback is the
        opportunity to configure the bundle based on custom arguments.

        :param callback:
            Callback that will be executed prior to the command line action
            execution. Use this callback to configure the bundle using input
            from the command line (including custom command arguments) before
            the cli command action is invoked.
        :param arguments:
            Optional command line arguments to parse and use in the callback
            and then in the cli action execution. If omitted the arguments
            will be parsed from the sys.argv values provided on the command
            line.
        """
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
            custom_args=remains,
            bundle=self._bundle
        )
        if callback is not None:
            callback(action)
        return command_actions[command](action)


def do_render(action: CommandAction) -> CommandAction:
    """
    Carries out a render to display action for command line interaction.
    """
    print(action.bundle.render_yaml_bundle())
    return action


def do_create(action: CommandAction) -> CommandAction:
    """
    Carries out a create action for the command line interaction.
    """
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
    return action


def do_delete(action: CommandAction) -> CommandAction:
    """
    Carries out a delete action for the command line interaction.
    """
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
    return action


def do_status(action: CommandAction) -> CommandAction:
    """
    Carries out a status display action for the command line interaction.
    """
    namespace = action.args.namespace or action.bundle.namespace
    print(f'\n=== BUNDLE STATUS {action.bundle.name} ===')
    responses = [
        execution.get_resource_status(r, namespace, echo=True)
        for r in action.bundle.resources
    ]
    has_error = any([r.symbol == '!!' for r in responses])
    if has_error:
        print('\nWARNING: Unable to get status of all resources.\n\n')
    return action
