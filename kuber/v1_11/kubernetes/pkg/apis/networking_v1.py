import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class NetworkPolicy(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.networking.v1.NetworkPolicy instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicy instance."""
        super(NetworkPolicy, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicy'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'NetworkPolicy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyIngressRule(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.networking.v1.NetworkPolicyIngressRule instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyIngressRule instance."""
        super(NetworkPolicyIngressRule, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyIngressRule'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'NetworkPolicyIngressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.networking.v1.NetworkPolicyList instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyList instance."""
        super(NetworkPolicyList, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'NetworkPolicyList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyPeer(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.networking.v1.NetworkPolicyPeer instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyPeer instance."""
        super(NetworkPolicyPeer, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyPeer'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'NetworkPolicyPeer':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyPort(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.networking.v1.NetworkPolicyPort instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyPort instance."""
        super(NetworkPolicyPort, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyPort'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'NetworkPolicyPort':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicySpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.networking.v1.NetworkPolicySpec instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicySpec instance."""
        super(NetworkPolicySpec, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicySpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'NetworkPolicySpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
