import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_13.meta_v1 import LabelSelector
from kuber.v1_13.meta_v1 import ListMeta
from kuber.v1_13.meta_v1 import ObjectMeta


class IPBlock(_kuber_definitions.Definition):
    """
    IPBlock describes a particular CIDR (Ex. "192.168.1.1/24")
    that is allowed to the pods matched by a NetworkPolicySpec's
    podSelector. The except entry describes CIDRs that should
    not be included within this rule.
    """

    def __init__(
            self,
            cidr: str = None,
            except_: typing.List[str] = None,
    ):
        """Create IPBlock instance."""
        super(IPBlock, self).__init__(
            api_version='networking/v1',
            kind='IPBlock'
        )
        self._properties = {
            'cidr': cidr or '',
            'except': except_ or [],

        }
        self._types = {
            'cidr': (str, None),
            'except': (list, str),

        }

    @property
    def cidr(self) -> str:
        """
        CIDR is a string representing the IP Block Valid examples
        are "192.168.1.1/24"
        """
        return self._properties.get('cidr')

    @cidr.setter
    def cidr(self, value: str):
        """
        CIDR is a string representing the IP Block Valid examples
        are "192.168.1.1/24"
        """
        self._properties['cidr'] = value

    @property
    def except_(self) -> typing.List[str]:
        """
        Except is a slice of CIDRs that should not be included
        within an IP Block Valid examples are "192.168.1.1/24"
        Except values will be rejected if they are outside the CIDR
        range
        """
        return self._properties.get('except')

    @except_.setter
    def except_(self, value: typing.List[str]):
        """
        Except is a slice of CIDRs that should not be included
        within an IP Block Valid examples are "192.168.1.1/24"
        Except values will be rejected if they are outside the CIDR
        range
        """
        self._properties['except'] = value

    def __enter__(self) -> 'IPBlock':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicy(_kuber_definitions.Resource):
    """
    NetworkPolicy describes what network traffic is allowed for
    a set of Pods
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'NetworkPolicySpec' = None,
    ):
        """Create NetworkPolicy instance."""
        super(NetworkPolicy, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicy'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or NetworkPolicySpec(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (NetworkPolicySpec, None),

        }

    @property
    def metadata(self) -> 'ObjectMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ObjectMeta', dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ObjectMeta().from_dict(value)
        self._properties['metadata'] = value

    @property
    def spec(self) -> 'NetworkPolicySpec':
        """
        Specification of the desired behavior for this
        NetworkPolicy.
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['NetworkPolicySpec', dict]):
        """
        Specification of the desired behavior for this
        NetworkPolicy.
        """
        if isinstance(value, dict):
            value = NetworkPolicySpec().from_dict(value)
        self._properties['spec'] = value

    def create_resource(self, namespace: 'str' = None):
        """
        Creates the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'create_namespaced_network_policy',
            'create_network_policy'
        ]

        _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )

    def replace_resource(self, namespace: 'str' = None):
        """
        Replaces the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'replace_namespaced_network_policy',
            'replace_network_policy'
        ]

        _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def patch_resource(self, namespace: 'str' = None):
        """
        Patches the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = [
            'patch_namespaced_network_policy',
            'patch_network_policy'
        ]

        _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )

    def get_resource_status(self, namespace: 'str' = None):
        """This resource does not have a status."""
        pass

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the NetworkPolicy from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_network_policy',
            'read_network_policy'
        ]
        return _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )

    def delete_resource(
            self,
            namespace: str = None,
            propagation_policy: str = 'Foreground',
            grace_period_seconds: int = 10
    ):
        """
        Deletes the NetworkPolicy from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_network_policy',
            'delete_network_policy'
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds
        )

        _kube_api.execute(
            action='delete',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name, 'body': body}
        )

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.NetworkingV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> 'NetworkPolicy':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyEgressRule(_kuber_definitions.Definition):
    """
    NetworkPolicyEgressRule describes a particular set of
    traffic that is allowed out of pods matched by a
    NetworkPolicySpec's podSelector. The traffic must match both
    ports and to. This type is beta-level in 1.8
    """

    def __init__(
            self,
            ports: typing.List['NetworkPolicyPort'] = None,
            to: typing.List['NetworkPolicyPeer'] = None,
    ):
        """Create NetworkPolicyEgressRule instance."""
        super(NetworkPolicyEgressRule, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyEgressRule'
        )
        self._properties = {
            'ports': ports or [],
            'to': to or [],

        }
        self._types = {
            'ports': (list, NetworkPolicyPort),
            'to': (list, NetworkPolicyPeer),

        }

    @property
    def ports(self) -> typing.List['NetworkPolicyPort']:
        """
        List of destination ports for outgoing traffic. Each item in
        this list is combined using a logical OR. If this field is
        empty or missing, this rule matches all ports (traffic not
        restricted by port). If this field is present and contains
        at least one item, then this rule allows traffic only if the
        traffic matches at least one port in the list.
        """
        return self._properties.get('ports')

    @ports.setter
    def ports(
            self,
            value: typing.Union[typing.List['NetworkPolicyPort'], typing.List[dict]]
    ):
        """
        List of destination ports for outgoing traffic. Each item in
        this list is combined using a logical OR. If this field is
        empty or missing, this rule matches all ports (traffic not
        restricted by port). If this field is present and contains
        at least one item, then this rule allows traffic only if the
        traffic matches at least one port in the list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPort().from_dict(item)
            cleaned.append(item)
        self._properties['ports'] = cleaned

    @property
    def to(self) -> typing.List['NetworkPolicyPeer']:
        """
        List of destinations for outgoing traffic of pods selected
        for this rule. Items in this list are combined using a
        logical OR operation. If this field is empty or missing,
        this rule matches all destinations (traffic not restricted
        by destination). If this field is present and contains at
        least one item, this rule allows traffic only if the traffic
        matches at least one item in the to list.
        """
        return self._properties.get('to')

    @to.setter
    def to(
            self,
            value: typing.Union[typing.List['NetworkPolicyPeer'], typing.List[dict]]
    ):
        """
        List of destinations for outgoing traffic of pods selected
        for this rule. Items in this list are combined using a
        logical OR operation. If this field is empty or missing,
        this rule matches all destinations (traffic not restricted
        by destination). If this field is present and contains at
        least one item, this rule allows traffic only if the traffic
        matches at least one item in the to list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPeer().from_dict(item)
            cleaned.append(item)
        self._properties['to'] = cleaned

    def __enter__(self) -> 'NetworkPolicyEgressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyIngressRule(_kuber_definitions.Definition):
    """
    NetworkPolicyIngressRule describes a particular set of
    traffic that is allowed to the pods matched by a
    NetworkPolicySpec's podSelector. The traffic must match both
    ports and from.
    """

    def __init__(
            self,
            from_: typing.List['NetworkPolicyPeer'] = None,
            ports: typing.List['NetworkPolicyPort'] = None,
    ):
        """Create NetworkPolicyIngressRule instance."""
        super(NetworkPolicyIngressRule, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyIngressRule'
        )
        self._properties = {
            'from': from_ or [],
            'ports': ports or [],

        }
        self._types = {
            'from': (list, NetworkPolicyPeer),
            'ports': (list, NetworkPolicyPort),

        }

    @property
    def from_(self) -> typing.List['NetworkPolicyPeer']:
        """
        List of sources which should be able to access the pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all sources (traffic not
        restricted by source). If this field is present and contains
        at least on item, this rule allows traffic only if the
        traffic matches at least one item in the from list.
        """
        return self._properties.get('from')

    @from_.setter
    def from_(
            self,
            value: typing.Union[typing.List['NetworkPolicyPeer'], typing.List[dict]]
    ):
        """
        List of sources which should be able to access the pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all sources (traffic not
        restricted by source). If this field is present and contains
        at least on item, this rule allows traffic only if the
        traffic matches at least one item in the from list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPeer().from_dict(item)
            cleaned.append(item)
        self._properties['from'] = cleaned

    @property
    def ports(self) -> typing.List['NetworkPolicyPort']:
        """
        List of ports which should be made accessible on the pods
        selected for this rule. Each item in this list is combined
        using a logical OR. If this field is empty or missing, this
        rule matches all ports (traffic not restricted by port). If
        this field is present and contains at least one item, then
        this rule allows traffic only if the traffic matches at
        least one port in the list.
        """
        return self._properties.get('ports')

    @ports.setter
    def ports(
            self,
            value: typing.Union[typing.List['NetworkPolicyPort'], typing.List[dict]]
    ):
        """
        List of ports which should be made accessible on the pods
        selected for this rule. Each item in this list is combined
        using a logical OR. If this field is empty or missing, this
        rule matches all ports (traffic not restricted by port). If
        this field is present and contains at least one item, then
        this rule allows traffic only if the traffic matches at
        least one port in the list.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyPort().from_dict(item)
            cleaned.append(item)
        self._properties['ports'] = cleaned

    def __enter__(self) -> 'NetworkPolicyIngressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyList(_kuber_definitions.Collection):
    """
    NetworkPolicyList is a list of NetworkPolicy objects.
    """

    def __init__(
            self,
            items: typing.List['NetworkPolicy'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create NetworkPolicyList instance."""
        super(NetworkPolicyList, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, NetworkPolicy),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['NetworkPolicy']:
        """
        Items is a list of schema objects.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['NetworkPolicy'], typing.List[dict]]
    ):
        """
        Items is a list of schema objects.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicy().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        if isinstance(value, dict):
            value = ListMeta().from_dict(value)
        self._properties['metadata'] = value

    @staticmethod
    def get_resource_api(
            api_client: client.ApiClient = None,
            **kwargs
    ) -> 'client.NetworkingV1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> 'NetworkPolicyList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyPeer(_kuber_definitions.Definition):
    """
    NetworkPolicyPeer describes a peer to allow traffic from.
    Only certain combinations of fields are allowed
    """

    def __init__(
            self,
            ip_block: 'IPBlock' = None,
            namespace_selector: 'LabelSelector' = None,
            pod_selector: 'LabelSelector' = None,
    ):
        """Create NetworkPolicyPeer instance."""
        super(NetworkPolicyPeer, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyPeer'
        )
        self._properties = {
            'ipBlock': ip_block or IPBlock(),
            'namespaceSelector': namespace_selector or LabelSelector(),
            'podSelector': pod_selector or LabelSelector(),

        }
        self._types = {
            'ipBlock': (IPBlock, None),
            'namespaceSelector': (LabelSelector, None),
            'podSelector': (LabelSelector, None),

        }

    @property
    def ip_block(self) -> 'IPBlock':
        """
        IPBlock defines policy on a particular IPBlock. If this
        field is set then neither of the other fields can be.
        """
        return self._properties.get('ipBlock')

    @ip_block.setter
    def ip_block(self, value: typing.Union['IPBlock', dict]):
        """
        IPBlock defines policy on a particular IPBlock. If this
        field is set then neither of the other fields can be.
        """
        if isinstance(value, dict):
            value = IPBlock().from_dict(value)
        self._properties['ipBlock'] = value

    @property
    def namespace_selector(self) -> 'LabelSelector':
        """
        Selects Namespaces using cluster-scoped labels. This field
        follows standard label selector semantics; if present but
        empty, it selects all namespaces.

        If PodSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects all Pods in the
        Namespaces selected by NamespaceSelector.
        """
        return self._properties.get('namespaceSelector')

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Selects Namespaces using cluster-scoped labels. This field
        follows standard label selector semantics; if present but
        empty, it selects all namespaces.

        If PodSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects all Pods in the
        Namespaces selected by NamespaceSelector.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['namespaceSelector'] = value

    @property
    def pod_selector(self) -> 'LabelSelector':
        """
        This is a label selector which selects Pods. This field
        follows standard label selector semantics; if present but
        empty, it selects all pods.

        If NamespaceSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects the Pods matching
        PodSelector in the policy's own Namespace.
        """
        return self._properties.get('podSelector')

    @pod_selector.setter
    def pod_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        This is a label selector which selects Pods. This field
        follows standard label selector semantics; if present but
        empty, it selects all pods.

        If NamespaceSelector is also
        set, then the NetworkPolicyPeer as a whole selects the Pods
        matching PodSelector in the Namespaces selected by
        NamespaceSelector. Otherwise it selects the Pods matching
        PodSelector in the policy's own Namespace.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['podSelector'] = value

    def __enter__(self) -> 'NetworkPolicyPeer':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyPort(_kuber_definitions.Definition):
    """
    NetworkPolicyPort describes a port to allow traffic on
    """

    def __init__(
            self,
            port: typing.Union[str, int, None] = None,
            protocol: str = None,
    ):
        """Create NetworkPolicyPort instance."""
        super(NetworkPolicyPort, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicyPort'
        )
        self._properties = {
            'port': port or None,
            'protocol': protocol or '',

        }
        self._types = {
            'port': (int, None),
            'protocol': (str, None),

        }

    @property
    def port(self) -> typing.Optional[int]:
        """
        The port on the given protocol. This can either be a
        numerical or named port on a pod. If this field is not
        provided, this matches all port names and numbers.
        """
        value = self._properties.get('port')
        return int(value) if value is not None else None

    @port.setter
    def port(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        The port on the given protocol. This can either be a
        numerical or named port on a pod. If this field is not
        provided, this matches all port names and numbers.
        """
        self._properties['port'] = None if value is None else f'{value}'

    @property
    def protocol(self) -> str:
        """
        The protocol (TCP, UDP, or SCTP) which traffic must match.
        If not specified, this field defaults to TCP.
        """
        return self._properties.get('protocol')

    @protocol.setter
    def protocol(self, value: str):
        """
        The protocol (TCP, UDP, or SCTP) which traffic must match.
        If not specified, this field defaults to TCP.
        """
        self._properties['protocol'] = value

    def __enter__(self) -> 'NetworkPolicyPort':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicySpec(_kuber_definitions.Definition):
    """
    NetworkPolicySpec provides the specification of a
    NetworkPolicy
    """

    def __init__(
            self,
            egress: typing.List['NetworkPolicyEgressRule'] = None,
            ingress: typing.List['NetworkPolicyIngressRule'] = None,
            pod_selector: 'LabelSelector' = None,
            policy_types: typing.List[str] = None,
    ):
        """Create NetworkPolicySpec instance."""
        super(NetworkPolicySpec, self).__init__(
            api_version='networking/v1',
            kind='NetworkPolicySpec'
        )
        self._properties = {
            'egress': egress or [],
            'ingress': ingress or [],
            'podSelector': pod_selector or LabelSelector(),
            'policyTypes': policy_types or [],

        }
        self._types = {
            'egress': (list, NetworkPolicyEgressRule),
            'ingress': (list, NetworkPolicyIngressRule),
            'podSelector': (LabelSelector, None),
            'policyTypes': (list, str),

        }

    @property
    def egress(self) -> typing.List['NetworkPolicyEgressRule']:
        """
        List of egress rules to be applied to the selected pods.
        Outgoing traffic is allowed if there are no NetworkPolicies
        selecting the pod (and cluster policy otherwise allows the
        traffic), OR if the traffic matches at least one egress rule
        across all of the NetworkPolicy objects whose podSelector
        matches the pod. If this field is empty then this
        NetworkPolicy limits all outgoing traffic (and serves solely
        to ensure that the pods it selects are isolated by default).
        This field is beta-level in 1.8
        """
        return self._properties.get('egress')

    @egress.setter
    def egress(
            self,
            value: typing.Union[typing.List['NetworkPolicyEgressRule'], typing.List[dict]]
    ):
        """
        List of egress rules to be applied to the selected pods.
        Outgoing traffic is allowed if there are no NetworkPolicies
        selecting the pod (and cluster policy otherwise allows the
        traffic), OR if the traffic matches at least one egress rule
        across all of the NetworkPolicy objects whose podSelector
        matches the pod. If this field is empty then this
        NetworkPolicy limits all outgoing traffic (and serves solely
        to ensure that the pods it selects are isolated by default).
        This field is beta-level in 1.8
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyEgressRule().from_dict(item)
            cleaned.append(item)
        self._properties['egress'] = cleaned

    @property
    def ingress(self) -> typing.List['NetworkPolicyIngressRule']:
        """
        List of ingress rules to be applied to the selected pods.
        Traffic is allowed to a pod if there are no NetworkPolicies
        selecting the pod (and cluster policy otherwise allows the
        traffic), OR if the traffic source is the pod's local node,
        OR if the traffic matches at least one ingress rule across
        all of the NetworkPolicy objects whose podSelector matches
        the pod. If this field is empty then this NetworkPolicy does
        not allow any traffic (and serves solely to ensure that the
        pods it selects are isolated by default)
        """
        return self._properties.get('ingress')

    @ingress.setter
    def ingress(
            self,
            value: typing.Union[typing.List['NetworkPolicyIngressRule'], typing.List[dict]]
    ):
        """
        List of ingress rules to be applied to the selected pods.
        Traffic is allowed to a pod if there are no NetworkPolicies
        selecting the pod (and cluster policy otherwise allows the
        traffic), OR if the traffic source is the pod's local node,
        OR if the traffic matches at least one ingress rule across
        all of the NetworkPolicy objects whose podSelector matches
        the pod. If this field is empty then this NetworkPolicy does
        not allow any traffic (and serves solely to ensure that the
        pods it selects are isolated by default)
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = NetworkPolicyIngressRule().from_dict(item)
            cleaned.append(item)
        self._properties['ingress'] = cleaned

    @property
    def pod_selector(self) -> 'LabelSelector':
        """
        Selects the pods to which this NetworkPolicy object applies.
        The array of ingress rules is applied to any pods selected
        by this field. Multiple network policies can select the same
        set of pods. In this case, the ingress rules for each are
        combined additively. This field is NOT optional and follows
        standard label selector semantics. An empty podSelector
        matches all pods in this namespace.
        """
        return self._properties.get('podSelector')

    @pod_selector.setter
    def pod_selector(self, value: typing.Union['LabelSelector', dict]):
        """
        Selects the pods to which this NetworkPolicy object applies.
        The array of ingress rules is applied to any pods selected
        by this field. Multiple network policies can select the same
        set of pods. In this case, the ingress rules for each are
        combined additively. This field is NOT optional and follows
        standard label selector semantics. An empty podSelector
        matches all pods in this namespace.
        """
        if isinstance(value, dict):
            value = LabelSelector().from_dict(value)
        self._properties['podSelector'] = value

    @property
    def policy_types(self) -> typing.List[str]:
        """
        List of rule types that the NetworkPolicy relates to. Valid
        options are Ingress, Egress, or Ingress,Egress. If this
        field is not specified, it will default based on the
        existence of Ingress or Egress rules; policies that contain
        an Egress section are assumed to affect Egress, and all
        policies (whether or not they contain an Ingress section)
        are assumed to affect Ingress. If you want to write an
        egress-only policy, you must explicitly specify policyTypes
        [ "Egress" ]. Likewise, if you want to write a policy that
        specifies that no egress is allowed, you must specify a
        policyTypes value that include "Egress" (since such a policy
        would not include an Egress section and would otherwise
        default to just [ "Ingress" ]). This field is beta-level in
        1.8
        """
        return self._properties.get('policyTypes')

    @policy_types.setter
    def policy_types(self, value: typing.List[str]):
        """
        List of rule types that the NetworkPolicy relates to. Valid
        options are Ingress, Egress, or Ingress,Egress. If this
        field is not specified, it will default based on the
        existence of Ingress or Egress rules; policies that contain
        an Egress section are assumed to affect Egress, and all
        policies (whether or not they contain an Ingress section)
        are assumed to affect Ingress. If you want to write an
        egress-only policy, you must explicitly specify policyTypes
        [ "Egress" ]. Likewise, if you want to write a policy that
        specifies that no egress is allowed, you must specify a
        policyTypes value that include "Egress" (since such a policy
        would not include an Egress section and would otherwise
        default to just [ "Ingress" ]). This field is beta-level in
        1.8
        """
        self._properties['policyTypes'] = value

    def __enter__(self) -> 'NetworkPolicySpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
