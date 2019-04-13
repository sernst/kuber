import json

from kubernetes.client.rest import ApiException as _ApiException


class MockApiException(_ApiException):
    """Mock ApiException class for use in testing."""

    def __init__(
            self,
            successful: bool = True,
            reason: str = 'Testing',
            body: dict = None
    ):
        super(MockApiException, self).__init__(
            reason=reason,
            status=200 if successful else 442
        )
        self.body = json.dumps({**{'reason': reason}, **(body or {})})
