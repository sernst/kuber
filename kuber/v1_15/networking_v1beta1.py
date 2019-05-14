import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_15.meta_v1 import ListMeta
from kuber.v1_15.core_v1 import LoadBalancerStatus
from kuber.v1_15.meta_v1 import ObjectMeta
from kuber.v1_15.meta_v1 import Status
from kuber.v1_15.meta_v1 import StatusDetails


class HTTPIngressPath(_kuber_definitions.Definition):
    """
    HTTPIngressPath associates a path regex with a backend.
    Incoming urls matching the path are forwarded to the
    backend.
    """

    def __init__(
            self,
            backend: 'IngressBackend' = None,
            path: str = None,
    ):
        """Create HTTPIngressPath instance."""
        super(HTTPIngressPath, self).__init__(
            api_version='networking/v1beta1',
            kind='HTTPIngressPath'
        )
        self._properties = {
            'backend': backend or IngressBackend(),
            'path': path or '',

        }
        self._types = {
            'backend': (IngressBackend, None),
            'path': (str, None),

        }

    @property
    def backend(self) -> 'IngressBackend':
        """
        Backend defines the referenced service endpoint to which the
        traffic will be forwarded to.
        """
        return self._properties.get('backend')

    @backend.setter
    def backend(self, value: typing.Union['IngressBackend', dict]):
        """
        Backend defines the referenced service endpoint to which the
        traffic will be forwarded to.
        """
        if isinstance(value, dict):
            value = IngressBackend().from_dict(value)
        self._properties['backend'] = value

    @property
    def path(self) -> str:
        """
        Path is an extended POSIX regex as defined by IEEE Std
        1003.1, (i.e this follows the egrep/unix syntax, not the
        perl syntax) matched against the path of an incoming
        request. Currently it can contain characters disallowed from
        the conventional "path" part of a URL as defined by RFC
        3986. Paths must begin with a '/'. If unspecified, the path
        defaults to a catch all sending traffic to the backend.
        """
        return self._properties.get('path')

    @path.setter
    def path(self, value: str):
        """
        Path is an extended POSIX regex as defined by IEEE Std
        1003.1, (i.e this follows the egrep/unix syntax, not the
        perl syntax) matched against the path of an incoming
        request. Currently it can contain characters disallowed from
        the conventional "path" part of a URL as defined by RFC
        3986. Paths must begin with a '/'. If unspecified, the path
        defaults to a catch all sending traffic to the backend.
        """
        self._properties['path'] = value

    def __enter__(self) -> 'HTTPIngressPath':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class HTTPIngressRuleValue(_kuber_definitions.Definition):
    """
    HTTPIngressRuleValue is a list of http selectors pointing to
    backends. In the example: http://<host>/<path>?<searchpart>
    -> backend where where parts of the url correspond to RFC
    3986, this resource will be used to match against everything
    after the last '/' and before the first '?' or '#'.
    """

    def __init__(
            self,
            paths: typing.List['HTTPIngressPath'] = None,
    ):
        """Create HTTPIngressRuleValue instance."""
        super(HTTPIngressRuleValue, self).__init__(
            api_version='networking/v1beta1',
            kind='HTTPIngressRuleValue'
        )
        self._properties = {
            'paths': paths or [],

        }
        self._types = {
            'paths': (list, HTTPIngressPath),

        }

    @property
    def paths(self) -> typing.List['HTTPIngressPath']:
        """
        A collection of paths that map requests to backends.
        """
        return self._properties.get('paths')

    @paths.setter
    def paths(
            self,
            value: typing.Union[typing.List['HTTPIngressPath'], typing.List[dict]]
    ):
        """
        A collection of paths that map requests to backends.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = HTTPIngressPath().from_dict(item)
            cleaned.append(item)
        self._properties['paths'] = cleaned

    def __enter__(self) -> 'HTTPIngressRuleValue':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Ingress(_kuber_definitions.Resource):
    """
    Ingress is a collection of rules that allow inbound
    connections to reach the endpoints defined by a backend. An
    Ingress can be configured to give services externally-
    reachable urls, load balance traffic, terminate SSL, offer
    name based virtual hosting etc.
    """

    def __init__(
            self,
            metadata: 'ObjectMeta' = None,
            spec: 'IngressSpec' = None,
            status: 'IngressStatus' = None,
    ):
        """Create Ingress instance."""
        super(Ingress, self).__init__(
            api_version='networking/v1beta1',
            kind='Ingress'
        )
        self._properties = {
            'metadata': metadata or ObjectMeta(),
            'spec': spec or IngressSpec(),
            'status': status or IngressStatus(),

        }
        self._types = {
            'apiVersion': (str, None),
            'kind': (str, None),
            'metadata': (ObjectMeta, None),
            'spec': (IngressSpec, None),
            'status': (IngressStatus, None),

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
    def spec(self) -> 'IngressSpec':
        """
        Spec is the desired state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('spec')

    @spec.setter
    def spec(self, value: typing.Union['IngressSpec', dict]):
        """
        Spec is the desired state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = IngressSpec().from_dict(value)
        self._properties['spec'] = value

    @property
    def status(self) -> 'IngressStatus':
        """
        Status is the current state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        return self._properties.get('status')

    @status.setter
    def status(self, value: typing.Union['IngressStatus', dict]):
        """
        Status is the current state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = IngressStatus().from_dict(value)
        self._properties['status'] = value

    def create_resource(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Creates the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            'create_namespaced_ingress',
            'create_ingress'
        ]

        response = _kube_api.execute(
            action='create',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict()}
        )
        return (
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def replace_resource(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Replaces the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'replace_namespaced_ingress',
            'replace_ingress'
        ]

        response = _kube_api.execute(
            action='replace',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def patch_resource(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Patches the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            'patch_namespaced_ingress',
            'patch_ingress'
        ]

        response = _kube_api.execute(
            action='patch',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'body': self.to_dict(), 'name': self.metadata.name}
        )
        return (
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def get_resource_status(
            self,
            namespace: 'str' = None
    ) -> 'IngressStatus':
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            'read_namespaced_ingress',
            'read_ingress'
        ]

        response = _kube_api.execute(
            action='read',
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={'name': self.metadata.name}
        )
        return (
            IngressStatus()
            .from_dict(_kube_api.to_kuber_dict(response.status))
        )

    def read_resource(
            self,
            namespace: str = None
    ):
        """
        Reads the Ingress from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            'read_namespaced_ingress',
            'read_ingress'
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
        Deletes the Ingress from the currently configured
        Kubernetes cluster.
        """
        names = [
            'delete_namespaced_ingress',
            'delete_ingress'
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
    ) -> 'client.NetworkingV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

    def __enter__(self) -> 'Ingress':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressBackend(_kuber_definitions.Definition):
    """
    IngressBackend describes all endpoints for a given service
    and port.
    """

    def __init__(
            self,
            service_name: str = None,
            service_port: typing.Union[str, int, None] = None,
    ):
        """Create IngressBackend instance."""
        super(IngressBackend, self).__init__(
            api_version='networking/v1beta1',
            kind='IngressBackend'
        )
        self._properties = {
            'serviceName': service_name or '',
            'servicePort': service_port or None,

        }
        self._types = {
            'serviceName': (str, None),
            'servicePort': (int, None),

        }

    @property
    def service_name(self) -> str:
        """
        Specifies the name of the referenced service.
        """
        return self._properties.get('serviceName')

    @service_name.setter
    def service_name(self, value: str):
        """
        Specifies the name of the referenced service.
        """
        self._properties['serviceName'] = value

    @property
    def service_port(self) -> typing.Optional[int]:
        """
        Specifies the port of the referenced service.
        """
        value = self._properties.get('servicePort')
        return int(value) if value is not None else None

    @service_port.setter
    def service_port(
            self,
            value: typing.Union[str, int, None]
    ):
        """
        Specifies the port of the referenced service.
        """
        self._properties['servicePort'] = None if value is None else f'{value}'

    def __enter__(self) -> 'IngressBackend':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressList(_kuber_definitions.Collection):
    """
    IngressList is a collection of Ingress.
    """

    def __init__(
            self,
            items: typing.List['Ingress'] = None,
            metadata: 'ListMeta' = None,
    ):
        """Create IngressList instance."""
        super(IngressList, self).__init__(
            api_version='networking/v1beta1',
            kind='IngressList'
        )
        self._properties = {
            'items': items or [],
            'metadata': metadata or ListMeta(),

        }
        self._types = {
            'apiVersion': (str, None),
            'items': (list, Ingress),
            'kind': (str, None),
            'metadata': (ListMeta, None),

        }

    @property
    def items(self) -> typing.List['Ingress']:
        """
        Items is the list of Ingress.
        """
        return self._properties.get('items')

    @items.setter
    def items(
            self,
            value: typing.Union[typing.List['Ingress'], typing.List[dict]]
    ):
        """
        Items is the list of Ingress.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = Ingress().from_dict(item)
            cleaned.append(item)
        self._properties['items'] = cleaned

    @property
    def metadata(self) -> 'ListMeta':
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-
        conventions.md#metadata
        """
        return self._properties.get('metadata')

    @metadata.setter
    def metadata(self, value: typing.Union['ListMeta', dict]):
        """
        Standard object's metadata. More info:
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
    ) -> 'client.NetworkingV1beta1Api':
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs['apl_client'] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

    def __enter__(self) -> 'IngressList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressRule(_kuber_definitions.Definition):
    """
    IngressRule represents the rules mapping the paths under a
    specified host to the related backend services. Incoming
    requests are first evaluated for a host match, then routed
    to the backend associated with the matching
    IngressRuleValue.
    """

    def __init__(
            self,
            host: str = None,
            http: 'HTTPIngressRuleValue' = None,
    ):
        """Create IngressRule instance."""
        super(IngressRule, self).__init__(
            api_version='networking/v1beta1',
            kind='IngressRule'
        )
        self._properties = {
            'host': host or '',
            'http': http or HTTPIngressRuleValue(),

        }
        self._types = {
            'host': (str, None),
            'http': (HTTPIngressRuleValue, None),

        }

    @property
    def host(self) -> str:
        """
        Host is the fully qualified domain name of a network host,
        as defined by RFC 3986. Note the following deviations from
        the "host" part of the URI as defined in the RFC: 1. IPs are
        not allowed. Currently an IngressRuleValue can only apply to
        the
        	  IP in the Spec of the parent Ingress.
        2. The `:`
        delimiter is not respected because ports are not allowed.
        Currently the port of an Ingress is implicitly :80 for http
        and
        	  :443 for https.
        Both these may change in the future.
        Incoming requests are matched against the host before the
        IngressRuleValue. If the host is unspecified, the Ingress
        routes all traffic based on the specified IngressRuleValue.
        """
        return self._properties.get('host')

    @host.setter
    def host(self, value: str):
        """
        Host is the fully qualified domain name of a network host,
        as defined by RFC 3986. Note the following deviations from
        the "host" part of the URI as defined in the RFC: 1. IPs are
        not allowed. Currently an IngressRuleValue can only apply to
        the
        	  IP in the Spec of the parent Ingress.
        2. The `:`
        delimiter is not respected because ports are not allowed.
        Currently the port of an Ingress is implicitly :80 for http
        and
        	  :443 for https.
        Both these may change in the future.
        Incoming requests are matched against the host before the
        IngressRuleValue. If the host is unspecified, the Ingress
        routes all traffic based on the specified IngressRuleValue.
        """
        self._properties['host'] = value

    @property
    def http(self) -> 'HTTPIngressRuleValue':
        """

        """
        return self._properties.get('http')

    @http.setter
    def http(self, value: typing.Union['HTTPIngressRuleValue', dict]):
        """

        """
        if isinstance(value, dict):
            value = HTTPIngressRuleValue().from_dict(value)
        self._properties['http'] = value

    def __enter__(self) -> 'IngressRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressSpec(_kuber_definitions.Definition):
    """
    IngressSpec describes the Ingress the user wishes to exist.
    """

    def __init__(
            self,
            backend: 'IngressBackend' = None,
            rules: typing.List['IngressRule'] = None,
            tls: typing.List['IngressTLS'] = None,
    ):
        """Create IngressSpec instance."""
        super(IngressSpec, self).__init__(
            api_version='networking/v1beta1',
            kind='IngressSpec'
        )
        self._properties = {
            'backend': backend or IngressBackend(),
            'rules': rules or [],
            'tls': tls or [],

        }
        self._types = {
            'backend': (IngressBackend, None),
            'rules': (list, IngressRule),
            'tls': (list, IngressTLS),

        }

    @property
    def backend(self) -> 'IngressBackend':
        """
        A default backend capable of servicing requests that don't
        match any rule. At least one of 'backend' or 'rules' must be
        specified. This field is optional to allow the loadbalancer
        controller or defaulting logic to specify a global default.
        """
        return self._properties.get('backend')

    @backend.setter
    def backend(self, value: typing.Union['IngressBackend', dict]):
        """
        A default backend capable of servicing requests that don't
        match any rule. At least one of 'backend' or 'rules' must be
        specified. This field is optional to allow the loadbalancer
        controller or defaulting logic to specify a global default.
        """
        if isinstance(value, dict):
            value = IngressBackend().from_dict(value)
        self._properties['backend'] = value

    @property
    def rules(self) -> typing.List['IngressRule']:
        """
        A list of host rules used to configure the Ingress. If
        unspecified, or no rule matches, all traffic is sent to the
        default backend.
        """
        return self._properties.get('rules')

    @rules.setter
    def rules(
            self,
            value: typing.Union[typing.List['IngressRule'], typing.List[dict]]
    ):
        """
        A list of host rules used to configure the Ingress. If
        unspecified, or no rule matches, all traffic is sent to the
        default backend.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IngressRule().from_dict(item)
            cleaned.append(item)
        self._properties['rules'] = cleaned

    @property
    def tls(self) -> typing.List['IngressTLS']:
        """
        TLS configuration. Currently the Ingress only supports a
        single TLS port, 443. If multiple members of this list
        specify different hosts, they will be multiplexed on the
        same port according to the hostname specified through the
        SNI TLS extension, if the ingress controller fulfilling the
        ingress supports SNI.
        """
        return self._properties.get('tls')

    @tls.setter
    def tls(
            self,
            value: typing.Union[typing.List['IngressTLS'], typing.List[dict]]
    ):
        """
        TLS configuration. Currently the Ingress only supports a
        single TLS port, 443. If multiple members of this list
        specify different hosts, they will be multiplexed on the
        same port according to the hostname specified through the
        SNI TLS extension, if the ingress controller fulfilling the
        ingress supports SNI.
        """
        cleaned = []
        for item in value:
            if isinstance(item, dict):
                item = IngressTLS().from_dict(item)
            cleaned.append(item)
        self._properties['tls'] = cleaned

    def __enter__(self) -> 'IngressSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressStatus(_kuber_definitions.Definition):
    """
    IngressStatus describe the current state of the Ingress.
    """

    def __init__(
            self,
            load_balancer: 'LoadBalancerStatus' = None,
    ):
        """Create IngressStatus instance."""
        super(IngressStatus, self).__init__(
            api_version='networking/v1beta1',
            kind='IngressStatus'
        )
        self._properties = {
            'loadBalancer': load_balancer or LoadBalancerStatus(),

        }
        self._types = {
            'loadBalancer': (LoadBalancerStatus, None),

        }

    @property
    def load_balancer(self) -> 'LoadBalancerStatus':
        """
        LoadBalancer contains the current status of the load-
        balancer.
        """
        return self._properties.get('loadBalancer')

    @load_balancer.setter
    def load_balancer(self, value: typing.Union['LoadBalancerStatus', dict]):
        """
        LoadBalancer contains the current status of the load-
        balancer.
        """
        if isinstance(value, dict):
            value = LoadBalancerStatus().from_dict(value)
        self._properties['loadBalancer'] = value

    def __enter__(self) -> 'IngressStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressTLS(_kuber_definitions.Definition):
    """
    IngressTLS describes the transport layer security associated
    with an Ingress.
    """

    def __init__(
            self,
            hosts: typing.List[str] = None,
            secret_name: str = None,
    ):
        """Create IngressTLS instance."""
        super(IngressTLS, self).__init__(
            api_version='networking/v1beta1',
            kind='IngressTLS'
        )
        self._properties = {
            'hosts': hosts or [],
            'secretName': secret_name or '',

        }
        self._types = {
            'hosts': (list, str),
            'secretName': (str, None),

        }

    @property
    def hosts(self) -> typing.List[str]:
        """
        Hosts are a list of hosts included in the TLS certificate.
        The values in this list must match the name/s used in the
        tlsSecret. Defaults to the wildcard host setting for the
        loadbalancer controller fulfilling this Ingress, if left
        unspecified.
        """
        return self._properties.get('hosts')

    @hosts.setter
    def hosts(self, value: typing.List[str]):
        """
        Hosts are a list of hosts included in the TLS certificate.
        The values in this list must match the name/s used in the
        tlsSecret. Defaults to the wildcard host setting for the
        loadbalancer controller fulfilling this Ingress, if left
        unspecified.
        """
        self._properties['hosts'] = value

    @property
    def secret_name(self) -> str:
        """
        SecretName is the name of the secret used to terminate SSL
        traffic on 443. Field is left optional to allow SSL routing
        based on SNI hostname alone. If the SNI host in a listener
        conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the Host header is used for routing.
        """
        return self._properties.get('secretName')

    @secret_name.setter
    def secret_name(self, value: str):
        """
        SecretName is the name of the secret used to terminate SSL
        traffic on 443. Field is left optional to allow SSL routing
        based on SNI hostname alone. If the SNI host in a listener
        conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the Host header is used for routing.
        """
        self._properties['secretName'] = value

    def __enter__(self) -> 'IngressTLS':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
