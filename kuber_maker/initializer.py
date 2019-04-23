import shutil
import os
import kuber_maker


def empty(version: str):
    """..."""
    path = kuber_maker.get_path(version)
    if os.path.exists(path):
        shutil.rmtree(path)


def create_subpackages(version: str, definitions: dict):
    paths = []
    for api_path in definitions.keys():
        module_path = kuber_maker.to_kuber_path(version, api_path)
        path = os.path.dirname(module_path)

        if os.path.basename(path) in ('kubernetes', 'apimachinery'):
            # These sub-packages are empty because the resources
            # here have been moved and the only items remaining are
            # the type definitions that will be skipped Time, Quantity,
            # and IntOrString.
            continue

        paths.append(path)

        if not os.path.exists(path):
            os.makedirs(path)
        _populate_package_inits(path)

    return paths


def _populate_package_inits(path: str):
    """..."""
    init_path = os.path.join(path, '__init__.py')
    while not os.path.exists(init_path):
        with open(init_path, 'w') as f:
            f.write('')
        init_path = os.path.join(
            os.path.dirname(os.path.dirname(init_path)),
            '__init__.py'
        )
