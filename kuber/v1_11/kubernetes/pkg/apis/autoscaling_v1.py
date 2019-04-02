import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class CrossVersionObjectReference(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.autoscaling.v1.CrossVersionObjectReference
    instead.
    """

    def __init__(
            self,
    ):
        """Create CrossVersionObjectReference instance."""
        super(CrossVersionObjectReference, self).__init__(
            api_version='autoscaling/v1',
            kind='CrossVersionObjectReference'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CrossVersionObjectReference':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscaler(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.autoscaling.v1.HorizontalPodAutoscaler instead.
    """

    def __init__(
            self,
    ):
        """Create HorizontalPodAutoscaler instance."""
        super(HorizontalPodAutoscaler, self).__init__(
            api_version='autoscaling/v1',
            kind='HorizontalPodAutoscaler'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'HorizontalPodAutoscaler':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.autoscaling.v1.HorizontalPodAutoscalerList
    instead.
    """

    def __init__(
            self,
    ):
        """Create HorizontalPodAutoscalerList instance."""
        super(HorizontalPodAutoscalerList, self).__init__(
            api_version='autoscaling/v1',
            kind='HorizontalPodAutoscalerList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'HorizontalPodAutoscalerList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.autoscaling.v1.HorizontalPodAutoscalerSpec
    instead.
    """

    def __init__(
            self,
    ):
        """Create HorizontalPodAutoscalerSpec instance."""
        super(HorizontalPodAutoscalerSpec, self).__init__(
            api_version='autoscaling/v1',
            kind='HorizontalPodAutoscalerSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'HorizontalPodAutoscalerSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HorizontalPodAutoscalerStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.autoscaling.v1.HorizontalPodAutoscalerStatus
    instead.
    """

    def __init__(
            self,
    ):
        """Create HorizontalPodAutoscalerStatus instance."""
        super(HorizontalPodAutoscalerStatus, self).__init__(
            api_version='autoscaling/v1',
            kind='HorizontalPodAutoscalerStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'HorizontalPodAutoscalerStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Scale(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.autoscaling.v1.Scale
    instead.
    """

    def __init__(
            self,
    ):
        """Create Scale instance."""
        super(Scale, self).__init__(
            api_version='autoscaling/v1',
            kind='Scale'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Scale':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.autoscaling.v1.ScaleSpec
    instead.
    """

    def __init__(
            self,
    ):
        """Create ScaleSpec instance."""
        super(ScaleSpec, self).__init__(
            api_version='autoscaling/v1',
            kind='ScaleSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ScaleSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScaleStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.autoscaling.v1.ScaleStatus
    instead.
    """

    def __init__(
            self,
    ):
        """Create ScaleStatus instance."""
        super(ScaleStatus, self).__init__(
            api_version='autoscaling/v1',
            kind='ScaleStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ScaleStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
