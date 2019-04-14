from unittest.mock import MagicMock
from unittest.mock import patch

import kuber
from kuber import kube_api
from kuber.tests import utils as test_utils


@patch('kubernetes.config.load_incluster_config')
@patch('kubernetes.config.load_kube_config')
def test_load_access_config(
        load_kube_config: MagicMock,
        load_incluster_config: MagicMock
):
    """Should load cluster configs."""
    kube_api.load_access_config()
    load_kube_config.assert_called_once()
    load_incluster_config.assert_not_called()


@patch('kubernetes.config.load_incluster_config')
@patch('kubernetes.config.load_kube_config')
def test_load_access_config_in_cluster(
        load_kube_config: MagicMock,
        load_incluster_config: MagicMock
):
    """Should load in-cluster configs."""
    kube_api.load_access_config(in_cluster=True)
    load_kube_config.assert_not_called()
    load_incluster_config.assert_called_once()


@patch('kubernetes.client.VersionApi.get_code')
def test_get_version_from_cluster(get_code: MagicMock):
    """Should return the expected "latest" version."""
    latest = kuber.latest_kube_version
    cluster_version = MagicMock()
    cluster_version.major = latest.major
    cluster_version.minor = latest.minor
    get_code.return_value = cluster_version
    result = kube_api.get_version_from_cluster()
    assert result.version == latest.version


@patch('kubernetes.client.VersionApi.get_code')
def test_get_version_from_cluster_error(get_code: MagicMock):
    """Should return the expected "latest" version as the fallback on error."""
    latest = kuber.latest_kube_version
    get_code.side_effect = test_utils.MockApiException(False)
    result = kube_api.get_version_from_cluster(latest)
    assert result.version == latest.version


@patch('kubernetes.client.VersionApi.get_code')
def test_get_version_from_cluster_error_label(get_code: MagicMock):
    """Should return the expected "latest" version as the fallback on error."""
    latest = kuber.latest_kube_version
    get_code.side_effect = test_utils.MockApiException(False)
    result = kube_api.get_version_from_cluster(latest.label)
    assert result.version == latest.version


@patch('kubernetes.client.VersionApi.get_code')
def test_get_version_from_cluster_error_no_fallback(get_code: MagicMock):
    """Should return the expected "latest" version as the fallback on error."""
    get_code.side_effect = test_utils.MockApiException(False)
    result = kube_api.get_version_from_cluster()
    assert isinstance(result, kuber.KubernetesVersion)
