import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class DaemonSet(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.DaemonSet instead.
    """

    def __init__(
            self,
    ):
        """Create DaemonSet instance."""
        super(DaemonSet, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSet'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DaemonSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.DaemonSetList instead.
    """

    def __init__(
            self,
    ):
        """Create DaemonSetList instance."""
        super(DaemonSetList, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DaemonSetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.DaemonSetSpec instead.
    """

    def __init__(
            self,
    ):
        """Create DaemonSetSpec instance."""
        super(DaemonSetSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DaemonSetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.DaemonSetStatus instead.
    """

    def __init__(
            self,
    ):
        """Create DaemonSetStatus instance."""
        super(DaemonSetStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DaemonSetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DaemonSetUpdateStrategy(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.DaemonSetUpdateStrategy
    instead.
    """

    def __init__(
            self,
    ):
        """Create DaemonSetUpdateStrategy instance."""
        super(DaemonSetUpdateStrategy, self).__init__(
            api_version='extensions/v1beta1',
            kind='DaemonSetUpdateStrategy'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'DaemonSetUpdateStrategy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Deployment(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.Deployment instead.
    """

    def __init__(
            self,
    ):
        """Create Deployment instance."""
        super(Deployment, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.DeploymentCondition instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentCondition instance."""
        super(DeploymentCondition, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.DeploymentList instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentList instance."""
        super(DeploymentList, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.DeploymentRollback instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentRollback instance."""
        super(DeploymentRollback, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.DeploymentSpec instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentSpec instance."""
        super(DeploymentSpec, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.DeploymentStatus instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentStatus instance."""
        super(DeploymentStatus, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.DeploymentStrategy instead.
    """

    def __init__(
            self,
    ):
        """Create DeploymentStrategy instance."""
        super(DeploymentStrategy, self).__init__(
            api_version='extensions/v1beta1',
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


class FSGroupStrategyOptions(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.FSGroupStrategyOptions
    instead.
    """

    def __init__(
            self,
    ):
        """Create FSGroupStrategyOptions instance."""
        super(FSGroupStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
            kind='FSGroupStrategyOptions'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'FSGroupStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HTTPIngressPath(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.HTTPIngressPath instead.
    """

    def __init__(
            self,
    ):
        """Create HTTPIngressPath instance."""
        super(HTTPIngressPath, self).__init__(
            api_version='extensions/v1beta1',
            kind='HTTPIngressPath'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'HTTPIngressPath':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HTTPIngressRuleValue(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.HTTPIngressRuleValue instead.
    """

    def __init__(
            self,
    ):
        """Create HTTPIngressRuleValue instance."""
        super(HTTPIngressRuleValue, self).__init__(
            api_version='extensions/v1beta1',
            kind='HTTPIngressRuleValue'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'HTTPIngressRuleValue':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HostPortRange(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.HostPortRange instead.
    """

    def __init__(
            self,
    ):
        """Create HostPortRange instance."""
        super(HostPortRange, self).__init__(
            api_version='extensions/v1beta1',
            kind='HostPortRange'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'HostPortRange':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IDRange(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.extensions.v1beta1.IDRange
    instead.
    """

    def __init__(
            self,
    ):
        """Create IDRange instance."""
        super(IDRange, self).__init__(
            api_version='extensions/v1beta1',
            kind='IDRange'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IDRange':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Ingress(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.extensions.v1beta1.Ingress
    instead.
    """

    def __init__(
            self,
    ):
        """Create Ingress instance."""
        super(Ingress, self).__init__(
            api_version='extensions/v1beta1',
            kind='Ingress'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Ingress':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressBackend(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.IngressBackend instead.
    """

    def __init__(
            self,
    ):
        """Create IngressBackend instance."""
        super(IngressBackend, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressBackend'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IngressBackend':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.IngressList instead.
    """

    def __init__(
            self,
    ):
        """Create IngressList instance."""
        super(IngressList, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IngressList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressRule(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.IngressRule instead.
    """

    def __init__(
            self,
    ):
        """Create IngressRule instance."""
        super(IngressRule, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressRule'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IngressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.IngressSpec instead.
    """

    def __init__(
            self,
    ):
        """Create IngressSpec instance."""
        super(IngressSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IngressSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.IngressStatus instead.
    """

    def __init__(
            self,
    ):
        """Create IngressStatus instance."""
        super(IngressStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IngressStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressTLS(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.IngressTLS instead.
    """

    def __init__(
            self,
    ):
        """Create IngressTLS instance."""
        super(IngressTLS, self).__init__(
            api_version='extensions/v1beta1',
            kind='IngressTLS'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'IngressTLS':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicy(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.NetworkPolicy instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicy instance."""
        super(NetworkPolicy, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.NetworkPolicyIngressRule
    instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyIngressRule instance."""
        super(NetworkPolicyIngressRule, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.NetworkPolicyList instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyList instance."""
        super(NetworkPolicyList, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.NetworkPolicyPeer instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyPeer instance."""
        super(NetworkPolicyPeer, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.NetworkPolicyPort instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicyPort instance."""
        super(NetworkPolicyPort, self).__init__(
            api_version='extensions/v1beta1',
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
    io.k8s.api.extensions.v1beta1.NetworkPolicySpec instead.
    """

    def __init__(
            self,
    ):
        """Create NetworkPolicySpec instance."""
        super(NetworkPolicySpec, self).__init__(
            api_version='extensions/v1beta1',
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


class PodSecurityPolicy(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.PodSecurityPolicy instead.
    """

    def __init__(
            self,
    ):
        """Create PodSecurityPolicy instance."""
        super(PodSecurityPolicy, self).__init__(
            api_version='extensions/v1beta1',
            kind='PodSecurityPolicy'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodSecurityPolicy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicyList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.PodSecurityPolicyList instead.
    """

    def __init__(
            self,
    ):
        """Create PodSecurityPolicyList instance."""
        super(PodSecurityPolicyList, self).__init__(
            api_version='extensions/v1beta1',
            kind='PodSecurityPolicyList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodSecurityPolicyList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSecurityPolicySpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.PodSecurityPolicySpec instead.
    """

    def __init__(
            self,
    ):
        """Create PodSecurityPolicySpec instance."""
        super(PodSecurityPolicySpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='PodSecurityPolicySpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PodSecurityPolicySpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSet(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.ReplicaSet instead.
    """

    def __init__(
            self,
    ):
        """Create ReplicaSet instance."""
        super(ReplicaSet, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSet'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ReplicaSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetCondition(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.ReplicaSetCondition instead.
    """

    def __init__(
            self,
    ):
        """Create ReplicaSetCondition instance."""
        super(ReplicaSetCondition, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetCondition'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ReplicaSetCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.ReplicaSetList instead.
    """

    def __init__(
            self,
    ):
        """Create ReplicaSetList instance."""
        super(ReplicaSetList, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ReplicaSetList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.ReplicaSetSpec instead.
    """

    def __init__(
            self,
    ):
        """Create ReplicaSetSpec instance."""
        super(ReplicaSetSpec, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ReplicaSetSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ReplicaSetStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.ReplicaSetStatus instead.
    """

    def __init__(
            self,
    ):
        """Create ReplicaSetStatus instance."""
        super(ReplicaSetStatus, self).__init__(
            api_version='extensions/v1beta1',
            kind='ReplicaSetStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ReplicaSetStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollbackConfig(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.RollbackConfig instead.
    """

    def __init__(
            self,
    ):
        """Create RollbackConfig instance."""
        super(RollbackConfig, self).__init__(
            api_version='extensions/v1beta1',
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


class RollingUpdateDaemonSet(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.RollingUpdateDaemonSet
    instead.
    """

    def __init__(
            self,
    ):
        """Create RollingUpdateDaemonSet instance."""
        super(RollingUpdateDaemonSet, self).__init__(
            api_version='extensions/v1beta1',
            kind='RollingUpdateDaemonSet'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RollingUpdateDaemonSet':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RollingUpdateDeployment(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.RollingUpdateDeployment
    instead.
    """

    def __init__(
            self,
    ):
        """Create RollingUpdateDeployment instance."""
        super(RollingUpdateDeployment, self).__init__(
            api_version='extensions/v1beta1',
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


class RunAsUserStrategyOptions(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.RunAsUserStrategyOptions
    instead.
    """

    def __init__(
            self,
    ):
        """Create RunAsUserStrategyOptions instance."""
        super(RunAsUserStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
            kind='RunAsUserStrategyOptions'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RunAsUserStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SELinuxStrategyOptions(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.SELinuxStrategyOptions
    instead.
    """

    def __init__(
            self,
    ):
        """Create SELinuxStrategyOptions instance."""
        super(SELinuxStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
            kind='SELinuxStrategyOptions'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'SELinuxStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Scale(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.extensions.v1beta1.Scale
    instead.
    """

    def __init__(
            self,
    ):
        """Create Scale instance."""
        super(Scale, self).__init__(
            api_version='extensions/v1beta1',
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
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.ScaleSpec instead.
    """

    def __init__(
            self,
    ):
        """Create ScaleSpec instance."""
        super(ScaleSpec, self).__init__(
            api_version='extensions/v1beta1',
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
    Deprecated. Please use
    io.k8s.api.extensions.v1beta1.ScaleStatus instead.
    """

    def __init__(
            self,
    ):
        """Create ScaleStatus instance."""
        super(ScaleStatus, self).__init__(
            api_version='extensions/v1beta1',
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


class SupplementalGroupsStrategyOptions(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.extensions.v1beta1.Supplem
    entalGroupsStrategyOptions instead.
    """

    def __init__(
            self,
    ):
        """Create SupplementalGroupsStrategyOptions instance."""
        super(SupplementalGroupsStrategyOptions, self).__init__(
            api_version='extensions/v1beta1',
            kind='SupplementalGroupsStrategyOptions'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'SupplementalGroupsStrategyOptions':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
