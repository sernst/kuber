import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
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
            api_version="networking/v1beta1", kind="HTTPIngressPath"
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
        Defaults to ImplementationSpecific.
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
        Defaults to ImplementationSpecific.
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
            api_version="networking/v1beta1", kind="HTTPIngressRuleValue"
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
        super(Ingress, self).__init__(api_version="networking/v1beta1", kind="Ingress")
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

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
        service_name: str = None,
        service_port: typing.Union[str, int, None] = None,
    ):
        """Create IngressBackend instance."""
        super(IngressBackend, self).__init__(
            api_version="networking/v1beta1", kind="IngressBackend"
        )
        self._properties = {
            "resource": resource
            if resource is not None
            else TypedLocalObjectReference(),
            "serviceName": service_name if service_name is not None else "",
            "servicePort": service_port if service_port is not None else None,
        }
        self._types = {
            "resource": (TypedLocalObjectReference, None),
            "serviceName": (str, None),
            "servicePort": (int, None),
        }

    @property
    def resource(self) -> "TypedLocalObjectReference":
        """
        Resource is an ObjectRef to another Kubernetes resource in
        the namespace of the Ingress object. If resource is
        specified, serviceName and servicePort must not be
        specified.
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
        specified, serviceName and servicePort must not be
        specified.
        """
        if isinstance(value, dict):
            value = typing.cast(
                TypedLocalObjectReference,
                TypedLocalObjectReference().from_dict(value),
            )
        self._properties["resource"] = value

    @property
    def service_name(self) -> str:
        """
        Specifies the name of the referenced service.
        """
        return typing.cast(
            str,
            self._properties.get("serviceName"),
        )

    @service_name.setter
    def service_name(self, value: str):
        """
        Specifies the name of the referenced service.
        """
        self._properties["serviceName"] = value

    @property
    def service_port(self) -> typing.Optional[int]:
        """
        Specifies the port of the referenced service.
        """
        value = self._properties.get("servicePort")
        return int(value) if value is not None else None

    @service_port.setter
    def service_port(self, value: typing.Union[str, int, None]):
        """
        Specifies the port of the referenced service.
        """
        self._properties["servicePort"] = None if value is None else f"{value}"

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
            api_version="networking/v1beta1", kind="IngressClass"
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

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
            api_version="networking/v1beta1", kind="IngressClassList"
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

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
            api_version="networking/v1beta1", kind="IngressClassSpec"
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
            api_version="networking/v1beta1", kind="IngressList"
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

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
            api_version="networking/v1beta1", kind="IngressRule"
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


class IngressSpec(_kuber_definitions.Definition):
    """
    IngressSpec describes the Ingress the user wishes to exist.
    """

    def __init__(
        self,
        backend: "IngressBackend" = None,
        ingress_class_name: str = None,
        rules: typing.List["IngressRule"] = None,
        tls: typing.List["IngressTLS"] = None,
    ):
        """Create IngressSpec instance."""
        super(IngressSpec, self).__init__(
            api_version="networking/v1beta1", kind="IngressSpec"
        )
        self._properties = {
            "backend": backend if backend is not None else IngressBackend(),
            "ingressClassName": ingress_class_name
            if ingress_class_name is not None
            else "",
            "rules": rules if rules is not None else [],
            "tls": tls if tls is not None else [],
        }
        self._types = {
            "backend": (IngressBackend, None),
            "ingressClassName": (str, None),
            "rules": (list, IngressRule),
            "tls": (list, IngressTLS),
        }

    @property
    def backend(self) -> "IngressBackend":
        """
        A default backend capable of servicing requests that don't
        match any rule. At least one of 'backend' or 'rules' must be
        specified. This field is optional to allow the loadbalancer
        controller or defaulting logic to specify a global default.
        """
        return typing.cast(
            "IngressBackend",
            self._properties.get("backend"),
        )

    @backend.setter
    def backend(self, value: typing.Union["IngressBackend", dict]):
        """
        A default backend capable of servicing requests that don't
        match any rule. At least one of 'backend' or 'rules' must be
        specified. This field is optional to allow the loadbalancer
        controller or defaulting logic to specify a global default.
        """
        if isinstance(value, dict):
            value = typing.cast(
                IngressBackend,
                IngressBackend().from_dict(value),
            )
        self._properties["backend"] = value

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
            api_version="networking/v1beta1", kind="IngressStatus"
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
        super(IngressTLS, self).__init__(
            api_version="networking/v1beta1", kind="IngressTLS"
        )
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
