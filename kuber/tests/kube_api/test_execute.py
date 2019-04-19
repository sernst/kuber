from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from kuber import kube_api
from kuber.latest import core_v1


def test_execute():
    """"Should execute the specified action on the service without error."""
    service = core_v1.Service()
    service.metadata.name = 'foo'

    api = MagicMock()
    code = MagicMock()
    code.co_varnames = ('bob', 'foo', 'namespace')
    api.create_namespaced_service.__code__ = code
    with patch.object(service, 'get_resource_api') as get_api:
        get_api.return_value = api
        service.create_resource(namespace='foo')

    api.create_namespaced_service.assert_called_once()


def test_execute_no_name():
    """"Should raise error when no api client function name exists."""
    resource = MagicMock()
    resource.get_resource_api.return_value = None

    with pytest.raises(ValueError):
        kube_api.execute(
            action='foo',
            resource=resource,
            names=['spam', 'ham']
        )
