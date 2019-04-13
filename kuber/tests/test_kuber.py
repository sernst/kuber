from unittest.mock import MagicMock

import kuber


def test_invoke():
    """
    Should call the callback and then execute a status command action on
    the created (and empty) resource bundle.
    """
    callback = MagicMock()
    kuber.invoke(callback, arguments=['status'])
    callback.assert_called_once()
