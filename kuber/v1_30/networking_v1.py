import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_30.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_30.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_30.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_30.meta_v1 import Status  # noqa: F401
from kuber.v1_30.meta_v1 import StatusDetails  # noqa: F401
from kuber.v1_30.core_v1 import TypedLocalObjectReference  # noqa: F401


class HTTPIngressPath(_kuber_definitions.Definition):
    """
    HTTPIngressPath associates a path with a backend. Incoming
    urls matching the path are forwarded to the backend.
    """

    def __init__(
        self,
        backend: typing.Optional["IngressBackend"] = None,
        path: typing.Optional[str] = None,
        path_type: typing.Optional[str] = None,
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
        backend defines the referenced service endpoint to which the
        traffic will be forwarded to.
        """
        return typing.cast(
            "IngressBackend",
            self._properties.get("backend"),
        )

    @backend.setter
    def backend(self, value: typing.Union["IngressBackend", dict]):
        """
        backend defines the referenced service endpoint to which the
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
        path is matched against the path of an incoming request.
        Currently it can contain characters disallowed from the
        conventional "path" part of a URL as defined by RFC 3986.
        Paths must begin with a '/' and must be present when using
        PathType with value "Exact" or "Prefix".
        """
        return typing.cast(
            str,
            self._properties.get("path"),
        )

    @path.setter
    def path(self, value: str):
        """
        path is matched against the path of an incoming request.
        Currently it can contain characters disallowed from the
        conventional "path" part of a URL as defined by RFC 3986.
        Paths must begin with a '/' and must be present when using
        PathType with value "Exact" or "Prefix".
        """
        self._properties["path"] = value

    @property
    def path_type(self) -> str:
        """
        pathType determines the interpretation of the path matching.
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
        pathType determines the interpretation of the path matching.
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
        paths: typing.Optional[typing.List["HTTPIngressPath"]] = None,
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
        paths is a collection of paths that map requests to
        backends.
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
        paths is a collection of paths that map requests to
        backends.
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
    "192.168.1.0/24","2001:db8::/64") that is allowed to the
    pods matched by a NetworkPolicySpec's podSelector. The
    except entry describes CIDRs that should not be included
    within this rule.
    """

    def __init__(
        self,
        cidr: typing.Optional[str] = None,
        except_: typing.Optional[typing.List[str]] = None,
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
        cidr is a string representing the IPBlock Valid examples are
        "192.168.1.0/24" or "2001:db8::/64"
        """
        return typing.cast(
            str,
            self._properties.get("cidr"),
        )

    @cidr.setter
    def cidr(self, value: str):
        """
        cidr is a string representing the IPBlock Valid examples are
        "192.168.1.0/24" or "2001:db8::/64"
        """
        self._properties["cidr"] = value

    @property
    def except_(self) -> typing.List[str]:
        """
        except is a slice of CIDRs that should not be included
        within an IPBlock Valid examples are "192.168.1.0/24" or
        "2001:db8::/64" Except values will be rejected if they are
        outside the cidr range
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("except"),
        )

    @except_.setter
    def except_(self, value: typing.List[str]):
        """
        except is a slice of CIDRs that should not be included
        within an IPBlock Valid examples are "192.168.1.0/24" or
        "2001:db8::/64" Except values will be rejected if they are
        outside the cidr range
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
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["IngressSpec"] = None,
        status: typing.Optional["IngressStatus"] = None,
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
        spec is the desired state of the Ingress. More info:
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
        spec is the desired state of the Ingress. More info:
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
        status is the current state of the Ingress. More info:
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
        status is the current state of the Ingress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressStatus,
                IngressStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "IngressStatus":
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

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "IngressStatus":
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

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "IngressStatus":
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

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "IngressStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_ingress",
            "read_ingress",
        ]

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

    def read_resource(self, namespace: typing.Optional[str] = None):
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
        namespace: typing.Optional[str] = None,
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
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
        resource: typing.Optional["TypedLocalObjectReference"] = None,
        service: typing.Optional["IngressServiceBackend"] = None,
    ):
        """Create IngressBackend instance."""
        super(IngressBackend, self).__init__(
            api_version="networking/v1", kind="IngressBackend"
        )
        self._properties = {
            "resource": (
                resource if resource is not None else TypedLocalObjectReference()
            ),
            "service": service if service is not None else IngressServiceBackend(),
        }
        self._types = {
            "resource": (TypedLocalObjectReference, None),
            "service": (IngressServiceBackend, None),
        }

    @property
    def resource(self) -> "TypedLocalObjectReference":
        """
        resource is an ObjectRef to another Kubernetes resource in
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
        resource is an ObjectRef to another Kubernetes resource in
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
        service references a service as a backend. This is a
        mutually exclusive setting with "Resource".
        """
        return typing.cast(
            "IngressServiceBackend",
            self._properties.get("service"),
        )

    @service.setter
    def service(self, value: typing.Union["IngressServiceBackend", dict]):
        """
        service references a service as a backend. This is a
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
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["IngressClassSpec"] = None,
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
        spec is the desired state of the IngressClass. More info:
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
        spec is the desired state of the IngressClass. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressClassSpec,
                IngressClassSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
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

    def replace_resource(self, namespace: typing.Optional["str"] = None):
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

    def patch_resource(self, namespace: typing.Optional["str"] = None):
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

    def get_resource_status(self, namespace: typing.Optional["str"] = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: typing.Optional[str] = None):
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
        namespace: typing.Optional[str] = None,
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
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
        items: typing.Optional[typing.List["IngressClass"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
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
        items is the list of IngressClasses.
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
        items is the list of IngressClasses.
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
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


class IngressClassParametersReference(_kuber_definitions.Definition):
    """
    IngressClassParametersReference identifies an API object.
    This can be used to specify a cluster or namespace-scoped
    resource.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
    ):
        """Create IngressClassParametersReference instance."""
        super(IngressClassParametersReference, self).__init__(
            api_version="networking/v1", kind="IngressClassParametersReference"
        )
        self._properties = {
            "apiGroup": api_group if api_group is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "scope": scope if scope is not None else "",
        }
        self._types = {
            "apiGroup": (str, None),
            "kind": (str, None),
            "name": (str, None),
            "namespace": (str, None),
            "scope": (str, None),
        }

    @property
    def api_group(self) -> str:
        """
        apiGroup is the group for the resource being referenced. If
        APIGroup is not specified, the specified Kind must be in the
        core API group. For any other third-party types, APIGroup is
        required.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        apiGroup is the group for the resource being referenced. If
        APIGroup is not specified, the specified Kind must be in the
        core API group. For any other third-party types, APIGroup is
        required.
        """
        self._properties["apiGroup"] = value

    @property
    def kind(self) -> str:
        """
        kind is the type of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        kind is the type of resource being referenced.
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        name is the name of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of resource being referenced.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        namespace is the namespace of the resource being referenced.
        This field is required when scope is set to "Namespace" and
        must be unset when scope is set to "Cluster".
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        namespace is the namespace of the resource being referenced.
        This field is required when scope is set to "Namespace" and
        must be unset when scope is set to "Cluster".
        """
        self._properties["namespace"] = value

    @property
    def scope(self) -> str:
        """
        scope represents if this refers to a cluster or namespace
        scoped resource. This may be set to "Cluster" (default) or
        "Namespace".
        """
        return typing.cast(
            str,
            self._properties.get("scope"),
        )

    @scope.setter
    def scope(self, value: str):
        """
        scope represents if this refers to a cluster or namespace
        scoped resource. This may be set to "Cluster" (default) or
        "Namespace".
        """
        self._properties["scope"] = value

    def __enter__(self) -> "IngressClassParametersReference":
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
        controller: typing.Optional[str] = None,
        parameters: typing.Optional["IngressClassParametersReference"] = None,
    ):
        """Create IngressClassSpec instance."""
        super(IngressClassSpec, self).__init__(
            api_version="networking/v1", kind="IngressClassSpec"
        )
        self._properties = {
            "controller": controller if controller is not None else "",
            "parameters": (
                parameters
                if parameters is not None
                else IngressClassParametersReference()
            ),
        }
        self._types = {
            "controller": (str, None),
            "parameters": (IngressClassParametersReference, None),
        }

    @property
    def controller(self) -> str:
        """
        controller refers to the name of the controller that should
        handle this class. This allows for different "flavors" that
        are controlled by the same controller. For example, you may
        have different parameters for the same implementing
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
        controller refers to the name of the controller that should
        handle this class. This allows for different "flavors" that
        are controlled by the same controller. For example, you may
        have different parameters for the same implementing
        controller. This should be specified as a domain-prefixed
        path no more than 250 characters in length, e.g.
        "acme.io/ingress-controller". This field is immutable.
        """
        self._properties["controller"] = value

    @property
    def parameters(self) -> "IngressClassParametersReference":
        """
        parameters is a link to a custom resource containing
        additional configuration for the controller. This is
        optional if the controller does not require extra
        parameters.
        """
        return typing.cast(
            "IngressClassParametersReference",
            self._properties.get("parameters"),
        )

    @parameters.setter
    def parameters(self, value: typing.Union["IngressClassParametersReference", dict]):
        """
        parameters is a link to a custom resource containing
        additional configuration for the controller. This is
        optional if the controller does not require extra
        parameters.
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressClassParametersReference,
                IngressClassParametersReference().from_dict(value),
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
        items: typing.Optional[typing.List["Ingress"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
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
        items is the list of Ingress.
        """
        return typing.cast(
            typing.List["Ingress"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["Ingress"], typing.List[dict]]):
        """
        items is the list of Ingress.
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
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


class IngressLoadBalancerIngress(_kuber_definitions.Definition):
    """
    IngressLoadBalancerIngress represents the status of a load-
    balancer ingress point.
    """

    def __init__(
        self,
        hostname: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        ports: typing.Optional[typing.List["IngressPortStatus"]] = None,
    ):
        """Create IngressLoadBalancerIngress instance."""
        super(IngressLoadBalancerIngress, self).__init__(
            api_version="networking/v1", kind="IngressLoadBalancerIngress"
        )
        self._properties = {
            "hostname": hostname if hostname is not None else "",
            "ip": ip if ip is not None else "",
            "ports": ports if ports is not None else [],
        }
        self._types = {
            "hostname": (str, None),
            "ip": (str, None),
            "ports": (list, IngressPortStatus),
        }

    @property
    def hostname(self) -> str:
        """
        hostname is set for load-balancer ingress points that are
        DNS based.
        """
        return typing.cast(
            str,
            self._properties.get("hostname"),
        )

    @hostname.setter
    def hostname(self, value: str):
        """
        hostname is set for load-balancer ingress points that are
        DNS based.
        """
        self._properties["hostname"] = value

    @property
    def ip(self) -> str:
        """
        ip is set for load-balancer ingress points that are IP
        based.
        """
        return typing.cast(
            str,
            self._properties.get("ip"),
        )

    @ip.setter
    def ip(self, value: str):
        """
        ip is set for load-balancer ingress points that are IP
        based.
        """
        self._properties["ip"] = value

    @property
    def ports(self) -> typing.List["IngressPortStatus"]:
        """
        ports provides information about the ports exposed by this
        LoadBalancer.
        """
        return typing.cast(
            typing.List["IngressPortStatus"],
            self._properties.get("ports"),
        )

    @ports.setter
    def ports(
        self, value: typing.Union[typing.List["IngressPortStatus"], typing.List[dict]]
    ):
        """
        ports provides information about the ports exposed by this
        LoadBalancer.
        """
        cleaned: typing.List[IngressPortStatus] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    IngressPortStatus,
                    IngressPortStatus().from_dict(item),
                )
            cleaned.append(typing.cast(IngressPortStatus, item))
        self._properties["ports"] = cleaned

    def __enter__(self) -> "IngressLoadBalancerIngress":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressLoadBalancerStatus(_kuber_definitions.Definition):
    """
    IngressLoadBalancerStatus represents the status of a load-
    balancer.
    """

    def __init__(
        self,
        ingress: typing.Optional[typing.List["IngressLoadBalancerIngress"]] = None,
    ):
        """Create IngressLoadBalancerStatus instance."""
        super(IngressLoadBalancerStatus, self).__init__(
            api_version="networking/v1", kind="IngressLoadBalancerStatus"
        )
        self._properties = {
            "ingress": ingress if ingress is not None else [],
        }
        self._types = {
            "ingress": (list, IngressLoadBalancerIngress),
        }

    @property
    def ingress(self) -> typing.List["IngressLoadBalancerIngress"]:
        """
        ingress is a list containing ingress points for the load-
        balancer.
        """
        return typing.cast(
            typing.List["IngressLoadBalancerIngress"],
            self._properties.get("ingress"),
        )

    @ingress.setter
    def ingress(
        self,
        value: typing.Union[
            typing.List["IngressLoadBalancerIngress"], typing.List[dict]
        ],
    ):
        """
        ingress is a list containing ingress points for the load-
        balancer.
        """
        cleaned: typing.List[IngressLoadBalancerIngress] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    IngressLoadBalancerIngress,
                    IngressLoadBalancerIngress().from_dict(item),
                )
            cleaned.append(typing.cast(IngressLoadBalancerIngress, item))
        self._properties["ingress"] = cleaned

    def __enter__(self) -> "IngressLoadBalancerStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressPortStatus(_kuber_definitions.Definition):
    """
    IngressPortStatus represents the error condition of a
    service port
    """

    def __init__(
        self,
        error: typing.Optional[str] = None,
        port: typing.Optional[int] = None,
        protocol: typing.Optional[str] = None,
    ):
        """Create IngressPortStatus instance."""
        super(IngressPortStatus, self).__init__(
            api_version="networking/v1", kind="IngressPortStatus"
        )
        self._properties = {
            "error": error if error is not None else "",
            "port": port if port is not None else None,
            "protocol": protocol if protocol is not None else "",
        }
        self._types = {
            "error": (str, None),
            "port": (int, None),
            "protocol": (str, None),
        }

    @property
    def error(self) -> str:
        """
        error is to record the problem with the service port The
        format of the error shall comply with the following rules: -
        built-in error values shall be specified in this file and
        those shall use
          CamelCase names
        - cloud provider specific error values must have names that
        comply with the
          format foo.example.com/CamelCase.
        """
        return typing.cast(
            str,
            self._properties.get("error"),
        )

    @error.setter
    def error(self, value: str):
        """
        error is to record the problem with the service port The
        format of the error shall comply with the following rules: -
        built-in error values shall be specified in this file and
        those shall use
          CamelCase names
        - cloud provider specific error values must have names that
        comply with the
          format foo.example.com/CamelCase.
        """
        self._properties["error"] = value

    @property
    def port(self) -> int:
        """
        port is the port number of the ingress port.
        """
        return typing.cast(
            int,
            self._properties.get("port"),
        )

    @port.setter
    def port(self, value: int):
        """
        port is the port number of the ingress port.
        """
        self._properties["port"] = value

    @property
    def protocol(self) -> str:
        """
        protocol is the protocol of the ingress port. The supported
        values are: "TCP", "UDP", "SCTP"
        """
        return typing.cast(
            str,
            self._properties.get("protocol"),
        )

    @protocol.setter
    def protocol(self, value: str):
        """
        protocol is the protocol of the ingress port. The supported
        values are: "TCP", "UDP", "SCTP"
        """
        self._properties["protocol"] = value

    def __enter__(self) -> "IngressPortStatus":
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
        host: typing.Optional[str] = None,
        http: typing.Optional["HTTPIngressRuleValue"] = None,
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
        host is the fully qualified domain name of a network host,
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

        host can be "precise" which is a domain name without the
        terminating dot of a network host (e.g. "foo.bar.com") or
        "wildcard", which is a domain name prefixed with a single
        wildcard label (e.g. "*.foo.com"). The wildcard character
        '*' must appear by itself as the first DNS label and matches
        only a single label. You cannot have a wildcard label by
        itself (e.g. Host == "*"). Requests will be matched against
        the Host field in the following way: 1. If host is precise,
        the request matches this rule if the http host header is
        equal to Host. 2. If host is a wildcard, then the request
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
        host is the fully qualified domain name of a network host,
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

        host can be "precise" which is a domain name without the
        terminating dot of a network host (e.g. "foo.bar.com") or
        "wildcard", which is a domain name prefixed with a single
        wildcard label (e.g. "*.foo.com"). The wildcard character
        '*' must appear by itself as the first DNS label and matches
        only a single label. You cannot have a wildcard label by
        itself (e.g. Host == "*"). Requests will be matched against
        the Host field in the following way: 1. If host is precise,
        the request matches this rule if the http host header is
        equal to Host. 2. If host is a wildcard, then the request
        matches this rule if the http host header is to equal to the
        suffix (removing the first label) of the wildcard rule.
        """
        self._properties["host"] = value

    @property
    def http(self) -> "HTTPIngressRuleValue":
        """ """
        return typing.cast(
            "HTTPIngressRuleValue",
            self._properties.get("http"),
        )

    @http.setter
    def http(self, value: typing.Union["HTTPIngressRuleValue", dict]):
        """ """
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
        name: typing.Optional[str] = None,
        port: typing.Optional["ServiceBackendPort"] = None,
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
        name is the referenced service. The service must exist in
        the same namespace as the Ingress object.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the referenced service. The service must exist in
        the same namespace as the Ingress object.
        """
        self._properties["name"] = value

    @property
    def port(self) -> "ServiceBackendPort":
        """
        port of the referenced service. A port name or port number
        is required for a IngressServiceBackend.
        """
        return typing.cast(
            "ServiceBackendPort",
            self._properties.get("port"),
        )

    @port.setter
    def port(self, value: typing.Union["ServiceBackendPort", dict]):
        """
        port of the referenced service. A port name or port number
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
        default_backend: typing.Optional["IngressBackend"] = None,
        ingress_class_name: typing.Optional[str] = None,
        rules: typing.Optional[typing.List["IngressRule"]] = None,
        tls: typing.Optional[typing.List["IngressTLS"]] = None,
    ):
        """Create IngressSpec instance."""
        super(IngressSpec, self).__init__(
            api_version="networking/v1", kind="IngressSpec"
        )
        self._properties = {
            "defaultBackend": (
                default_backend if default_backend is not None else IngressBackend()
            ),
            "ingressClassName": (
                ingress_class_name if ingress_class_name is not None else ""
            ),
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
        defaultBackend is the backend that should handle requests
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
        defaultBackend is the backend that should handle requests
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
        ingressClassName is the name of an IngressClass cluster
        resource. Ingress controller implementations use this field
        to know whether they should be serving this Ingress
        resource, by a transitive connection (controller ->
        IngressClass -> Ingress resource). Although the
        `kubernetes.io/ingress.class` annotation (simple constant
        name) was never formally defined, it was widely supported by
        Ingress controllers to create a direct binding between
        Ingress controller and Ingress resources. Newly created
        Ingress resources should prefer using the field. However,
        even though the annotation is officially deprecated, for
        backwards compatibility reasons, ingress controllers should
        still honor that annotation if present.
        """
        return typing.cast(
            str,
            self._properties.get("ingressClassName"),
        )

    @ingress_class_name.setter
    def ingress_class_name(self, value: str):
        """
        ingressClassName is the name of an IngressClass cluster
        resource. Ingress controller implementations use this field
        to know whether they should be serving this Ingress
        resource, by a transitive connection (controller ->
        IngressClass -> Ingress resource). Although the
        `kubernetes.io/ingress.class` annotation (simple constant
        name) was never formally defined, it was widely supported by
        Ingress controllers to create a direct binding between
        Ingress controller and Ingress resources. Newly created
        Ingress resources should prefer using the field. However,
        even though the annotation is officially deprecated, for
        backwards compatibility reasons, ingress controllers should
        still honor that annotation if present.
        """
        self._properties["ingressClassName"] = value

    @property
    def rules(self) -> typing.List["IngressRule"]:
        """
        rules is a list of host rules used to configure the Ingress.
        If unspecified, or no rule matches, all traffic is sent to
        the default backend.
        """
        return typing.cast(
            typing.List["IngressRule"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(self, value: typing.Union[typing.List["IngressRule"], typing.List[dict]]):
        """
        rules is a list of host rules used to configure the Ingress.
        If unspecified, or no rule matches, all traffic is sent to
        the default backend.
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
        tls represents the TLS configuration. Currently the Ingress
        only supports a single TLS port, 443. If multiple members of
        this list specify different hosts, they will be multiplexed
        on the same port according to the hostname specified through
        the SNI TLS extension, if the ingress controller fulfilling
        the ingress supports SNI.
        """
        return typing.cast(
            typing.List["IngressTLS"],
            self._properties.get("tls"),
        )

    @tls.setter
    def tls(self, value: typing.Union[typing.List["IngressTLS"], typing.List[dict]]):
        """
        tls represents the TLS configuration. Currently the Ingress
        only supports a single TLS port, 443. If multiple members of
        this list specify different hosts, they will be multiplexed
        on the same port according to the hostname specified through
        the SNI TLS extension, if the ingress controller fulfilling
        the ingress supports SNI.
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
        load_balancer: typing.Optional["IngressLoadBalancerStatus"] = None,
    ):
        """Create IngressStatus instance."""
        super(IngressStatus, self).__init__(
            api_version="networking/v1", kind="IngressStatus"
        )
        self._properties = {
            "loadBalancer": (
                load_balancer
                if load_balancer is not None
                else IngressLoadBalancerStatus()
            ),
        }
        self._types = {
            "loadBalancer": (IngressLoadBalancerStatus, None),
        }

    @property
    def load_balancer(self) -> "IngressLoadBalancerStatus":
        """
        loadBalancer contains the current status of the load-
        balancer.
        """
        return typing.cast(
            "IngressLoadBalancerStatus",
            self._properties.get("loadBalancer"),
        )

    @load_balancer.setter
    def load_balancer(self, value: typing.Union["IngressLoadBalancerStatus", dict]):
        """
        loadBalancer contains the current status of the load-
        balancer.
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressLoadBalancerStatus,
                IngressLoadBalancerStatus().from_dict(value),
            )
        self._properties["loadBalancer"] = value

    def __enter__(self) -> "IngressStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IngressTLS(_kuber_definitions.Definition):
    """
    IngressTLS describes the transport layer security associated
    with an ingress.
    """

    def __init__(
        self,
        hosts: typing.Optional[typing.List[str]] = None,
        secret_name: typing.Optional[str] = None,
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
        hosts is a list of hosts included in the TLS certificate.
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
        hosts is a list of hosts included in the TLS certificate.
        The values in this list must match the name/s used in the
        tlsSecret. Defaults to the wildcard host setting for the
        loadbalancer controller fulfilling this Ingress, if left
        unspecified.
        """
        self._properties["hosts"] = value

    @property
    def secret_name(self) -> str:
        """
        secretName is the name of the secret used to terminate TLS
        traffic on port 443. Field is left optional to allow TLS
        routing based on SNI hostname alone. If the SNI host in a
        listener conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the "Host" header is used for routing.
        """
        return typing.cast(
            str,
            self._properties.get("secretName"),
        )

    @secret_name.setter
    def secret_name(self, value: str):
        """
        secretName is the name of the secret used to terminate TLS
        traffic on port 443. Field is left optional to allow TLS
        routing based on SNI hostname alone. If the SNI host in a
        listener conflicts with the "Host" header field used by an
        IngressRule, the SNI host is used for termination and value
        of the "Host" header is used for routing.
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
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["NetworkPolicySpec"] = None,
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
        spec represents the specification of the desired behavior
        for this NetworkPolicy.
        """
        return typing.cast(
            "NetworkPolicySpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["NetworkPolicySpec", dict]):
        """
        spec represents the specification of the desired behavior
        for this NetworkPolicy.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NetworkPolicySpec,
                NetworkPolicySpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
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

    def replace_resource(self, namespace: typing.Optional["str"] = None):
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

    def patch_resource(self, namespace: typing.Optional["str"] = None):
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

    def get_resource_status(self, namespace: typing.Optional["str"] = None):
        """This resource does not have a status."""
        pass

    def read_resource(self, namespace: typing.Optional[str] = None):
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
        namespace: typing.Optional[str] = None,
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
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
        ports: typing.Optional[typing.List["NetworkPolicyPort"]] = None,
        to: typing.Optional[typing.List["NetworkPolicyPeer"]] = None,
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
        ports is a list of destination ports for outgoing traffic.
        Each item in this list is combined using a logical OR. If
        this field is empty or missing, this rule matches all ports
        (traffic not restricted by port). If this field is present
        and contains at least one item, then this rule allows
        traffic only if the traffic matches at least one port in the
        list.
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
        ports is a list of destination ports for outgoing traffic.
        Each item in this list is combined using a logical OR. If
        this field is empty or missing, this rule matches all ports
        (traffic not restricted by port). If this field is present
        and contains at least one item, then this rule allows
        traffic only if the traffic matches at least one port in the
        list.
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
        to is a list of destinations for outgoing traffic of pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all destinations (traffic not
        restricted by destination). If this field is present and
        contains at least one item, this rule allows traffic only if
        the traffic matches at least one item in the to list.
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
        to is a list of destinations for outgoing traffic of pods
        selected for this rule. Items in this list are combined
        using a logical OR operation. If this field is empty or
        missing, this rule matches all destinations (traffic not
        restricted by destination). If this field is present and
        contains at least one item, this rule allows traffic only if
        the traffic matches at least one item in the to list.
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
        from_: typing.Optional[typing.List["NetworkPolicyPeer"]] = None,
        ports: typing.Optional[typing.List["NetworkPolicyPort"]] = None,
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
        from is a list of sources which should be able to access the
        pods selected for this rule. Items in this list are combined
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
        from is a list of sources which should be able to access the
        pods selected for this rule. Items in this list are combined
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
        ports is a list of ports which should be made accessible on
        the pods selected for this rule. Each item in this list is
        combined using a logical OR. If this field is empty or
        missing, this rule matches all ports (traffic not restricted
        by port). If this field is present and contains at least one
        item, then this rule allows traffic only if the traffic
        matches at least one port in the list.
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
        ports is a list of ports which should be made accessible on
        the pods selected for this rule. Each item in this list is
        combined using a logical OR. If this field is empty or
        missing, this rule matches all ports (traffic not restricted
        by port). If this field is present and contains at least one
        item, then this rule allows traffic only if the traffic
        matches at least one port in the list.
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
        items: typing.Optional[typing.List["NetworkPolicy"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
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
        items is a list of schema objects.
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
        items is a list of schema objects.
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
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
        ip_block: typing.Optional["IPBlock"] = None,
        namespace_selector: typing.Optional["LabelSelector"] = None,
        pod_selector: typing.Optional["LabelSelector"] = None,
    ):
        """Create NetworkPolicyPeer instance."""
        super(NetworkPolicyPeer, self).__init__(
            api_version="networking/v1", kind="NetworkPolicyPeer"
        )
        self._properties = {
            "ipBlock": ip_block if ip_block is not None else IPBlock(),
            "namespaceSelector": (
                namespace_selector
                if namespace_selector is not None
                else LabelSelector()
            ),
            "podSelector": (
                pod_selector if pod_selector is not None else LabelSelector()
            ),
        }
        self._types = {
            "ipBlock": (IPBlock, None),
            "namespaceSelector": (LabelSelector, None),
            "podSelector": (LabelSelector, None),
        }

    @property
    def ip_block(self) -> "IPBlock":
        """
        ipBlock defines policy on a particular IPBlock. If this
        field is set then neither of the other fields can be.
        """
        return typing.cast(
            "IPBlock",
            self._properties.get("ipBlock"),
        )

    @ip_block.setter
    def ip_block(self, value: typing.Union["IPBlock", dict]):
        """
        ipBlock defines policy on a particular IPBlock. If this
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
        namespaceSelector selects namespaces using cluster-scoped
        labels. This field follows standard label selector
        semantics; if present but empty, it selects all namespaces.

        If podSelector is also set, then the NetworkPolicyPeer as a
        whole selects the pods matching podSelector in the
        namespaces selected by namespaceSelector. Otherwise it
        selects all pods in the namespaces selected by
        namespaceSelector.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("namespaceSelector"),
        )

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        namespaceSelector selects namespaces using cluster-scoped
        labels. This field follows standard label selector
        semantics; if present but empty, it selects all namespaces.

        If podSelector is also set, then the NetworkPolicyPeer as a
        whole selects the pods matching podSelector in the
        namespaces selected by namespaceSelector. Otherwise it
        selects all pods in the namespaces selected by
        namespaceSelector.
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
        podSelector is a label selector which selects pods. This
        field follows standard label selector semantics; if present
        but empty, it selects all pods.

        If namespaceSelector is also set, then the NetworkPolicyPeer
        as a whole selects the pods matching podSelector in the
        Namespaces selected by NamespaceSelector. Otherwise it
        selects the pods matching podSelector in the policy's own
        namespace.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("podSelector"),
        )

    @pod_selector.setter
    def pod_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        podSelector is a label selector which selects pods. This
        field follows standard label selector semantics; if present
        but empty, it selects all pods.

        If namespaceSelector is also set, then the NetworkPolicyPeer
        as a whole selects the pods matching podSelector in the
        Namespaces selected by NamespaceSelector. Otherwise it
        selects the pods matching podSelector in the policy's own
        namespace.
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
        end_port: typing.Optional[int] = None,
        port: typing.Optional[typing.Union[str, int, None]] = None,
        protocol: typing.Optional[str] = None,
    ):
        """Create NetworkPolicyPort instance."""
        super(NetworkPolicyPort, self).__init__(
            api_version="networking/v1", kind="NetworkPolicyPort"
        )
        self._properties = {
            "endPort": end_port if end_port is not None else None,
            "port": port if port is not None else None,
            "protocol": protocol if protocol is not None else "",
        }
        self._types = {
            "endPort": (int, None),
            "port": (_types.integer_or_string, None),
            "protocol": (str, None),
        }

    @property
    def end_port(self) -> int:
        """
        endPort indicates that the range of ports from port to
        endPort if set, inclusive, should be allowed by the policy.
        This field cannot be defined if the port field is not
        defined or if the port field is defined as a named (string)
        port. The endPort must be equal or greater than port.
        """
        return typing.cast(
            int,
            self._properties.get("endPort"),
        )

    @end_port.setter
    def end_port(self, value: int):
        """
        endPort indicates that the range of ports from port to
        endPort if set, inclusive, should be allowed by the policy.
        This field cannot be defined if the port field is not
        defined or if the port field is defined as a named (string)
        port. The endPort must be equal or greater than port.
        """
        self._properties["endPort"] = value

    @property
    def port(self) -> typing.Union[str, int, None]:
        """
        port represents the port on the given protocol. This can
        either be a numerical or named port on a pod. If this field
        is not provided, this matches all port names and numbers. If
        present, only traffic on the specified protocol AND port
        will be matched.
        """
        return typing.cast(
            typing.Union[str, int, None],
            self._properties.get("port"),
        )

    @port.setter
    def port(self, value: typing.Union[str, int, None]):
        """
        port represents the port on the given protocol. This can
        either be a numerical or named port on a pod. If this field
        is not provided, this matches all port names and numbers. If
        present, only traffic on the specified protocol AND port
        will be matched.
        """
        self._properties["port"] = _types.integer_or_string(value)

    @property
    def protocol(self) -> str:
        """
        protocol represents the protocol (TCP, UDP, or SCTP) which
        traffic must match. If not specified, this field defaults to
        TCP.
        """
        return typing.cast(
            str,
            self._properties.get("protocol"),
        )

    @protocol.setter
    def protocol(self, value: str):
        """
        protocol represents the protocol (TCP, UDP, or SCTP) which
        traffic must match. If not specified, this field defaults to
        TCP.
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
        egress: typing.Optional[typing.List["NetworkPolicyEgressRule"]] = None,
        ingress: typing.Optional[typing.List["NetworkPolicyIngressRule"]] = None,
        pod_selector: typing.Optional["LabelSelector"] = None,
        policy_types: typing.Optional[typing.List[str]] = None,
    ):
        """Create NetworkPolicySpec instance."""
        super(NetworkPolicySpec, self).__init__(
            api_version="networking/v1", kind="NetworkPolicySpec"
        )
        self._properties = {
            "egress": egress if egress is not None else [],
            "ingress": ingress if ingress is not None else [],
            "podSelector": (
                pod_selector if pod_selector is not None else LabelSelector()
            ),
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
        egress is a list of egress rules to be applied to the
        selected pods. Outgoing traffic is allowed if there are no
        NetworkPolicies selecting the pod (and cluster policy
        otherwise allows the traffic), OR if the traffic matches at
        least one egress rule across all of the NetworkPolicy
        objects whose podSelector matches the pod. If this field is
        empty then this NetworkPolicy limits all outgoing traffic
        (and serves solely to ensure that the pods it selects are
        isolated by default). This field is beta-level in 1.8
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
        egress is a list of egress rules to be applied to the
        selected pods. Outgoing traffic is allowed if there are no
        NetworkPolicies selecting the pod (and cluster policy
        otherwise allows the traffic), OR if the traffic matches at
        least one egress rule across all of the NetworkPolicy
        objects whose podSelector matches the pod. If this field is
        empty then this NetworkPolicy limits all outgoing traffic
        (and serves solely to ensure that the pods it selects are
        isolated by default). This field is beta-level in 1.8
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
        ingress is a list of ingress rules to be applied to the
        selected pods. Traffic is allowed to a pod if there are no
        NetworkPolicies selecting the pod (and cluster policy
        otherwise allows the traffic), OR if the traffic source is
        the pod's local node, OR if the traffic matches at least one
        ingress rule across all of the NetworkPolicy objects whose
        podSelector matches the pod. If this field is empty then
        this NetworkPolicy does not allow any traffic (and serves
        solely to ensure that the pods it selects are isolated by
        default)
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
        ingress is a list of ingress rules to be applied to the
        selected pods. Traffic is allowed to a pod if there are no
        NetworkPolicies selecting the pod (and cluster policy
        otherwise allows the traffic), OR if the traffic source is
        the pod's local node, OR if the traffic matches at least one
        ingress rule across all of the NetworkPolicy objects whose
        podSelector matches the pod. If this field is empty then
        this NetworkPolicy does not allow any traffic (and serves
        solely to ensure that the pods it selects are isolated by
        default)
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
        podSelector selects the pods to which this NetworkPolicy
        object applies. The array of ingress rules is applied to any
        pods selected by this field. Multiple network policies can
        select the same set of pods. In this case, the ingress rules
        for each are combined additively. This field is NOT optional
        and follows standard label selector semantics. An empty
        podSelector matches all pods in this namespace.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("podSelector"),
        )

    @pod_selector.setter
    def pod_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        podSelector selects the pods to which this NetworkPolicy
        object applies. The array of ingress rules is applied to any
        pods selected by this field. Multiple network policies can
        select the same set of pods. In this case, the ingress rules
        for each are combined additively. This field is NOT optional
        and follows standard label selector semantics. An empty
        podSelector matches all pods in this namespace.
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
        policyTypes is a list of rule types that the NetworkPolicy
        relates to. Valid options are ["Ingress"], ["Egress"], or
        ["Ingress", "Egress"]. If this field is not specified, it
        will default based on the existence of ingress or egress
        rules; policies that contain an egress section are assumed
        to affect egress, and all policies (whether or not they
        contain an ingress section) are assumed to affect ingress.
        If you want to write an egress-only policy, you must
        explicitly specify policyTypes [ "Egress" ]. Likewise, if
        you want to write a policy that specifies that no egress is
        allowed, you must specify a policyTypes value that include
        "Egress" (since such a policy would not include an egress
        section and would otherwise default to just [ "Ingress" ]).
        This field is beta-level in 1.8
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("policyTypes"),
        )

    @policy_types.setter
    def policy_types(self, value: typing.List[str]):
        """
        policyTypes is a list of rule types that the NetworkPolicy
        relates to. Valid options are ["Ingress"], ["Egress"], or
        ["Ingress", "Egress"]. If this field is not specified, it
        will default based on the existence of ingress or egress
        rules; policies that contain an egress section are assumed
        to affect egress, and all policies (whether or not they
        contain an ingress section) are assumed to affect ingress.
        If you want to write an egress-only policy, you must
        explicitly specify policyTypes [ "Egress" ]. Likewise, if
        you want to write a policy that specifies that no egress is
        allowed, you must specify a policyTypes value that include
        "Egress" (since such a policy would not include an egress
        section and would otherwise default to just [ "Ingress" ]).
        This field is beta-level in 1.8
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
        name: typing.Optional[str] = None,
        number: typing.Optional[int] = None,
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
        name is the name of the port on the Service. This is a
        mutually exclusive setting with "Number".
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of the port on the Service. This is a
        mutually exclusive setting with "Number".
        """
        self._properties["name"] = value

    @property
    def number(self) -> int:
        """
        number is the numerical port number (e.g. 80) on the
        Service. This is a mutually exclusive setting with "Name".
        """
        return typing.cast(
            int,
            self._properties.get("number"),
        )

    @number.setter
    def number(self, value: int):
        """
        number is the numerical port number (e.g. 80) on the
        Service. This is a mutually exclusive setting with "Name".
        """
        self._properties["number"] = value

    def __enter__(self) -> "ServiceBackendPort":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
