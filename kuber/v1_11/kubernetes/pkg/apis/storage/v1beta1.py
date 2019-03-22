import typing


from kuber import definitions as _kuber_definitions


class StorageClass(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.storage.v1beta1.StorageClass instead.
    """

    def __init__(
            self,
    ):
        """Create StorageClass instance."""
        super(StorageClass, self).__init__(
            api_version='storage/v1beta1',
            kind='StorageClass'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'StorageClass':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StorageClassList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.storage.v1beta1.StorageClassList instead.
    """

    def __init__(
            self,
    ):
        """Create StorageClassList instance."""
        super(StorageClassList, self).__init__(
            api_version='storage/v1beta1',
            kind='StorageClassList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'StorageClassList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
