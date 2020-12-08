import pathlib
from unittest.mock import MagicMock
from unittest.mock import patch

import kuber

directory = pathlib.Path(__file__).parent.absolute()


@patch("requests.get")
def test_from_url(requests_get: MagicMock):
    """Should load bundle from URL."""
    response = MagicMock(text=directory.joinpath("test-first.yaml").read_text())
    requests_get.return_value = response
    bundle = kuber.from_url("https://foo.bar/something.yaml", "latest", "test")
    assert (
        len(bundle.resources) == 2
    ), """
        Expect two resources to be loaded from the URL mocked by the local file.
        """
