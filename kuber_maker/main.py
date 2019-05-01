import argparse
import os
import typing

import kuber_maker
from kuber_maker import documenting
from kuber_maker import initializer
from kuber_maker import packaging
from kuber_maker import parsing
from kuber_maker import render
from kuber_maker import updater


def generate(version: str):
    """..."""
    spec = kuber_maker.load_spec(version)
    initializer.empty(version)
    initializer.create_subpackages(version, spec.definitions)
    entities = parsing.parse_definitions(version, spec.definitions)

    for package in entities.packages.keys():
        contents = render.render_package(package, entities)
        path = kuber_maker.directory_of_package(package)

        with open(f'{path}.py', 'wb') as f:
            f.write(contents.encode())
        print(f'[CREATED]: {path}.py')

    contents = render.render_root_package(version, spec)
    path = kuber_maker.get_path(version, '__init__.py')
    with open(path, 'w') as f:
        f.write(contents)
    print(f'[RENDERED]: {path}')


def generate_all():
    """..."""
    directory = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'specs'
    ))
    spec_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    for filename in spec_files:
        version = filename[:-5]
        print(f'\n\n=== {version} ===')
        generate(version)


def main(args: typing.List[str] = None):
    """..."""
    parser = argparse.ArgumentParser(prog='kuber_maker')
    subs = parser.add_subparsers(dest='action')

    p = subs.add_parser('build')
    p.add_argument('version', nargs='?')
    p.add_argument('--all', action='store_true')

    subs.add_parser('update')
    subs.add_parser('status')
    subs.add_parser('docs')
    subs.add_parser('apidocs')
    subs.add_parser('release')

    arguments = parser.parse_args(args=args)
    if arguments.action == 'status':
        return updater.check_for_updates()
    if arguments.action == 'update':
        return updater.update_specs()
    if arguments.action == 'release':
        return packaging.deploy_release()
    if arguments.action == 'docs':
        return documenting.build_docs()
    if arguments.action == 'apidocs':
        return documenting.update_api_docs()
    if arguments.version:
        return generate(arguments.version)
    elif arguments.all:
        return generate_all()

    raise ValueError('Specify a version or select all')
