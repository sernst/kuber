import argparse
import typing

from kuber import management


class CommandAction(typing.NamedTuple):
    """..."""

    args: argparse.Namespace
    remains: typing.List[str]
    bundle: 'management.ResourceBundle'
    cli: 'ResourceBundleCli'


def _populate_create(subparsers):
    """..."""
    subparsers.add_parser('create', help='Create the resource bundle.')


def _populate_render(subparsers):
    """..."""
    subparsers.add_parser('render', help='Render the bundle')


def _parse_args(
        arguments: typing.Sequence[str] = None
) -> typing.Tuple[argparse.Namespace, typing.List[str]]:
    """..."""
    parser = argparse.ArgumentParser(prog='kuber-resource-bundle')
    subparsers = parser.add_subparsers(
        title='Kuber Resource Bundle Command',
        dest='command'
    )
    _populate_create(subparsers)
    _populate_render(subparsers)

    return parser.parse_known_args(args=arguments)


def do_render(action: CommandAction):
    """..."""
    print(action.bundle.render_yaml_bundle())


def do_create(action: CommandAction):
    """..."""
    print('CREATE', action.bundle)


def do_delete(action: CommandAction):
    """..."""
    print('DELETE', action.bundle)


class ResourceBundleCli:
    """..."""

    def __init__(self, bundle: 'management.ResourceBundle'):
        """..."""
        self._bundle = bundle

    def __call__(self, arguments: typing.Sequence[str] = None):
        """..."""
        args, remains = _parse_args(arguments)
        command_actions = {
            'create': do_create,
            'render': do_render,
            'delete': do_delete
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
