from unittest.mock import MagicMock

import kuber


def test_cli_invocation():
    """
    Should call the callback and then execute a status command action on
    the created (and empty) resource bundle.
    """
    callback = MagicMock()
    kuber.cli(callback, arguments=['status'])
    callback.assert_called_once()


def test_latest_version_stable():
    """Should have a stable latest version."""
    assert not kuber.latest_kube_version.pre_release
    assert 'alpha' not in str(kuber.latest_kube_version)
    assert 'beta' not in str(kuber.latest_kube_version)
