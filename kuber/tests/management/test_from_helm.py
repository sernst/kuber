import pathlib
from unittest.mock import MagicMock
from unittest.mock import patch

import kuber

directory = pathlib.Path(__file__).parent.absolute()


@patch("subprocess.run")
def test_from_helm(subprocess_run: MagicMock):
    """Should load bundle from helm template."""
    response = MagicMock(
        stdout=directory.joinpath("test-first.yaml").read_text().encode()
    )
    subprocess_run.return_value = response
    bundle = kuber.from_helm("foobar", "some/chart")
    assert (
        len(bundle.resources) == 2
    ), """
        Expect two resources to be loaded from the URL mocked by the local file.
        """
