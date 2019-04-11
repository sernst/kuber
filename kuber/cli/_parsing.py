import argparse
import typing

from kuber import management


def _populate_create(subparsers):
    """..."""
    parser = subparsers.add_parser(
        'create',
        help='Create the resource bundle.'
    )
    parser.add_argument('--namespace')


def _populate_status(subparsers):
    """..."""
    parser = subparsers.add_parser('status', help='Resource bundle status.')
    parser.add_argument('--namespace')


def _populate_delete(subparsers):
    """..."""
    parser = subparsers.add_parser(
        'delete',
        help='Delete the resource bundle.'
    )
    parser.add_argument('--namespace')


def _populate_render(subparsers):
    """..."""
    subparsers.add_parser('render', help='Render the bundle')


def parse_args(
        bundle: 'management.ResourceBundle',
        arguments: typing.Sequence[str] = None
) -> typing.Tuple[argparse.Namespace, typing.List[str]]:
    """Parses the CLI command line arguments."""
    parser = argparse.ArgumentParser(prog=bundle.name)
    subparsers = parser.add_subparsers(
        title='Kuber Resource Bundle Command',
        dest='command'
    )
    _populate_create(subparsers)
    _populate_delete(subparsers)
    _populate_render(subparsers)
    _populate_status(subparsers)

    return parser.parse_known_args(args=arguments)
