import typing


from kuber import definitions as _kuber_definitions


class PodPreset(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.settings.v1alpha1.PodPreset instead.
    """

    def __init__(
            self,
    ):
        """Create PodPreset instance."""
        super(PodPreset, self).__init__(
            api_version='settings/v1alpha1',
            kind='PodPreset'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodPreset':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodPresetList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.settings.v1alpha1.PodPresetList instead.
    """

    def __init__(
            self,
    ):
        """Create PodPresetList instance."""
        super(PodPresetList, self).__init__(
            api_version='settings/v1alpha1',
            kind='PodPresetList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodPresetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodPresetSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.settings.v1alpha1.PodPresetSpec instead.
    """

    def __init__(
            self,
    ):
        """Create PodPresetSpec instance."""
        super(PodPresetSpec, self).__init__(
            api_version='settings/v1alpha1',
            kind='PodPresetSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodPresetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
