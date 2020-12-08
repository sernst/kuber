import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_19.meta_v1 import LabelSelector
from kuber.v1_19.meta_v1 import ListMeta
from kuber.v1_19.core_v1 import LoadBalancerStatus
from kuber.v1_19.meta_v1 import ObjectMeta
from kuber.v1_19.meta_v1 import Status
from kuber.v1_19.meta_v1 import StatusDetails
from kuber.v1_19.core_v1 import TypedLocalObjectReference


class HTTPIngressPath(_kuber_definitions.Definition):
    """
    HTTPIngressPath associates a path with a backend. Incoming
    urls matching the path are forwarded to the backend.
    """

    def __init__(
        self,
        backend: "IngressBackend" = None,
        path: str = None,
        path_type: str = None,
    ):
        """Create HTTPIngressPath instance."""
        super(HTTPIngressPath, self).__init__(
            api_version="networking/v1", kind="HTTPIngressPath"
        )
        self._properties = {
            "backend": backend if backend is not None else IngressBackend(),
            "path": path if path is not None else "",
            "pathType": path_type if path_type is not None else "",
        }
        self._types = {
            "backend": (IngressBackend, None),
            "path": (str, None),
            "pathType": (str, None),
        }

    @property
    def backend(self) -> "IngressBackend":
        """
        Backend defines the referenced service endpoint to which the
        traffic will be forwarded to.
        """
        return typing.cast(
            "IngressBackend",
            self._properties.get("backend"),
        )

    @backend.setter
    def backend(self, value: typing.Union["IngressBackend", dict]):
        """
        Backend defines the referenced service endpoint to which the
        traffic will be forwarded to.
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressBackend,
                IngressBackend().from_dict(value),
            )
        self._properties["backend"] = value

    @property
    def path(self) -> str:
        """
        Path is matched against the path of an incoming request.
        Currently it can contain characters disallowed from the
        conventional "path" part of a URL as defined by RFC 3986.
        Paths must begin with a '/'. When unspecified, all paths
        from incoming requests are matched.
        """
        return typing.cast(
            str,
            self._properties.get("path"),
        )

    @path.setter
    def path(self, value: str):
        """
        Path is matched against the path of an incoming request.
        Currently it can contain characters disallowed from the
        conventional "path" part of a URL as defined by RFC 3986.
        Paths must begin with a '/'. When unspecified, all paths
        from incoming requests are matched.
        """
        self._properties["path"] = value

    @property
    def path_type(self) -> str:
        """
        PathType determines the interpretation of the Path matching.
        PathType can be one of the following values: * Exact:
        Matches the URL path exactly. * Prefix: Matches based on a
        URL path prefix split by '/'. Matching is
          done on a path element by element basis. A path element
        refers is the
          list of labels in the path split by the '/' separator. A
        request is a
          match for path p if every p is an element-wise prefix of p
        of the
          request path. Note that if the last element of the path is
        a substring
          of the last element in request path, it is not a match
        (e.g. /foo/bar
          matches /foo/bar/baz, but does not match /foo/barbaz).
        * ImplementationSpecific: Interpretation of the Path
        matching is up to
          the IngressClass. Implementations can treat this as a
        separate PathType
          or treat it identically to Prefix or Exact path types.
        Implementations are required to support all path types.
        """
        return typing.cast(
            str,
            self._properties.get("pathType"),
        )

    @path_type.setter
    def path_type(self, value: str):
        """
        PathType determines the interpretation of the Path matching.
        PathType can be one of the following values: * Exact:
        Matches the URL path exactly. * Prefix: Matches based on a
        URL path prefix split by '/'. Matching is
          done on a path element by element basis. A path element
        refers is the
          list of labels in the path split by the '/' separator. A
        request is a
          match for path p if every p is an element-wise prefix of p
        of the
          request path. Note that if the last element of the path is
        a substring
          of the last element in request path, it is not a match
        (e.g. /foo/bar
          matches /foo/bar/baz, but does not match /foo/barbaz).
        * ImplementationSpecific: Interpretation of the Path
        matching is up to
          the IngressClass. Implementations can treat this as a
        separate PathType
          or treat it identically to Prefix or Exact path types.
        Implementations are required to support all path types.
        """
        self._properties["pathType"] = value

    def __enter__(self) -> "HTTPIngressPath":
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
        paths: typing.List["HTTPIngressPath"] = None,
    ):
        """Create HTTPIngressRuleValue instance."""
        super(HTTPIngressRuleValue, self).__init__(
            api_version="networking/v1", kind="HTTPIngressRuleValue"
        )
        self._properties = {
            "paths": paths if paths is not None else [],
        }
        self._types = {
            "paths": (list, HTTPIngressPath),
        }

    @property
    def paths(self) -> typing.List["HTTPIngressPath"]:
        """
        A collection of paths that map requests to backends.
        """
        return typing.cast(
            typing.List["HTTPIngressPath"],
            self._properties.get("paths"),
        )

    @paths.setter
    def paths(
        self, value: typing.Union[typing.List["HTTPIngressPath"], typing.List[dict]]
    ):
        """
        A collection of paths that map requests to backends.
        """
        cleaned: typing.List[HTTPIngressPath] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    HTTPIngressPath,
                    HTTPIngressPath().from_dict(item),
                )
            cleaned.append(typing.cast(HTTPIngressPath, item))
        self._properties["paths"] = cleaned

    def __enter__(self) -> "HTTPIngressRuleValue":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IPBlock(_kuber_definitions.Definition):
    """
    IPBlock describes a particular CIDR (Ex.
    "192.168.1.1/24","2001:db9::/64") that is allowed to the
    pods matched by a NetworkPolicySpec's podSelector. The
    except entry describes CIDRs that should not be included
    within this rule.
    """

    def __init__(
        self,
        cidr: str = None,
        except_: typing.List[str] = None,
    ):
        """Create IPBlock instance."""
        super(IPBlock, self).__init__(api_version="networking/v1", kind="IPBlock")
        self._properties = {
            "cidr": cidr if cidr is not None else "",
            "except": except_ if except_ is not None else [],
        }
        self._types = {
            "cidr": (str, None),
            "except": (list, str),
        }

    @property
    def cidr(self) -> str:
        """
        CIDR is a string representing the IP Block Valid examples
        are "192.168.1.1/24" or "2001:db9::/64"
        """
        return typing.cast(
            str,
            self._properties.get("cidr"),
        )

    @cidr.setter
    def cidr(self, value: str):
        """
        CIDR is a string representing the IP Block Valid examples
        are "192.168.1.1/24" or "2001:db9::/64"
        """
        self._properties["cidr"] = value

    @property
    def except_(self) -> typing.List[str]:
        """
        Except is a slice of CIDRs that should not be included
        within an IP Block Valid examples are "192.168.1.1/24" or
        "2001:db9::/64" Except values will be rejected if they are
        outside the CIDR range
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("except"),
        )

    @except_.setter
    def except_(self, value: typing.List[str]):
        """
        Except is a slice of CIDRs that should not be included
        within an IP Block Valid examples are "192.168.1.1/24" or
        "2001:db9::/64" Except values will be rejected if they are
        outside the CIDR range
        """
        self._properties["except"] = value

    def __enter__(self) -> "IPBlock":
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
        metadata: "ObjectMeta" = None,
        spec: "IngressSpec" = None,
        status: "IngressStatus" = None,
    ):
        """Create Ingress instance."""
        super(Ingress, self).__init__(api_version="networking/v1", kind="Ingress")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else IngressSpec(),
            "status": status if status is not None else IngressStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (IngressSpec, None),
            "status": (IngressStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "IngressSpec":
        """
        Spec is the desired state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "IngressSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["IngressSpec", dict]):
        """
        Spec is the desired state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressSpec,
                IngressSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "IngressStatus":
        """
        Status is the current state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "IngressStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["IngressStatus", dict]):
        """
        Status is the current state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressStatus,
                IngressStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "IngressStatus":
        """
        Creates the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_ingress", "create_ingress"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = IngressStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "IngressStatus":
        """
        Replaces the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_ingress", "replace_ingress"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = IngressStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "IngressStatus":
        """
        Patches the Ingress in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_ingress", "patch_ingress"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = IngressStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "IngressStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_ingress", "read_ingress"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = IngressStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the Ingress from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_ingress",
            "read_ingress",
        ]
        return _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

    def delete_resource(
        self,
        namespace: str = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the Ingress from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_ingress",
            "delete_ingress",
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds,
        )

        _kube_api.execute(
            action="delete",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name, "body": body},
        )

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NetworkingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> "Ingress":
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
        resource: "TypedLocalObjectReference" = None,
        service: "IngressServiceBackend" = None,
    ):
        """Create IngressBackend instance."""
        super(IngressBackend, self).__init__(
            api_version="networking/v1", kind="IngressBackend"
        )
        self._properties = {
            "resource": resource
            if resource is not None
            else TypedLocalObjectReference(),
            "service": service if service is not None else IngressServiceBackend(),
        }
        self._types = {
            "resource": (TypedLocalObjectReference, None),
            "service": (IngressServiceBackend, None),
        }

    @property
    def resource(self) -> "TypedLocalObjectReference":
        """
        Resource is an ObjectRef to another Kubernetes resource in
        the namespace of the Ingress object. If resource is
        specified, a service.Name and service.Port must not be
        specified. This is a mutually exclusive setting with
        "Service".
        """
        return typing.cast(
            "TypedLocalObjectReference",
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: typing.Union["TypedLocalObjectReference", dict]):
        """
        Resource is an ObjectRef to another Kubernetes resource in
        the namespace of the Ingress object. If resource is
        specified, a service.Name and service.Port must not be
        specified. This is a mutually exclusive setting with
        "Service".
        """
        if isinstance(value, dict):
            value = typing.cast(
                TypedLocalObjectReference,
                TypedLocalObjectReference().from_dict(value),
            )
        self._properties["resource"] = value

    @property
    def service(self) -> "IngressServiceBackend":
        """
        Service references a Service as a Backend. This is a
        mutually exclusive setting with "Resource".
        """
        return typing.cast(
            "IngressServiceBackend",
            self._properties.get("service"),
        )

    @service.setter
    def service(self, value: typing.Union["IngressServiceBackend", dict]):
        """
        Service references a Service as a Backend. This is a
        mutually exclusive setting with "Resource".
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressServiceBackend,
                IngressServiceBackend().from_dict(value),
            )
        self._properties["service"] = value

    def __enter__(self) -> "IngressBackend":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressClass(_kuber_definitions.Resource):
    """
    IngressClass represents the class of the Ingress, referenced
    by the Ingress Spec. The `ingressclass.kubernetes.io/is-
    default-class` annotation can be used to indicate that an
    IngressClass should be considered default. When a single
    IngressClass resource has this annotation set to true, new
    Ingress resources without a class specified will be assigned
    this default class.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "IngressClassSpec" = None,
    ):
        """Create IngressClass instance."""
        super(IngressClass, self).__init__(
            api_version="networking/v1", kind="IngressClass"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else IngressClassSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (IngressClassSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "IngressClassSpec":
        """
        Spec is the desired state of the IngressClass. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "IngressClassSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["IngressClassSpec", dict]):
        """
        Spec is the desired state of the IngressClass. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressClassSpec,
                IngressClassSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: "str" = None):
        """
        Creates the IngressClass in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_ingress_class", "create_ingress_class"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: "str" = None):
        """
        Replaces the IngressClass in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_ingress_class", "replace_ingress_class"]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: "str" = None):
        """
        Patches the IngressClass in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_ingress_class", "patch_ingress_class"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: "str" = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: str = None):
        """
        Reads the IngressClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_ingress_class",
            "read_ingress_class",
        ]
        return _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

    def delete_resource(
        self,
        namespace: str = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the IngressClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_ingress_class",
            "delete_ingress_class",
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds,
        )

        _kube_api.execute(
            action="delete",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name, "body": body},
        )

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NetworkingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> "IngressClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressClassList(_kuber_definitions.Collection):
    """
    IngressClassList is a collection of IngressClasses.
    """

    def __init__(
        self,
        items: typing.List["IngressClass"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create IngressClassList instance."""
        super(IngressClassList, self).__init__(
            api_version="networking/v1", kind="IngressClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, IngressClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["IngressClass"]:
        """
        Items is the list of IngressClasses.
        """
        return typing.cast(
            typing.List["IngressClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["IngressClass"], typing.List[dict]]
    ):
        """
        Items is the list of IngressClasses.
        """
        cleaned: typing.List[IngressClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    IngressClass,
                    IngressClass().from_dict(item),
                )
            cleaned.append(typing.cast(IngressClass, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NetworkingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> "IngressClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressClassSpec(_kuber_definitions.Definition):
    """
    IngressClassSpec provides information about the class of an
    Ingress.
    """

    def __init__(
        self,
        controller: str = None,
        parameters: "TypedLocalObjectReference" = None,
    ):
        """Create IngressClassSpec instance."""
        super(IngressClassSpec, self).__init__(
            api_version="networking/v1", kind="IngressClassSpec"
        )
        self._properties = {
            "controller": controller if controller is not None else "",
            "parameters": parameters
            if parameters is not None
            else TypedLocalObjectReference(),
        }
        self._types = {
            "controller": (str, None),
            "parameters": (TypedLocalObjectReference, None),
        }

    @property
    def controller(self) -> str:
        """
        Controller refers to the name of the controller that should
        handle this class. This allows for different "flavors" that
        are controlled by the same controller. For example, you may
        have different Parameters for the same implementing
        controller. This should be specified as a domain-prefixed
        path no more than 250 characters in length, e.g.
        "acme.io/ingress-controller". This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("controller"),
        )

    @controller.setter
    def controller(self, value: str):
        """
        Controller refers to the name of the controller that should
        handle this class. This allows for different "flavors" that
        are controlled by the same controller. For example, you may
        have different Parameters for the same implementing
        controller. This should be specified as a domain-prefixed
        path no more than 250 characters in length, e.g.
        "acme.io/ingress-controller". This field is immutable.
        """
        self._properties["controller"] = value

    @property
    def parameters(self) -> "TypedLocalObjectReference":
        """
        Parameters is a link to a custom resource containing
        additional configuration for the controller. This is
        optional if the controller does not require extra
        parameters.
        """
        return typing.cast(
            "TypedLocalObjectReference",
            self._properties.get("parameters"),
        )

    @parameters.setter
    def parameters(self, value: typing.Union["TypedLocalObjectReference", dict]):
        """
        Parameters is a link to a custom resource containing
        additional configuration for the controller. This is
        optional if the controller does not require extra
        parameters.
        """
        if isinstance(value, dict):
            value = typing.cast(
                TypedLocalObjectReference,
                TypedLocalObjectReference().from_dict(value),
            )
        self._properties["parameters"] = value

    def __enter__(self) -> "IngressClassSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressList(_kuber_definitions.Collection):
    """
    IngressList is a collection of Ingress.
    """

    def __init__(
        self,
        items: typing.List["Ingress"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create IngressList instance."""
        super(IngressList, self).__init__(
            api_version="networking/v1", kind="IngressList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, Ingress),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["Ingress"]:
        """
        Items is the list of Ingress.
        """
        return typing.cast(
            typing.List["Ingress"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["Ingress"], typing.List[dict]]):
        """
        Items is the list of Ingress.
        """
        cleaned: typing.List[Ingress] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Ingress,
                    Ingress().from_dict(item),
                )
            cleaned.append(typing.cast(Ingress, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NetworkingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> "IngressList":
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
        http: "HTTPIngressRuleValue" = None,
    ):
        """Create IngressRule instance."""
        super(IngressRule, self).__init__(
            api_version="networking/v1", kind="IngressRule"
        )
        self._properties = {
            "host": host if host is not None else "",
            "http": http if http is not None else HTTPIngressRuleValue(),
        }
        self._types = {
            "host": (str, None),
            "http": (HTTPIngressRuleValue, None),
        }

    @property
    def host(self) -> str:
        """
        Host is the fully qualified domain name of a network host,
        as defined by RFC 3986. Note the following deviations from
        the "host" part of the URI as defined in RFC 3986: 1. IPs
        are not allowed. Currently an IngressRuleValue can only
        apply to
           the IP in the Spec of the parent Ingress.
        2. The `:` delimiter is not respected because ports are not
        allowed.
                  Currently the port of an Ingress is implicitly :80 for
        http and
                  :443 for https.
        Both these may change in the future. Incoming requests are
        matched against the host before the IngressRuleValue. If the
        host is unspecified, the Ingress routes all traffic based on
        the specified IngressRuleValue.

        Host can be "precise" which is a domain name without the
        terminating dot of a network host (e.g. "foo.bar.com") or
        "wildcard", which is a domain name prefixed with a single
        wildcard label (e.g. "*.foo.com"). The wildcard character
        '*' must appear by itself as the first DNS label and matches
        only a single label. You cannot have a wildcard label by
        itself (e.g. Host == "*"). Requests will be matched against
        the Host field in the following way: 1. If Host is precise,
        the request matches this rule if the http host header is
        equal to Host. 2. If Host is a wildcard, then the request
        matches this rule if the http host header is to equal to the
        suffix (removing the first label) of the wildcard rule.
        """
        return typing.cast(
            str,
            self._properties.get("host"),
        )

    @host.setter
    def host(self, value: str):
        """
        Host is the fully qualified domain name of a network host,
        as defined by RFC 3986. Note the following deviations from
        the "host" part of the URI as defined in RFC 3986: 1. IPs
        are not allowed. Currently an IngressRuleValue can only
        apply to
           the IP in the Spec of the parent Ingress.
        2. The `:` delimiter is not respected because ports are not
        allowed.
                  Currently the port of an Ingress is implicitly :80 for
        http and
                  :443 for https.
        Both these may change in the future. Incoming requests are
        matched against the host before the IngressRuleValue. If the
        host is unspecified, the Ingress routes all traffic based on
        the specified IngressRuleValue.

        Host can be "precise" which is a domain name without the
        terminating dot of a network host (e.g. "foo.bar.com") or
        "wildcard", which is a domain name prefixed with a single
        wildcard label (e.g. "*.foo.com"). The wildcard character
        '*' must appear by itself as the first DNS label and matches
        only a single label. You cannot have a wildcard label by
        itself (e.g. Host == "*"). Requests will be matched against
        the Host field in the following way: 1. If Host is precise,
        the request matches this rule if the http host header is
        equal to Host. 2. If Host is a wildcard, then the request
        matches this rule if the http host header is to equal to the
        suffix (removing the first label) of the wildcard rule.
        """
        self._properties["host"] = value

    @property
    def http(self) -> "HTTPIngressRuleValue":
        """"""
        return typing.cast(
            "HTTPIngressRuleValue",
            self._properties.get("http"),
        )

    @http.setter
    def http(self, value: typing.Union["HTTPIngressRuleValue", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                HTTPIngressRuleValue,
                HTTPIngressRuleValue().from_dict(value),
            )
        self._properties["http"] = value

    def __enter__(self) -> "IngressRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressServiceBackend(_kuber_definitions.Definition):
    """
    IngressServiceBackend references a Kubernetes Service as a
    Backend.
    """

    def __init__(
        self,
        name: str = None,
        port: "ServiceBackendPort" = None,
    ):
        """Create IngressServiceBackend instance."""
        super(IngressServiceBackend, self).__init__(
            api_version="networking/v1", kind="IngressServiceBackend"
        )
        self._properties = {
            "name": name if name is not None else "",
            "port": port if port is not None else ServiceBackendPort(),
        }
        self._types = {
            "name": (str, None),
            "port": (ServiceBackendPort, None),
        }

    @property
    def name(self) -> str:
        """
        Name is the referenced service. The service must exist in
        the same namespace as the Ingress object.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the referenced service. The service must exist in
        the same namespace as the Ingress object.
        """
        self._properties["name"] = value

    @property
    def port(self) -> "ServiceBackendPort":
        """
        Port of the referenced service. A port name or port number
        is required for a IngressServiceBackend.
        """
        return typing.cast(
            "ServiceBackendPort",
            self._properties.get("port"),
        )

    @port.setter
    def port(self, value: typing.Union["ServiceBackendPort", dict]):
        """
        Port of the referenced service. A port name or port number
        is required for a IngressServiceBackend.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ServiceBackendPort,
                ServiceBackendPort().from_dict(value),
            )
        self._properties["port"] = value

    def __enter__(self) -> "IngressServiceBackend":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressSpec(_kuber_definitions.Definition):
    """
    IngressSpec describes the Ingress the user wishes to exist.
    """

    def __init__(
        self,
        default_backend: "IngressBackend" = None,
        ingress_class_name: str = None,
        rules: typing.List["IngressRule"] = None,
        tls: typing.List["IngressTLS"] = None,
    ):
        """Create IngressSpec instance."""
        super(IngressSpec, self).__init__(
            api_version="networking/v1", kind="IngressSpec"
        )
        self._properties = {
            "defaultBackend": default_backend
            if default_backend is not None
            else IngressBackend(),
            "ingressClassName": ingress_class_name
            if ingress_class_name is not None
            else "",
            "rules": rules if rules is not None else [],
            "tls": tls if tls is not None else [],
        }
        self._types = {
            "defaultBackend": (IngressBackend, None),
            "ingressClassName": (str, None),
            "rules": (list, IngressRule),
            "tls": (list, IngressTLS),
        }

    @property
    def default_backend(self) -> "IngressBackend":
        """
        DefaultBackend is the backend that should handle requests
        that don't match any rule. If Rules are not specified,
        DefaultBackend must be specified. If DefaultBackend is not
        set, the handling of requests that do not match any of the
        rules will be up to the Ingress controller.
        """
        return typing.cast(
            "IngressBackend",
            self._properties.get("defaultBackend"),
        )

    @default_backend.setter
    def default_backend(self, value: typing.Union["IngressBackend", dict]):
        """
        DefaultBackend is the backend that should handle requests
        that don't match any rule. If Rules are not specified,
        DefaultBackend must be specified. If DefaultBackend is not
        set, the handling of requests that do not match any of the
        rules will be up to the Ingress controller.
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressBackend,
                IngressBackend().from_dict(value),
            )
        self._properties["defaultBackend"] = value

    @property
    def ingress_class_name(self) -> str:
        """
        IngressClassName is the name of the IngressClass cluster
        resource. The associated IngressClass defines which
        controller will implement the resource. This replaces the
        deprecated `kubernetes.io/ingress.class` annotation. For
        backwards compatibility, when that annotation is set, it
        must be given precedence over this field. The controller may
        emit a warning if the field and annotation have different
        values. Implementations of this API should ignore Ingresses
        without a class specified. An IngressClass resource may be
        marked as default, which can be used to set a default value
        for this field. For more information, refer to the
        IngressClass documentation.
        """
        return typing.cast(
            str,
            self._properties.get("ingressClassName"),
        )

    @ingress_class_name.setter
    def ingress_class_name(self, value: str):
        """
        IngressClassName is the name of the IngressClass cluster
        resource. The associated IngressClass defines which
        controller will implement the resource. This replaces the
        deprecated `kubernetes.io/ingress.class` annotation. For
        backwards compatibility, when that annotation is set, it
        must be given precedence over this field. The controller may
        emit a warning if the field and annotation have different
        values. Implementations of this API should ignore Ingresses
        without a class specified. An IngressClass resource may be
        marked as default, which can be used to set a default value
        for this field. For more information, refer to the
        IngressClass documentation.
        """
        self._properties["ingressClassName"] = value

    @property
    def rules(self) -> typing.List["IngressRule"]:
        """
        A list of host rules used to configure the Ingress. If
        unspecified, or no rule matches, all traffic is sent to the
        default backend.
        """
        return typing.cast(
            typing.List["IngressRule"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(self, value: typing.Union[typing.List["IngressRule"], typing.List[dict]]):
        """
        A list of host rules used to configure the Ingress. If
        unspecified, or no rule matches, all traffic is sent to the
        default backend.
        """
        cleaned: typing.List[IngressRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    IngressRule,
                    IngressRule().from_dict(item),
                )
            cleaned.append(typing.cast(IngressRule, item))
        self._properties["rules"] = cleaned

    @property
    def tls(self) -> typing.List["IngressTLS"]:
        """
        TLS configuration. Currently the Ingress only supports a
        single TLS port, 443. If multiple members of this list
        specify different hosts, they will be multiplexed on the
        same port according to the hostname specified through the
        SNI TLS extension, if the ingress controller fulfilling the
        ingress supports SNI.
        """
        return typing.cast(
            typing.List["IngressTLS"],
            self._properties.get("tls"),
        )

    @tls.setter
    def tls(self, value: typing.Union[typing.List["IngressTLS"], typing.List[dict]]):
        """
        TLS configuration. Currently the Ingress only supports a
        single TLS port, 443. If multiple members of this list
        specify different hosts, they will be multiplexed on the
        same port according to the hostname specified through the
        SNI TLS extension, if the ingress controller fulfilling the
        ingress supports SNI.
        """
        cleaned: typing.List[IngressTLS] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    IngressTLS,
                    IngressTLS().from_dict(item),
                )
            cleaned.append(typing.cast(IngressTLS, item))
        self._properties["tls"] = cleaned

    def __enter__(self) -> "IngressSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressStatus(_kuber_definitions.Definition):
    """
    IngressStatus describe the current state of the Ingress.
    """

    def __init__(
        self,
        load_balancer: "LoadBalancerStatus" = None,
    ):
        """Create IngressStatus instance."""
        super(IngressStatus, self).__init__(
            api_version="networking/v1", kind="IngressStatus"
        )
        self._properties = {
            "loadBalancer": load_balancer
            if load_balancer is not None
            else LoadBalancerStatus(),
        }
        self._types = {
            "loadBalancer": (LoadBalancerStatus, None),
        }

    @property
    def load_balancer(self) -> "LoadBalancerStatus":
        """
        LoadBalancer contains the current status of the load-
        balancer.
        """
        return typing.cast(
            "LoadBalancerStatus",
            self._properties.get("loadBalancer"),
        )

    @load_balancer.setter
    def load_balancer(self, value: typing.Union["LoadBalancerStatus", dict]):
        """
        LoadBalancer contains the current status of the load-
        balancer.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LoadBalancerStatus,
                LoadBalancerStatus().from_dict(value),
            )
        self._properties["loadBalancer"] = value

    def __enter__(self) -> "IngressStatus":
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
        super(IngressTLS, self).__init__(api_version="networking/v1", kind="IngressTLS")
        self._properties = {
            "hosts": hosts if hosts is not None else [],
            "secretName": secret_name if secret_name is not None else "",
        }
        self._types = {
            "hosts": (list, str),
            "secretName": (str, None),
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
        return typing.cast(
            typing.List[str],
            self._properties.get("hosts"),
        )

    @hosts.setter
    def hosts(self, value: typing.List[str]):
        """
        Hosts are a list of hosts included in the TLS certificate.
        The values in this list must match the name/s used in the
        tlsSecret. Defaults to the wildcard host setting for the
        loadbalancer controller fulfilling this Ingress, if left
        unspecified.
        """
        self._properties["hosts"] = value

    @property
    def secret_name(self) -> str:
        """
        SecretName is the name of the secret used to terminate TLS
        traffic on port 443. Field is left optional to allow TLS
        routing based on SNI hostname alone. If the SNI host in a
        listener conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the Host header is used for routing.
        """
        return typing.cast(
            str,
            self._properties.get("secretName"),
        )

    @secret_name.setter
    def secret_name(self, value: str):
        """
        SecretName is the name of the secret used to terminate TLS
        traffic on port 443. Field is left optional to allow TLS
        routing based on SNI hostname alone. If the SNI host in a
        listener conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the Host header is used for routing.
        """
        self._properties["secretName"] = value

    def __enter__(self) -> "IngressTLS":
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
        metadata: "ObjectMeta" = None,
        spec: "NetworkPolicySpec" = None,
    ):
        """Create NetworkPolicy instance."""
        super(NetworkPolicy, self).__init__(
            api_version="networking/v1", kind="NetworkPolicy"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else NetworkPolicySpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (NetworkPolicySpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "NetworkPolicySpec":
        """
        Specification of the desired behavior for this
        NetworkPolicy.
        """
        return typing.cast(
            "NetworkPolicySpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["NetworkPolicySpec", dict]):
        """
        Specification of the desired behavior for this
        NetworkPolicy.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NetworkPolicySpec,
                NetworkPolicySpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: "str" = None):
        """
        Creates the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_network_policy", "create_network_policy"]

        _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

    def replace_resource(self, namespace: "str" = None):
        """
        Replaces the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_network_policy", "replace_network_policy"]

        _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def patch_resource(self, namespace: "str" = None):
        """
        Patches the NetworkPolicy in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_network_policy", "patch_network_policy"]

        _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

    def get_resource_status(self, namespace: "str" = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: str = None):
        """
        Reads the NetworkPolicy from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_network_policy",
            "read_network_policy",
        ]
        return _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

    def delete_resource(
        self,
        namespace: str = None,
        propagation_policy: str = "Foreground",
        grace_period_seconds: int = 10,
    ):
        """
        Deletes the NetworkPolicy from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_network_policy",
            "delete_network_policy",
        ]

        body = client.V1DeleteOptions(
            propagation_policy=propagation_policy,
            grace_period_seconds=grace_period_seconds,
        )

        _kube_api.execute(
            action="delete",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name, "body": body},
        )

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NetworkingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> "NetworkPolicy":
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
        ports: typing.List["NetworkPolicyPort"] = None,
        to: typing.List["NetworkPolicyPeer"] = None,
    ):
        """Create NetworkPolicyEgressRule instance."""
        super(NetworkPolicyEgressRule, self).__init__(
            api_version="networking/v1", kind="NetworkPolicyEgressRule"
        )
        self._properties = {
            "ports": ports if ports is not None else [],
            "to": to if to is not None else [],
        }
        self._types = {
            "ports": (list, NetworkPolicyPort),
            "to": (list, NetworkPolicyPeer),
        }

    @property
    def ports(self) -> typing.List["NetworkPolicyPort"]:
        """
        List of destination ports for outgoing traffic. Each item in
        this list is combined using a logical OR. If this field is
        empty or missing, this rule matches all ports (traffic not
        restricted by port). If this field is present and contains
        at least one item, then this rule allows traffic only if the
        traffic matches at least one port in the list.
        """
        return typing.cast(
            typing.List["NetworkPolicyPort"],
            self._properties.get("ports"),
        )

    @ports.setter
    def ports(
        self, value: typing.Union[typing.List["NetworkPolicyPort"], typing.List[dict]]
    ):
        """
        List of destination ports for outgoing traffic. Each item in
        this list is combined using a logical OR. If this field is
        empty or missing, this rule matches all ports (traffic not
        restricted by port). If this field is present and contains
        at least one item, then this rule allows traffic only if the
        traffic matches at least one port in the list.
        """
        cleaned: typing.List[NetworkPolicyPort] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NetworkPolicyPort,
                    NetworkPolicyPort().from_dict(item),
                )
            cleaned.append(typing.cast(NetworkPolicyPort, item))
        self._properties["ports"] = cleaned

    @property
    def to(self) -> typing.List["NetworkPolicyPeer"]:
        """
        List of destinations for outgoing traffic of pods selected
        for this rule. Items in this list are combined using a
        logical OR operation. If this field is empty or missing,
        this rule matches all destinations (traffic not restricted
        by destination). If this field is present and contains at
        least one item, this rule allows traffic only if the traffic
        matches at least one item in the to list.
        """
        return typing.cast(
            typing.List["NetworkPolicyPeer"],
            self._properties.get("to"),
        )

    @to.setter
    def to(
        self, value: typing.Union[typing.List["NetworkPolicyPeer"], typing.List[dict]]
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
        cleaned: typing.List[NetworkPolicyPeer] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NetworkPolicyPeer,
                    NetworkPolicyPeer().from_dict(item),
                )
            cleaned.append(typing.cast(NetworkPolicyPeer, item))
        self._properties["to"] = cleaned

    def __enter__(self) -> "NetworkPolicyEgressRule":
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
        from_: typing.List["NetworkPolicyPeer"] = None,
        ports: typing.List["NetworkPolicyPort"] = None,
    ):
        """Create NetworkPolicyIngressRule instance."""
        super(NetworkPolicyIngressRule, self).__init__(
            api_version="networking/v1", kind="NetworkPolicyIngressRule"
        )
        self._properties = {
            "from": from_ if from_ is not None else [],
            "ports": ports if ports is not None else [],
        }
        self._types = {
            "from": (list, NetworkPolicyPeer),
            "ports": (list, NetworkPolicyPort),
        }

    @property
    def from_(self) -> typing.List["NetworkPolicyPeer"]:
        """
        List of sources which should be able to access the pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all sources (traffic not
        restricted by source). If this field is present and contains
        at least one item, this rule allows traffic only if the
        traffic matches at least one item in the from list.
        """
        return typing.cast(
            typing.List["NetworkPolicyPeer"],
            self._properties.get("from"),
        )

    @from_.setter
    def from_(
        self, value: typing.Union[typing.List["NetworkPolicyPeer"], typing.List[dict]]
    ):
        """
        List of sources which should be able to access the pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all sources (traffic not
        restricted by source). If this field is present and contains
        at least one item, this rule allows traffic only if the
        traffic matches at least one item in the from list.
        """
        cleaned: typing.List[NetworkPolicyPeer] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NetworkPolicyPeer,
                    NetworkPolicyPeer().from_dict(item),
                )
            cleaned.append(typing.cast(NetworkPolicyPeer, item))
        self._properties["from"] = cleaned

    @property
    def ports(self) -> typing.List["NetworkPolicyPort"]:
        """
        List of ports which should be made accessible on the pods
        selected for this rule. Each item in this list is combined
        using a logical OR. If this field is empty or missing, this
        rule matches all ports (traffic not restricted by port). If
        this field is present and contains at least one item, then
        this rule allows traffic only if the traffic matches at
        least one port in the list.
        """
        return typing.cast(
            typing.List["NetworkPolicyPort"],
            self._properties.get("ports"),
        )

    @ports.setter
    def ports(
        self, value: typing.Union[typing.List["NetworkPolicyPort"], typing.List[dict]]
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
        cleaned: typing.List[NetworkPolicyPort] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NetworkPolicyPort,
                    NetworkPolicyPort().from_dict(item),
                )
            cleaned.append(typing.cast(NetworkPolicyPort, item))
        self._properties["ports"] = cleaned

    def __enter__(self) -> "NetworkPolicyIngressRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyList(_kuber_definitions.Collection):
    """
    NetworkPolicyList is a list of NetworkPolicy objects.
    """

    def __init__(
        self,
        items: typing.List["NetworkPolicy"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create NetworkPolicyList instance."""
        super(NetworkPolicyList, self).__init__(
            api_version="networking/v1", kind="NetworkPolicyList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, NetworkPolicy),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["NetworkPolicy"]:
        """
        Items is a list of schema objects.
        """
        return typing.cast(
            typing.List["NetworkPolicy"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["NetworkPolicy"], typing.List[dict]]
    ):
        """
        Items is a list of schema objects.
        """
        cleaned: typing.List[NetworkPolicy] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NetworkPolicy,
                    NetworkPolicy().from_dict(item),
                )
            cleaned.append(typing.cast(NetworkPolicy, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ListMeta,
                ListMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @staticmethod
    def get_resource_api(
        api_client: client.ApiClient = None, **kwargs
    ) -> "client.NetworkingV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1Api(**kwargs)

    def __enter__(self) -> "NetworkPolicyList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkPolicyPeer(_kuber_definitions.Definition):
    """
    NetworkPolicyPeer describes a peer to allow traffic to/from.
    Only certain combinations of fields are allowed
    """

    def __init__(
        self,
        ip_block: "IPBlock" = None,
        namespace_selector: "LabelSelector" = None,
        pod_selector: "LabelSelector" = None,
    ):
        """Create NetworkPolicyPeer instance."""
        super(NetworkPolicyPeer, self).__init__(
            api_version="networking/v1", kind="NetworkPolicyPeer"
        )
        self._properties = {
            "ipBlock": ip_block if ip_block is not None else IPBlock(),
            "namespaceSelector": namespace_selector
            if namespace_selector is not None
            else LabelSelector(),
            "podSelector": pod_selector
            if pod_selector is not None
            else LabelSelector(),
        }
        self._types = {
            "ipBlock": (IPBlock, None),
            "namespaceSelector": (LabelSelector, None),
            "podSelector": (LabelSelector, None),
        }

    @property
    def ip_block(self) -> "IPBlock":
        """
        IPBlock defines policy on a particular IPBlock. If this
        field is set then neither of the other fields can be.
        """
        return typing.cast(
            "IPBlock",
            self._properties.get("ipBlock"),
        )

    @ip_block.setter
    def ip_block(self, value: typing.Union["IPBlock", dict]):
        """
        IPBlock defines policy on a particular IPBlock. If this
        field is set then neither of the other fields can be.
        """
        if isinstance(value, dict):
            value = typing.cast(
                IPBlock,
                IPBlock().from_dict(value),
            )
        self._properties["ipBlock"] = value

    @property
    def namespace_selector(self) -> "LabelSelector":
        """
        Selects Namespaces using cluster-scoped labels. This field
        follows standard label selector semantics; if present but
        empty, it selects all namespaces.

        If PodSelector is also set, then the NetworkPolicyPeer as a
        whole selects the Pods matching PodSelector in the
        Namespaces selected by NamespaceSelector. Otherwise it
        selects all Pods in the Namespaces selected by
        NamespaceSelector.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("namespaceSelector"),
        )

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        Selects Namespaces using cluster-scoped labels. This field
        follows standard label selector semantics; if present but
        empty, it selects all namespaces.

        If PodSelector is also set, then the NetworkPolicyPeer as a
        whole selects the Pods matching PodSelector in the
        Namespaces selected by NamespaceSelector. Otherwise it
        selects all Pods in the Namespaces selected by
        NamespaceSelector.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["namespaceSelector"] = value

    @property
    def pod_selector(self) -> "LabelSelector":
        """
        This is a label selector which selects Pods. This field
        follows standard label selector semantics; if present but
        empty, it selects all pods.

        If NamespaceSelector is also set, then the NetworkPolicyPeer
        as a whole selects the Pods matching PodSelector in the
        Namespaces selected by NamespaceSelector. Otherwise it
        selects the Pods matching PodSelector in the policy's own
        Namespace.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("podSelector"),
        )

    @pod_selector.setter
    def pod_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        This is a label selector which selects Pods. This field
        follows standard label selector semantics; if present but
        empty, it selects all pods.

        If NamespaceSelector is also set, then the NetworkPolicyPeer
        as a whole selects the Pods matching PodSelector in the
        Namespaces selected by NamespaceSelector. Otherwise it
        selects the Pods matching PodSelector in the policy's own
        Namespace.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["podSelector"] = value

    def __enter__(self) -> "NetworkPolicyPeer":
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
            api_version="networking/v1", kind="NetworkPolicyPort"
        )
        self._properties = {
            "port": port if port is not None else None,
            "protocol": protocol if protocol is not None else "",
        }
        self._types = {
            "port": (int, None),
            "protocol": (str, None),
        }

    @property
    def port(self) -> typing.Optional[int]:
        """
        The port on the given protocol. This can either be a
        numerical or named port on a pod. If this field is not
        provided, this matches all port names and numbers.
        """
        value = self._properties.get("port")
        return int(value) if value is not None else None

    @port.setter
    def port(self, value: typing.Union[str, int, None]):
        """
        The port on the given protocol. This can either be a
        numerical or named port on a pod. If this field is not
        provided, this matches all port names and numbers.
        """
        self._properties["port"] = None if value is None else f"{value}"

    @property
    def protocol(self) -> str:
        """
        The protocol (TCP, UDP, or SCTP) which traffic must match.
        If not specified, this field defaults to TCP.
        """
        return typing.cast(
            str,
            self._properties.get("protocol"),
        )

    @protocol.setter
    def protocol(self, value: str):
        """
        The protocol (TCP, UDP, or SCTP) which traffic must match.
        If not specified, this field defaults to TCP.
        """
        self._properties["protocol"] = value

    def __enter__(self) -> "NetworkPolicyPort":
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
        egress: typing.List["NetworkPolicyEgressRule"] = None,
        ingress: typing.List["NetworkPolicyIngressRule"] = None,
        pod_selector: "LabelSelector" = None,
        policy_types: typing.List[str] = None,
    ):
        """Create NetworkPolicySpec instance."""
        super(NetworkPolicySpec, self).__init__(
            api_version="networking/v1", kind="NetworkPolicySpec"
        )
        self._properties = {
            "egress": egress if egress is not None else [],
            "ingress": ingress if ingress is not None else [],
            "podSelector": pod_selector
            if pod_selector is not None
            else LabelSelector(),
            "policyTypes": policy_types if policy_types is not None else [],
        }
        self._types = {
            "egress": (list, NetworkPolicyEgressRule),
            "ingress": (list, NetworkPolicyIngressRule),
            "podSelector": (LabelSelector, None),
            "policyTypes": (list, str),
        }

    @property
    def egress(self) -> typing.List["NetworkPolicyEgressRule"]:
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
        return typing.cast(
            typing.List["NetworkPolicyEgressRule"],
            self._properties.get("egress"),
        )

    @egress.setter
    def egress(
        self,
        value: typing.Union[typing.List["NetworkPolicyEgressRule"], typing.List[dict]],
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
        cleaned: typing.List[NetworkPolicyEgressRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NetworkPolicyEgressRule,
                    NetworkPolicyEgressRule().from_dict(item),
                )
            cleaned.append(typing.cast(NetworkPolicyEgressRule, item))
        self._properties["egress"] = cleaned

    @property
    def ingress(self) -> typing.List["NetworkPolicyIngressRule"]:
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
        return typing.cast(
            typing.List["NetworkPolicyIngressRule"],
            self._properties.get("ingress"),
        )

    @ingress.setter
    def ingress(
        self,
        value: typing.Union[typing.List["NetworkPolicyIngressRule"], typing.List[dict]],
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
        cleaned: typing.List[NetworkPolicyIngressRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NetworkPolicyIngressRule,
                    NetworkPolicyIngressRule().from_dict(item),
                )
            cleaned.append(typing.cast(NetworkPolicyIngressRule, item))
        self._properties["ingress"] = cleaned

    @property
    def pod_selector(self) -> "LabelSelector":
        """
        Selects the pods to which this NetworkPolicy object applies.
        The array of ingress rules is applied to any pods selected
        by this field. Multiple network policies can select the same
        set of pods. In this case, the ingress rules for each are
        combined additively. This field is NOT optional and follows
        standard label selector semantics. An empty podSelector
        matches all pods in this namespace.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("podSelector"),
        )

    @pod_selector.setter
    def pod_selector(self, value: typing.Union["LabelSelector", dict]):
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
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["podSelector"] = value

    @property
    def policy_types(self) -> typing.List[str]:
        """
        List of rule types that the NetworkPolicy relates to. Valid
        options are "Ingress", "Egress", or "Ingress,Egress". If
        this field is not specified, it will default based on the
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
        return typing.cast(
            typing.List[str],
            self._properties.get("policyTypes"),
        )

    @policy_types.setter
    def policy_types(self, value: typing.List[str]):
        """
        List of rule types that the NetworkPolicy relates to. Valid
        options are "Ingress", "Egress", or "Ingress,Egress". If
        this field is not specified, it will default based on the
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
        self._properties["policyTypes"] = value

    def __enter__(self) -> "NetworkPolicySpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceBackendPort(_kuber_definitions.Definition):
    """
    ServiceBackendPort is the service port being referenced.
    """

    def __init__(
        self,
        name: str = None,
        number: int = None,
    ):
        """Create ServiceBackendPort instance."""
        super(ServiceBackendPort, self).__init__(
            api_version="networking/v1", kind="ServiceBackendPort"
        )
        self._properties = {
            "name": name if name is not None else "",
            "number": number if number is not None else None,
        }
        self._types = {
            "name": (str, None),
            "number": (int, None),
        }

    @property
    def name(self) -> str:
        """
        Name is the name of the port on the Service. This is a
        mutually exclusive setting with "Number".
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the port on the Service. This is a
        mutually exclusive setting with "Number".
        """
        self._properties["name"] = value

    @property
    def number(self) -> int:
        """
        Number is the numerical port number (e.g. 80) on the
        Service. This is a mutually exclusive setting with "Name".
        """
        return typing.cast(
            int,
            self._properties.get("number"),
        )

    @number.setter
    def number(self, value: int):
        """
        Number is the numerical port number (e.g. 80) on the
        Service. This is a mutually exclusive setting with "Name".
        """
        self._properties["number"] = value

    def __enter__(self) -> "ServiceBackendPort":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
