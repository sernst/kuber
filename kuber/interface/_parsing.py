import argparse
import typing

from kuber import management


def _populate_create(subparsers):
    """..."""
    parser = subparsers.add_parser(
        'create',
        help='Create the resource bundle.'
    )
    parser.add_argument(
        '--target', action='append',
        help=(
            'Specify the resource in the bundle to target with this '
            'operation. Only the resource specified will be acted upon. '
            'Use this flag multiple times in the same call to target '
            'multiple resources. If omitted, the default behavior is '
            'to target all resources in the bundle. Targets are specified '
            'as <KIND>/<NAME>, e.g. --target=Namespace/foo.'
        )
    )
    parser.add_argument('--namespace')
    parser.add_argument(
        '--settings', action='append',
        help=(
            'Specify a file path or directory to load settings from. '
            'These settings will be available in the ResourceBundle '
            'to use in dynamically configuring the bundle.'
        )
    )


def _populate_status(subparsers):
    """..."""
    parser = subparsers.add_parser('status', help='Resource bundle status.')
    parser.add_argument('--namespace')
    parser.add_argument(
        '--target', action='append',
        help=(
            'Specify the resource in the bundle to target with this '
            'operation. Only the resource specified will be acted upon. '
            'Use this flag multiple times in the same call to target '
            'multiple resources. If omitted, the default behavior is '
            'to target all resources in the bundle. Targets are specified '
            'as <KIND>/<NAME>, e.g. --target=Namespace/foo.'
        )
    )


def _populate_delete(subparsers):
    """..."""
    parser = subparsers.add_parser(
        'delete',
        help='Delete the resource bundle.'
    )
    parser.add_argument('--namespace')
    parser.add_argument(
        '--target', action='append',
        help=(
            'Specify the resource in the bundle to target with this '
            'operation. Only the resource specified will be acted upon. '
            'Use this flag multiple times in the same call to target '
            'multiple resources. If omitted, the default behavior is '
            'to target all resources in the bundle. Targets are specified '
            'as <KIND>/<NAME>, e.g. --target=Namespace/foo.'
        )
    )


def _populate_render(subparsers):
    """..."""
    parser = subparsers.add_parser('render', help='Render the bundle')
    parser.add_argument('--namespace')
    parser.add_argument(
        '--settings',
        action='append',
        help=(
            'Specify a file path or directory to load settings from. '
            'These settings will be available in the ResourceBundle '
            'to use in dynamically configuring the bundle.'
        )
    )
    parser.add_argument(
        '--target', action='append',
        help=(
            'Specify the resource in the bundle to target with this '
            'operation. Only the resource specified will be acted upon. '
            'Use this flag multiple times in the same call to target '
            'multiple resources. If omitted, the default behavior is '
            'to target all resources in the bundle. Targets are specified '
            'as <KIND>/<NAME>, e.g. --target=Namespace/foo.'
        )
    )


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
