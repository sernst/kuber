import os
import argparse

import kuber_maker
from kuber_maker import initializer
from kuber_maker import parsing
from kuber_maker import render


def generate(version: str):
    """..."""
    spec = kuber_maker.load_spec(version)
    initializer.empty(version)
    initializer.create_subpackages(version, spec['definitions'])
    entities = parsing.parse_definitions(version, spec['definitions'])

    for package in entities.packages.keys():
        contents = render.render_package(package, entities)
        path = kuber_maker.directory_of_package(package)

        with open(f'{path}.py', 'w') as f:
            f.write(contents)
        print(f'[CREATED]: {path}.py')


def generate_all():
    """..."""
    directory = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..', 'specs'
    ))
    for filename in os.listdir(directory):
        version = filename[1:-5]
        print(f'\n\n=== {version} ===')
        generate(version)


def main():
    """..."""
    parser = argparse.ArgumentParser(prog='kuber_maker')
    parser.add_argument('version', nargs='?')
    parser.add_argument('--all', action='store_true')
    arguments = parser.parse_args()
    if arguments.version:
        return generate(arguments.version)
    elif arguments.all:
        return generate_all()

    raise ValueError('Specify a version or select all')

