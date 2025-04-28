import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_32.meta_v1 import Condition  # noqa: F401
from kuber.v1_32.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_32.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_32.meta_v1 import Status  # noqa: F401
from kuber.v1_32.meta_v1 import StatusDetails  # noqa: F401


class IPAddress(_kuber_definitions.Resource):
    """
    IPAddress represents a single IP of a single IP Family. The
    object is designed to be used by APIs that operate on IP
    addresses. The object is used by the Service core API for
    allocation of IP addresses. An IP address can be represented
    in different formats, to guarantee the uniqueness of the IP,
    the name of the object is the IP address in canonical
    format, four decimal digits separated by dots suppressing
    leading zeros for IPv4 and the representation defined by RFC
    5952 for IPv6. Valid: 192.168.1.5 or 2001:db8::1 or
    2001:db8:aaaa:bbbb:cccc:dddd:eeee:1 Invalid: 10.01.2.3 or
    2001:db8:0:0:0::1
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["IPAddressSpec"] = None,
    ):
        """Create IPAddress instance."""
        super(IPAddress, self).__init__(
            api_version="networking/v1beta1", kind="IPAddress"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else IPAddressSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (IPAddressSpec, None),
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
    def spec(self) -> "IPAddressSpec":
        """
        spec is the desired state of the IPAddress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "IPAddressSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["IPAddressSpec", dict]):
        """
        spec is the desired state of the IPAddress. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                IPAddressSpec,
                IPAddressSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the IPAddress in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_ipaddress", "create_ipaddress"]

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
        Replaces the IPAddress in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_ipaddress", "replace_ipaddress"]

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
        Patches the IPAddress in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_ipaddress", "patch_ipaddress"]

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
        Reads the IPAddress from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_ipaddress",
            "read_ipaddress",
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
        Deletes the IPAddress from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_ipaddress",
            "delete_ipaddress",
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

    def __enter__(self) -> "IPAddress":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IPAddressList(_kuber_definitions.Collection):
    """
    IPAddressList contains a list of IPAddress.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["IPAddress"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create IPAddressList instance."""
        super(IPAddressList, self).__init__(
            api_version="networking/v1beta1", kind="IPAddressList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, IPAddress),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["IPAddress"]:
        """
        items is the list of IPAddresses.
        """
        return typing.cast(
            typing.List["IPAddress"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["IPAddress"], typing.List[dict]]):
        """
        items is the list of IPAddresses.
        """
        cleaned: typing.List[IPAddress] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    IPAddress,
                    IPAddress().from_dict(item),
                )
            cleaned.append(typing.cast(IPAddress, item))
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

    def __enter__(self) -> "IPAddressList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class IPAddressSpec(_kuber_definitions.Definition):
    """
    IPAddressSpec describe the attributes in an IP Address.
    """

    def __init__(
        self,
        parent_ref: typing.Optional["ParentReference"] = None,
    ):
        """Create IPAddressSpec instance."""
        super(IPAddressSpec, self).__init__(
            api_version="networking/v1beta1", kind="IPAddressSpec"
        )
        self._properties = {
            "parentRef": parent_ref if parent_ref is not None else ParentReference(),
        }
        self._types = {
            "parentRef": (ParentReference, None),
        }

    @property
    def parent_ref(self) -> "ParentReference":
        """
        ParentRef references the resource that an IPAddress is
        attached to. An IPAddress must reference a parent object.
        """
        return typing.cast(
            "ParentReference",
            self._properties.get("parentRef"),
        )

    @parent_ref.setter
    def parent_ref(self, value: typing.Union["ParentReference", dict]):
        """
        ParentRef references the resource that an IPAddress is
        attached to. An IPAddress must reference a parent object.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ParentReference,
                ParentReference().from_dict(value),
            )
        self._properties["parentRef"] = value

    def __enter__(self) -> "IPAddressSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ParentReference(_kuber_definitions.Definition):
    """
    ParentReference describes a reference to a parent object.
    """

    def __init__(
        self,
        group: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
    ):
        """Create ParentReference instance."""
        super(ParentReference, self).__init__(
            api_version="networking/v1beta1", kind="ParentReference"
        )
        self._properties = {
            "group": group if group is not None else "",
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "resource": resource if resource is not None else "",
        }
        self._types = {
            "group": (str, None),
            "name": (str, None),
            "namespace": (str, None),
            "resource": (str, None),
        }

    @property
    def group(self) -> str:
        """
        Group is the group of the object being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("group"),
        )

    @group.setter
    def group(self, value: str):
        """
        Group is the group of the object being referenced.
        """
        self._properties["group"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of the object being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the object being referenced.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        Namespace is the namespace of the object being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace is the namespace of the object being referenced.
        """
        self._properties["namespace"] = value

    @property
    def resource(self) -> str:
        """
        Resource is the resource of the object being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: str):
        """
        Resource is the resource of the object being referenced.
        """
        self._properties["resource"] = value

    def __enter__(self) -> "ParentReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceCIDR(_kuber_definitions.Resource):
    """
    ServiceCIDR defines a range of IP addresses using CIDR
    format (e.g. 192.168.0.0/24 or 2001:db2::/64). This range is
    used to allocate ClusterIPs to Service objects.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ServiceCIDRSpec"] = None,
        status: typing.Optional["ServiceCIDRStatus"] = None,
    ):
        """Create ServiceCIDR instance."""
        super(ServiceCIDR, self).__init__(
            api_version="networking/v1beta1", kind="ServiceCIDR"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ServiceCIDRSpec(),
            "status": status if status is not None else ServiceCIDRStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ServiceCIDRSpec, None),
            "status": (ServiceCIDRStatus, None),
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
    def spec(self) -> "ServiceCIDRSpec":
        """
        spec is the desired state of the ServiceCIDR. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "ServiceCIDRSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ServiceCIDRSpec", dict]):
        """
        spec is the desired state of the ServiceCIDR. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                ServiceCIDRSpec,
                ServiceCIDRSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "ServiceCIDRStatus":
        """
        status represents the current state of the ServiceCIDR. More
        info: https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "ServiceCIDRStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["ServiceCIDRStatus", dict]):
        """
        status represents the current state of the ServiceCIDR. More
        info: https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                ServiceCIDRStatus,
                ServiceCIDRStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ServiceCIDRStatus":
        """
        Creates the ServiceCIDR in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_service_cidr", "create_service_cidr"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = ServiceCIDRStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ServiceCIDRStatus":
        """
        Replaces the ServiceCIDR in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_service_cidr", "replace_service_cidr"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ServiceCIDRStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ServiceCIDRStatus":
        """
        Patches the ServiceCIDR in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_service_cidr", "patch_service_cidr"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ServiceCIDRStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "ServiceCIDRStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_service_cidr",
            "read_service_cidr",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = ServiceCIDRStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the ServiceCIDR from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_service_cidr",
            "read_service_cidr",
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
        Deletes the ServiceCIDR from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_service_cidr",
            "delete_service_cidr",
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

    def __enter__(self) -> "ServiceCIDR":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceCIDRList(_kuber_definitions.Collection):
    """
    ServiceCIDRList contains a list of ServiceCIDR objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ServiceCIDR"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ServiceCIDRList instance."""
        super(ServiceCIDRList, self).__init__(
            api_version="networking/v1beta1", kind="ServiceCIDRList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ServiceCIDR),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ServiceCIDR"]:
        """
        items is the list of ServiceCIDRs.
        """
        return typing.cast(
            typing.List["ServiceCIDR"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["ServiceCIDR"], typing.List[dict]]):
        """
        items is the list of ServiceCIDRs.
        """
        cleaned: typing.List[ServiceCIDR] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ServiceCIDR,
                    ServiceCIDR().from_dict(item),
                )
            cleaned.append(typing.cast(ServiceCIDR, item))
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
    ) -> "client.NetworkingV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.NetworkingV1beta1Api(**kwargs)

    def __enter__(self) -> "ServiceCIDRList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceCIDRSpec(_kuber_definitions.Definition):
    """
    ServiceCIDRSpec define the CIDRs the user wants to use for
    allocating ClusterIPs for Services.
    """

    def __init__(
        self,
        cidrs: typing.Optional[typing.List[str]] = None,
    ):
        """Create ServiceCIDRSpec instance."""
        super(ServiceCIDRSpec, self).__init__(
            api_version="networking/v1beta1", kind="ServiceCIDRSpec"
        )
        self._properties = {
            "cidrs": cidrs if cidrs is not None else [],
        }
        self._types = {
            "cidrs": (list, str),
        }

    @property
    def cidrs(self) -> typing.List[str]:
        """
        CIDRs defines the IP blocks in CIDR notation (e.g.
        "192.168.0.0/24" or "2001:db8::/64") from which to assign
        service cluster IPs. Max of two CIDRs is allowed, one of
        each IP family. This field is immutable.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("cidrs"),
        )

    @cidrs.setter
    def cidrs(self, value: typing.List[str]):
        """
        CIDRs defines the IP blocks in CIDR notation (e.g.
        "192.168.0.0/24" or "2001:db8::/64") from which to assign
        service cluster IPs. Max of two CIDRs is allowed, one of
        each IP family. This field is immutable.
        """
        self._properties["cidrs"] = value

    def __enter__(self) -> "ServiceCIDRSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceCIDRStatus(_kuber_definitions.Definition):
    """
    ServiceCIDRStatus describes the current state of the
    ServiceCIDR.
    """

    def __init__(
        self,
        conditions: typing.Optional[typing.List["Condition"]] = None,
    ):
        """Create ServiceCIDRStatus instance."""
        super(ServiceCIDRStatus, self).__init__(
            api_version="networking/v1beta1", kind="ServiceCIDRStatus"
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
        }
        self._types = {
            "conditions": (list, Condition),
        }

    @property
    def conditions(self) -> typing.List["Condition"]:
        """
        conditions holds an array of metav1.Condition that describe
        the state of the ServiceCIDR. Current service state
        """
        return typing.cast(
            typing.List["Condition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["Condition"], typing.List[dict]]
    ):
        """
        conditions holds an array of metav1.Condition that describe
        the state of the ServiceCIDR. Current service state
        """
        cleaned: typing.List[Condition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Condition,
                    Condition().from_dict(item),
                )
            cleaned.append(typing.cast(Condition, item))
        self._properties["conditions"] = cleaned

    def __enter__(self) -> "ServiceCIDRStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
