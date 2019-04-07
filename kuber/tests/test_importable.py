import importlib
import os

from kuber import versioning

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_importable():
    """Should be able to import every generated file."""
    root_path = os.path.dirname(MY_DIRECTORY)

    for version in versioning.get_all_versions():
        v = version.label.replace('.', '_')
        path = os.path.join(root_path, v)
        module_names = [m[:-3] for m in os.listdir(path) if m.endswith('.py')]
        for name in module_names:
            m = importlib.import_module('.'.join(['kuber', v, name]))
            assert m is not None, f'Expected kuber.{v}.{m} to be importable.'
