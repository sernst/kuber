import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class Eviction(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.policy.v1beta1.Eviction
    instead.
    """

    def __init__(
            self,
    ):
        """Create Eviction instance."""
        super(Eviction, self).__init__(
            api_version='policy/v1beta1',
            kind='Eviction'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Eviction':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudget(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.policy.v1beta1.PodDisruptionBudget instead.
    """

    def __init__(
            self,
    ):
        """Create PodDisruptionBudget instance."""
        super(PodDisruptionBudget, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudget'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodDisruptionBudget':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudgetList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.policy.v1beta1.PodDisruptionBudgetList instead.
    """

    def __init__(
            self,
    ):
        """Create PodDisruptionBudgetList instance."""
        super(PodDisruptionBudgetList, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudgetList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodDisruptionBudgetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudgetSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.policy.v1beta1.PodDisruptionBudgetSpec instead.
    """

    def __init__(
            self,
    ):
        """Create PodDisruptionBudgetSpec instance."""
        super(PodDisruptionBudgetSpec, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudgetSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodDisruptionBudgetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodDisruptionBudgetStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.policy.v1beta1.PodDisruptionBudgetStatus instead.
    """

    def __init__(
            self,
    ):
        """Create PodDisruptionBudgetStatus instance."""
        super(PodDisruptionBudgetStatus, self).__init__(
            api_version='policy/v1beta1',
            kind='PodDisruptionBudgetStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodDisruptionBudgetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
