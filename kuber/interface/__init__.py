import argparse
import os
import typing

import kuber
from kuber import execution
from kuber import management
from kuber.interface import _parsing


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
        action = CommandAction(
            args=args,
            custom_args=remains,
            bundle=self._bundle
        )
        _populate_settings(action)
        if callback is not None:
            callback(action)
        return command_actions[command](action)


def _is_target(action: CommandAction, resource: 'kuber.Resource') -> bool:
    """
    Determines whether or not the specified resource should be included
    in the command line action.
    """
    targets = [t.lower() for t in (vars(action.args).get('target') or [])]
    if not targets:
        return True

    identifier = f'{resource.kind}/{resource.metadata.name}'.lower()
    return identifier in targets


def do_render(action: CommandAction) -> CommandAction:
    """
    Carries out a render to display action for command line interaction.
    """
    renders = [
        resource.to_yaml()
        for resource in action.bundle.resources
        if _is_target(action, resource)
    ]
    print('\n---\n\n'.join(renders))
    return action


def do_create(action: CommandAction) -> CommandAction:
    """
    Carries out a create action for the command line interaction.
    """
    default_namespace = action.args.namespace or action.bundle.namespace
    print(f'\n=== CREATING BUNDLE {action.bundle.name} ===')
    responses = [
        execution.create_resource(
            resource=resource,
            namespace=resource.metadata.namespace or default_namespace,
            echo=True
        )
        for resource in action.bundle.resources
        if _is_target(action, resource)
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
    default_namespace = action.args.namespace or action.bundle.namespace
    print(f'\n=== DELETING BUNDLE {action.bundle.name} ===')
    responses = [
        execution.delete_resource(
            resource=resource,
            namespace=resource.metadata.namespace or default_namespace,
            echo=True
        )
        for resource in action.bundle.resources
        if _is_target(action, resource)
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
    default_namespace = action.args.namespace or action.bundle.namespace
    print(f'\n=== BUNDLE STATUS {action.bundle.name} ===')
    responses = [
        execution.get_resource_status(
            resource=resource,
            namespace=resource.metadata.namespace or default_namespace,
            echo=True
        )
        for resource in action.bundle.resources
        if _is_target(action, resource)
    ]
    has_error = any([r.symbol == '!!' for r in responses])
    if has_error:
        print('\nWARNING: Unable to get status of all resources.\n\n')
    return action


def _populate_settings(action: CommandAction):
    """
    Loads any number of specified settings files/directories into the
    :param action:
    """
    try:
        settings_paths = action.args.settings or []
    except AttributeError:  # pragma: no cover
        return

    for path in settings_paths:
        if os.path.isdir(path):
            action.bundle.settings.add_from_directory(path)
        elif os.path.isfile(path):
            action.bundle.settings.add_from_file(path)
        else:
            raise ValueError(
                f'The settings "{path}" path is invalid or could not '
                'be found.'
            )
