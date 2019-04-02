import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class Initializer(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.admissionregistration.v1alpha1.Initializer
    instead.
    """

    def __init__(
            self,
    ):
        """Create Initializer instance."""
        super(Initializer, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='Initializer'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Initializer':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class InitializerConfiguration(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.admissionregistration.v1al
    pha1.InitializerConfiguration instead.
    """

    def __init__(
            self,
    ):
        """Create InitializerConfiguration instance."""
        super(InitializerConfiguration, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='InitializerConfiguration'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'InitializerConfiguration':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class InitializerConfigurationList(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.admissionregistration.v1al
    pha1.InitializerConfigurationList instead.
    """

    def __init__(
            self,
    ):
        """Create InitializerConfigurationList instance."""
        super(InitializerConfigurationList, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='InitializerConfigurationList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'InitializerConfigurationList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Rule(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.admissionregistration.v1alpha1.Rule instead.
    """

    def __init__(
            self,
    ):
        """Create Rule instance."""
        super(Rule, self).__init__(
            api_version='admissionregistration/v1alpha1',
            kind='Rule'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Rule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
