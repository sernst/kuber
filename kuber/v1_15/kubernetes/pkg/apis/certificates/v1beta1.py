import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class CertificateSigningRequest(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.certificates.v1beta1.CertificateSigningRequest
    instead.
    """

    def __init__(
            self,
    ):
        """Create CertificateSigningRequest instance."""
        super(CertificateSigningRequest, self).__init__(
            api_version='certificates/v1beta1',
            kind='CertificateSigningRequest'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CertificateSigningRequest':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestCondition(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.certificates.v1beta1.Certi
    ficateSigningRequestCondition instead.
    """

    def __init__(
            self,
    ):
        """Create CertificateSigningRequestCondition instance."""
        super(CertificateSigningRequestCondition, self).__init__(
            api_version='certificates/v1beta1',
            kind='CertificateSigningRequestCondition'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CertificateSigningRequestCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestList(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.certificates.v1beta1.Certi
    ficateSigningRequestList instead.
    """

    def __init__(
            self,
    ):
        """Create CertificateSigningRequestList instance."""
        super(CertificateSigningRequestList, self).__init__(
            api_version='certificates/v1beta1',
            kind='CertificateSigningRequestList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CertificateSigningRequestList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.certificates.v1beta1.Certi
    ficateSigningRequestSpec instead.
    """

    def __init__(
            self,
    ):
        """Create CertificateSigningRequestSpec instance."""
        super(CertificateSigningRequestSpec, self).__init__(
            api_version='certificates/v1beta1',
            kind='CertificateSigningRequestSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CertificateSigningRequestSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CertificateSigningRequestStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.certificates.v1beta1.Certi
    ficateSigningRequestStatus instead.
    """

    def __init__(
            self,
    ):
        """Create CertificateSigningRequestStatus instance."""
        super(CertificateSigningRequestStatus, self).__init__(
            api_version='certificates/v1beta1',
            kind='CertificateSigningRequestStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CertificateSigningRequestStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
