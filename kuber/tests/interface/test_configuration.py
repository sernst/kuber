import os

import pytest

import kuber

MY_DIRECTORY = os.path.realpath(os.path.dirname(__file__))


def test_assignments():
    """Should manage internal settings as expected."""
    settings = kuber.create_bundle().settings
    settings.add(a=1, b=2)
    settings.add(b=None)
    settings.c = 'hello'
    settings['d'] = 'goodbye'

    assert settings.a == 1
    assert settings['a'] == 1
    assert settings.grab('a', 'b', 'c', 'd') == (1, None, 'hello', 'goodbye')


def test_file_error():
    """Should error out if the file is not of the correct type."""
    settings = kuber.create_bundle().settings

    with pytest.raises(IOError):
        settings.add_from_file(os.path.realpath(__file__))
