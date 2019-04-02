import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class ControllerRevision(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.ControllerRevision instead.
    """

    def __init__(
            self,
    ):
        """Create ControllerRevision instance."""
        super(ControllerRevision, self).__init__(
            api_version='apps/v1beta1',
            kind='ControllerRevision'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ControllerRevision':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ControllerRevisionList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.ControllerRevisionList instead.
    """

    def __init__(
            self,
    ):
        """Create ControllerRevisionList instance."""
        super(ControllerRevisionList, self).__init__(
            api_version='apps/v1beta1',
            kind='ControllerRevisionList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ControllerRevisionList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Deployment(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.apps.v1beta1.Deployment
    instead.
    """

    def __init__(
            self,
    ):
        """Create Deployment instance."""
        super(Deployment, self).__init__(
            api_version='apps/v1beta1',
            kind='Deployment'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Deployment':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentCondition(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.DeploymentCondition instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentCondition instance."""
        super(DeploymentCondition, self).__init__(
            api_version='apps/v1beta1',
            kind='DeploymentCondition'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DeploymentCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.DeploymentList instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentList instance."""
        super(DeploymentList, self).__init__(
            api_version='apps/v1beta1',
            kind='DeploymentList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DeploymentList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentRollback(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.DeploymentRollback instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentRollback instance."""
        super(DeploymentRollback, self).__init__(
            api_version='apps/v1beta1',
            kind='DeploymentRollback'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DeploymentRollback':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.DeploymentSpec instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentSpec instance."""
        super(DeploymentSpec, self).__init__(
            api_version='apps/v1beta1',
            kind='DeploymentSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DeploymentSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.DeploymentStatus instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentStatus instance."""
        super(DeploymentStatus, self).__init__(
            api_version='apps/v1beta1',
            kind='DeploymentStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DeploymentStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeploymentStrategy(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.DeploymentStrategy instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentStrategy instance."""
        super(DeploymentStrategy, self).__init__(
            api_version='apps/v1beta1',
            kind='DeploymentStrategy'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DeploymentStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollbackConfig(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.RollbackConfig instead.
    """

    def __init__(
            self,
    ):
        """Create RollbackConfig instance."""
        super(RollbackConfig, self).__init__(
            api_version='apps/v1beta1',
            kind='RollbackConfig'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RollbackConfig':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollingUpdateDeployment(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.RollingUpdateDeployment instead.
    """

    def __init__(
            self,
    ):
        """Create RollingUpdateDeployment instance."""
        super(RollingUpdateDeployment, self).__init__(
            api_version='apps/v1beta1',
            kind='RollingUpdateDeployment'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RollingUpdateDeployment':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollingUpdateStatefulSetStrategy(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.RollingUpdateStatefulSetStrategy
    instead.
    """

    def __init__(
            self,
    ):
        """Create RollingUpdateStatefulSetStrategy instance."""
        super(RollingUpdateStatefulSetStrategy, self).__init__(
            api_version='apps/v1beta1',
            kind='RollingUpdateStatefulSetStrategy'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RollingUpdateStatefulSetStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Scale(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.apps.v1beta1.Scale
    instead.
    """

    def __init__(
            self,
    ):
        """Create Scale instance."""
        super(Scale, self).__init__(
            api_version='apps/v1beta1',
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
    Deprecated. Please use io.k8s.api.apps.v1beta1.ScaleSpec
    instead.
    """

    def __init__(
            self,
    ):
        """Create ScaleSpec instance."""
        super(ScaleSpec, self).__init__(
            api_version='apps/v1beta1',
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
    Deprecated. Please use io.k8s.api.apps.v1beta1.ScaleStatus
    instead.
    """

    def __init__(
            self,
    ):
        """Create ScaleStatus instance."""
        super(ScaleStatus, self).__init__(
            api_version='apps/v1beta1',
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


class StatefulSet(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.apps.v1beta1.StatefulSet
    instead.
    """

    def __init__(
            self,
    ):
        """Create StatefulSet instance."""
        super(StatefulSet, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSet'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'StatefulSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.StatefulSetList instead.
    """

    def __init__(
            self,
    ):
        """Create StatefulSetList instance."""
        super(StatefulSetList, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'StatefulSetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.StatefulSetSpec instead.
    """

    def __init__(
            self,
    ):
        """Create StatefulSetSpec instance."""
        super(StatefulSetSpec, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'StatefulSetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.StatefulSetStatus instead.
    """

    def __init__(
            self,
    ):
        """Create StatefulSetStatus instance."""
        super(StatefulSetStatus, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'StatefulSetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StatefulSetUpdateStrategy(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.apps.v1beta1.StatefulSetUpdateStrategy instead.
    """

    def __init__(
            self,
    ):
        """Create StatefulSetUpdateStrategy instance."""
        super(StatefulSetUpdateStrategy, self).__init__(
            api_version='apps/v1beta1',
            kind='StatefulSetUpdateStrategy'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'StatefulSetUpdateStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
