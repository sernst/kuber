import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_30.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_30.core_v1 import NodeSelector  # noqa: F401
from kuber.v1_30.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_30.apimachinery_runtime import RawExtension  # noqa: F401
from kuber.v1_30.meta_v1 import Status  # noqa: F401
from kuber.v1_30.meta_v1 import StatusDetails  # noqa: F401


class AllocationResult(_kuber_definitions.Definition):
    """
    AllocationResult contains attributes of an allocated
    resource.
    """

    def __init__(
        self,
        available_on_nodes: typing.Optional["NodeSelector"] = None,
        resource_handles: typing.Optional[typing.List["ResourceHandle"]] = None,
        shareable: typing.Optional[bool] = None,
    ):
        """Create AllocationResult instance."""
        super(AllocationResult, self).__init__(
            api_version="resource/v1alpha2", kind="AllocationResult"
        )
        self._properties = {
            "availableOnNodes": (
                available_on_nodes if available_on_nodes is not None else NodeSelector()
            ),
            "resourceHandles": resource_handles if resource_handles is not None else [],
            "shareable": shareable if shareable is not None else None,
        }
        self._types = {
            "availableOnNodes": (NodeSelector, None),
            "resourceHandles": (list, ResourceHandle),
            "shareable": (bool, None),
        }

    @property
    def available_on_nodes(self) -> "NodeSelector":
        """
        This field will get set by the resource driver after it has
        allocated the resource to inform the scheduler where it can
        schedule Pods using the ResourceClaim.

        Setting this field is optional. If null, the resource is
        available everywhere.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("availableOnNodes"),
        )

    @available_on_nodes.setter
    def available_on_nodes(self, value: typing.Union["NodeSelector", dict]):
        """
        This field will get set by the resource driver after it has
        allocated the resource to inform the scheduler where it can
        schedule Pods using the ResourceClaim.

        Setting this field is optional. If null, the resource is
        available everywhere.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["availableOnNodes"] = value

    @property
    def resource_handles(self) -> typing.List["ResourceHandle"]:
        """
        ResourceHandles contain the state associated with an
        allocation that should be maintained throughout the lifetime
        of a claim. Each ResourceHandle contains data that should be
        passed to a specific kubelet plugin once it lands on a node.
        This data is returned by the driver after a successful
        allocation and is opaque to Kubernetes. Driver documentation
        may explain to users how to interpret this data if needed.

        Setting this field is optional. It has a maximum size of 32
        entries. If null (or empty), it is assumed this allocation
        will be processed by a single kubelet plugin with no
        ResourceHandle data attached. The name of the kubelet plugin
        invoked will match the DriverName set in the
        ResourceClaimStatus this AllocationResult is embedded in.
        """
        return typing.cast(
            typing.List["ResourceHandle"],
            self._properties.get("resourceHandles"),
        )

    @resource_handles.setter
    def resource_handles(
        self, value: typing.Union[typing.List["ResourceHandle"], typing.List[dict]]
    ):
        """
        ResourceHandles contain the state associated with an
        allocation that should be maintained throughout the lifetime
        of a claim. Each ResourceHandle contains data that should be
        passed to a specific kubelet plugin once it lands on a node.
        This data is returned by the driver after a successful
        allocation and is opaque to Kubernetes. Driver documentation
        may explain to users how to interpret this data if needed.

        Setting this field is optional. It has a maximum size of 32
        entries. If null (or empty), it is assumed this allocation
        will be processed by a single kubelet plugin with no
        ResourceHandle data attached. The name of the kubelet plugin
        invoked will match the DriverName set in the
        ResourceClaimStatus this AllocationResult is embedded in.
        """
        cleaned: typing.List[ResourceHandle] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceHandle,
                    ResourceHandle().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceHandle, item))
        self._properties["resourceHandles"] = cleaned

    @property
    def shareable(self) -> bool:
        """
        Shareable determines whether the resource supports more than
        one consumer at a time.
        """
        return typing.cast(
            bool,
            self._properties.get("shareable"),
        )

    @shareable.setter
    def shareable(self, value: bool):
        """
        Shareable determines whether the resource supports more than
        one consumer at a time.
        """
        self._properties["shareable"] = value

    def __enter__(self) -> "AllocationResult":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DriverAllocationResult(_kuber_definitions.Definition):
    """
    DriverAllocationResult contains vendor parameters and the
    allocation result for one request.
    """

    def __init__(
        self,
        named_resources: typing.Optional["NamedResourcesAllocationResult"] = None,
        vendor_request_parameters: typing.Optional["RawExtension"] = None,
    ):
        """Create DriverAllocationResult instance."""
        super(DriverAllocationResult, self).__init__(
            api_version="resource/v1alpha2", kind="DriverAllocationResult"
        )
        self._properties = {
            "namedResources": (
                named_resources
                if named_resources is not None
                else NamedResourcesAllocationResult()
            ),
            "vendorRequestParameters": (
                vendor_request_parameters
                if vendor_request_parameters is not None
                else RawExtension()
            ),
        }
        self._types = {
            "namedResources": (NamedResourcesAllocationResult, None),
            "vendorRequestParameters": (RawExtension, None),
        }

    @property
    def named_resources(self) -> "NamedResourcesAllocationResult":
        """
        NamedResources describes the allocation result when using
        the named resources model.
        """
        return typing.cast(
            "NamedResourcesAllocationResult",
            self._properties.get("namedResources"),
        )

    @named_resources.setter
    def named_resources(
        self, value: typing.Union["NamedResourcesAllocationResult", dict]
    ):
        """
        NamedResources describes the allocation result when using
        the named resources model.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NamedResourcesAllocationResult,
                NamedResourcesAllocationResult().from_dict(value),
            )
        self._properties["namedResources"] = value

    @property
    def vendor_request_parameters(self) -> "RawExtension":
        """
        VendorRequestParameters are the per-request configuration
        parameters from the time that the claim was allocated.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("vendorRequestParameters"),
        )

    @vendor_request_parameters.setter
    def vendor_request_parameters(self, value: typing.Union["RawExtension", dict]):
        """
        VendorRequestParameters are the per-request configuration
        parameters from the time that the claim was allocated.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["vendorRequestParameters"] = value

    def __enter__(self) -> "DriverAllocationResult":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DriverRequests(_kuber_definitions.Definition):
    """
    DriverRequests describes all resources that are needed from
    one particular driver.
    """

    def __init__(
        self,
        driver_name: typing.Optional[str] = None,
        requests: typing.Optional[typing.List["ResourceRequest"]] = None,
        vendor_parameters: typing.Optional["RawExtension"] = None,
    ):
        """Create DriverRequests instance."""
        super(DriverRequests, self).__init__(
            api_version="resource/v1alpha2", kind="DriverRequests"
        )
        self._properties = {
            "driverName": driver_name if driver_name is not None else "",
            "requests": requests if requests is not None else [],
            "vendorParameters": (
                vendor_parameters if vendor_parameters is not None else RawExtension()
            ),
        }
        self._types = {
            "driverName": (str, None),
            "requests": (list, ResourceRequest),
            "vendorParameters": (RawExtension, None),
        }

    @property
    def driver_name(self) -> str:
        """
        DriverName is the name used by the DRA driver kubelet
        plugin.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName is the name used by the DRA driver kubelet
        plugin.
        """
        self._properties["driverName"] = value

    @property
    def requests(self) -> typing.List["ResourceRequest"]:
        """
        Requests describes all resources that are needed from the
        driver.
        """
        return typing.cast(
            typing.List["ResourceRequest"],
            self._properties.get("requests"),
        )

    @requests.setter
    def requests(
        self, value: typing.Union[typing.List["ResourceRequest"], typing.List[dict]]
    ):
        """
        Requests describes all resources that are needed from the
        driver.
        """
        cleaned: typing.List[ResourceRequest] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceRequest,
                    ResourceRequest().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceRequest, item))
        self._properties["requests"] = cleaned

    @property
    def vendor_parameters(self) -> "RawExtension":
        """
        VendorParameters are arbitrary setup parameters for all
        requests of the claim. They are ignored while allocating the
        claim.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("vendorParameters"),
        )

    @vendor_parameters.setter
    def vendor_parameters(self, value: typing.Union["RawExtension", dict]):
        """
        VendorParameters are arbitrary setup parameters for all
        requests of the claim. They are ignored while allocating the
        claim.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["vendorParameters"] = value

    def __enter__(self) -> "DriverRequests":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesAllocationResult(_kuber_definitions.Definition):
    """
    NamedResourcesAllocationResult is used in
    AllocationResultModel.
    """

    def __init__(
        self,
        name: typing.Optional[str] = None,
    ):
        """Create NamedResourcesAllocationResult instance."""
        super(NamedResourcesAllocationResult, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesAllocationResult"
        )
        self._properties = {
            "name": name if name is not None else "",
        }
        self._types = {
            "name": (str, None),
        }

    @property
    def name(self) -> str:
        """
        Name is the name of the selected resource instance.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the selected resource instance.
        """
        self._properties["name"] = value

    def __enter__(self) -> "NamedResourcesAllocationResult":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesAttribute(_kuber_definitions.Definition):
    """
    NamedResourcesAttribute is a combination of an attribute
    name and its value.
    """

    def __init__(
        self,
        bool_: typing.Optional[bool] = None,
        int_: typing.Optional[int] = None,
        int_slice: typing.Optional["NamedResourcesIntSlice"] = None,
        name: typing.Optional[str] = None,
        quantity: typing.Optional[typing.Union[str, int, None]] = None,
        string: typing.Optional[str] = None,
        string_slice: typing.Optional["NamedResourcesStringSlice"] = None,
        version: typing.Optional[str] = None,
    ):
        """Create NamedResourcesAttribute instance."""
        super(NamedResourcesAttribute, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesAttribute"
        )
        self._properties = {
            "bool": bool_ if bool_ is not None else None,
            "int": int_ if int_ is not None else None,
            "intSlice": (
                int_slice if int_slice is not None else NamedResourcesIntSlice()
            ),
            "name": name if name is not None else "",
            "quantity": quantity if quantity is not None else None,
            "string": string if string is not None else "",
            "stringSlice": (
                string_slice
                if string_slice is not None
                else NamedResourcesStringSlice()
            ),
            "version": version if version is not None else "",
        }
        self._types = {
            "bool": (bool, None),
            "int": (int, None),
            "intSlice": (NamedResourcesIntSlice, None),
            "name": (str, None),
            "quantity": (_types.integer_or_string, None),
            "string": (str, None),
            "stringSlice": (NamedResourcesStringSlice, None),
            "version": (str, None),
        }

    @property
    def bool_(self) -> bool:
        """
        BoolValue is a true/false value.
        """
        return typing.cast(
            bool,
            self._properties.get("bool"),
        )

    @bool_.setter
    def bool_(self, value: bool):
        """
        BoolValue is a true/false value.
        """
        self._properties["bool"] = value

    @property
    def int_(self) -> int:
        """
        IntValue is a 64-bit integer.
        """
        return typing.cast(
            int,
            self._properties.get("int"),
        )

    @int_.setter
    def int_(self, value: int):
        """
        IntValue is a 64-bit integer.
        """
        self._properties["int"] = value

    @property
    def int_slice(self) -> "NamedResourcesIntSlice":
        """
        IntSliceValue is an array of 64-bit integers.
        """
        return typing.cast(
            "NamedResourcesIntSlice",
            self._properties.get("intSlice"),
        )

    @int_slice.setter
    def int_slice(self, value: typing.Union["NamedResourcesIntSlice", dict]):
        """
        IntSliceValue is an array of 64-bit integers.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NamedResourcesIntSlice,
                NamedResourcesIntSlice().from_dict(value),
            )
        self._properties["intSlice"] = value

    @property
    def name(self) -> str:
        """
        Name is unique identifier among all resource instances
        managed by the driver on the node. It must be a DNS
        subdomain.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is unique identifier among all resource instances
        managed by the driver on the node. It must be a DNS
        subdomain.
        """
        self._properties["name"] = value

    @property
    def quantity(self) -> typing.Optional[str]:
        """
        QuantityValue is a quantity.
        """
        value = self._properties.get("quantity")
        return f"{value}" if value is not None else None

    @quantity.setter
    def quantity(self, value: typing.Union[str, int, None]):
        """
        QuantityValue is a quantity.
        """
        self._properties["quantity"] = _types.integer_or_string(value)

    @property
    def string(self) -> str:
        """
        StringValue is a string.
        """
        return typing.cast(
            str,
            self._properties.get("string"),
        )

    @string.setter
    def string(self, value: str):
        """
        StringValue is a string.
        """
        self._properties["string"] = value

    @property
    def string_slice(self) -> "NamedResourcesStringSlice":
        """
        StringSliceValue is an array of strings.
        """
        return typing.cast(
            "NamedResourcesStringSlice",
            self._properties.get("stringSlice"),
        )

    @string_slice.setter
    def string_slice(self, value: typing.Union["NamedResourcesStringSlice", dict]):
        """
        StringSliceValue is an array of strings.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NamedResourcesStringSlice,
                NamedResourcesStringSlice().from_dict(value),
            )
        self._properties["stringSlice"] = value

    @property
    def version(self) -> str:
        """
        VersionValue is a semantic version according to semver.org
        spec 2.0.0.
        """
        return typing.cast(
            str,
            self._properties.get("version"),
        )

    @version.setter
    def version(self, value: str):
        """
        VersionValue is a semantic version according to semver.org
        spec 2.0.0.
        """
        self._properties["version"] = value

    def __enter__(self) -> "NamedResourcesAttribute":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesFilter(_kuber_definitions.Definition):
    """
    NamedResourcesFilter is used in ResourceFilterModel.
    """

    def __init__(
        self,
        selector: typing.Optional[str] = None,
    ):
        """Create NamedResourcesFilter instance."""
        super(NamedResourcesFilter, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesFilter"
        )
        self._properties = {
            "selector": selector if selector is not None else "",
        }
        self._types = {
            "selector": (str, None),
        }

    @property
    def selector(self) -> str:
        """
        Selector is a CEL expression which must evaluate to true if
        a resource instance is suitable. The language is as defined
        in https://kubernetes.io/docs/reference/using-api/cel/

        In addition, for each type NamedResourcesin AttributeValue
        there is a map that resolves to the corresponding value of
        the instance under evaluation. For example:

           attributes.quantity["a"].isGreaterThan(quantity("0")) &&
           attributes.stringslice["b"].isSorted()
        """
        return typing.cast(
            str,
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: str):
        """
        Selector is a CEL expression which must evaluate to true if
        a resource instance is suitable. The language is as defined
        in https://kubernetes.io/docs/reference/using-api/cel/

        In addition, for each type NamedResourcesin AttributeValue
        there is a map that resolves to the corresponding value of
        the instance under evaluation. For example:

           attributes.quantity["a"].isGreaterThan(quantity("0")) &&
           attributes.stringslice["b"].isSorted()
        """
        self._properties["selector"] = value

    def __enter__(self) -> "NamedResourcesFilter":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesInstance(_kuber_definitions.Definition):
    """
    NamedResourcesInstance represents one individual hardware
    instance that can be selected based on its attributes.
    """

    def __init__(
        self,
        attributes: typing.Optional[typing.List["NamedResourcesAttribute"]] = None,
        name: typing.Optional[str] = None,
    ):
        """Create NamedResourcesInstance instance."""
        super(NamedResourcesInstance, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesInstance"
        )
        self._properties = {
            "attributes": attributes if attributes is not None else [],
            "name": name if name is not None else "",
        }
        self._types = {
            "attributes": (list, NamedResourcesAttribute),
            "name": (str, None),
        }

    @property
    def attributes(self) -> typing.List["NamedResourcesAttribute"]:
        """
        Attributes defines the attributes of this resource instance.
        The name of each attribute must be unique.
        """
        return typing.cast(
            typing.List["NamedResourcesAttribute"],
            self._properties.get("attributes"),
        )

    @attributes.setter
    def attributes(
        self,
        value: typing.Union[typing.List["NamedResourcesAttribute"], typing.List[dict]],
    ):
        """
        Attributes defines the attributes of this resource instance.
        The name of each attribute must be unique.
        """
        cleaned: typing.List[NamedResourcesAttribute] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NamedResourcesAttribute,
                    NamedResourcesAttribute().from_dict(item),
                )
            cleaned.append(typing.cast(NamedResourcesAttribute, item))
        self._properties["attributes"] = cleaned

    @property
    def name(self) -> str:
        """
        Name is unique identifier among all resource instances
        managed by the driver on the node. It must be a DNS
        subdomain.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is unique identifier among all resource instances
        managed by the driver on the node. It must be a DNS
        subdomain.
        """
        self._properties["name"] = value

    def __enter__(self) -> "NamedResourcesInstance":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesIntSlice(_kuber_definitions.Definition):
    """
    NamedResourcesIntSlice contains a slice of 64-bit integers.
    """

    def __init__(
        self,
        ints: typing.Optional[typing.List[int]] = None,
    ):
        """Create NamedResourcesIntSlice instance."""
        super(NamedResourcesIntSlice, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesIntSlice"
        )
        self._properties = {
            "ints": ints if ints is not None else [],
        }
        self._types = {
            "ints": (list, int),
        }

    @property
    def ints(self) -> typing.List[int]:
        """
        Ints is the slice of 64-bit integers.
        """
        return typing.cast(
            typing.List[int],
            self._properties.get("ints"),
        )

    @ints.setter
    def ints(self, value: typing.List[int]):
        """
        Ints is the slice of 64-bit integers.
        """
        self._properties["ints"] = value

    def __enter__(self) -> "NamedResourcesIntSlice":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesRequest(_kuber_definitions.Definition):
    """
    NamedResourcesRequest is used in ResourceRequestModel.
    """

    def __init__(
        self,
        selector: typing.Optional[str] = None,
    ):
        """Create NamedResourcesRequest instance."""
        super(NamedResourcesRequest, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesRequest"
        )
        self._properties = {
            "selector": selector if selector is not None else "",
        }
        self._types = {
            "selector": (str, None),
        }

    @property
    def selector(self) -> str:
        """
        Selector is a CEL expression which must evaluate to true if
        a resource instance is suitable. The language is as defined
        in https://kubernetes.io/docs/reference/using-api/cel/

        In addition, for each type NamedResourcesin AttributeValue
        there is a map that resolves to the corresponding value of
        the instance under evaluation. For example:

           attributes.quantity["a"].isGreaterThan(quantity("0")) &&
           attributes.stringslice["b"].isSorted()
        """
        return typing.cast(
            str,
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: str):
        """
        Selector is a CEL expression which must evaluate to true if
        a resource instance is suitable. The language is as defined
        in https://kubernetes.io/docs/reference/using-api/cel/

        In addition, for each type NamedResourcesin AttributeValue
        there is a map that resolves to the corresponding value of
        the instance under evaluation. For example:

           attributes.quantity["a"].isGreaterThan(quantity("0")) &&
           attributes.stringslice["b"].isSorted()
        """
        self._properties["selector"] = value

    def __enter__(self) -> "NamedResourcesRequest":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesResources(_kuber_definitions.Definition):
    """
    NamedResourcesResources is used in ResourceModel.
    """

    def __init__(
        self,
        instances: typing.Optional[typing.List["NamedResourcesInstance"]] = None,
    ):
        """Create NamedResourcesResources instance."""
        super(NamedResourcesResources, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesResources"
        )
        self._properties = {
            "instances": instances if instances is not None else [],
        }
        self._types = {
            "instances": (list, NamedResourcesInstance),
        }

    @property
    def instances(self) -> typing.List["NamedResourcesInstance"]:
        """
        The list of all individual resources instances currently
        available.
        """
        return typing.cast(
            typing.List["NamedResourcesInstance"],
            self._properties.get("instances"),
        )

    @instances.setter
    def instances(
        self,
        value: typing.Union[typing.List["NamedResourcesInstance"], typing.List[dict]],
    ):
        """
        The list of all individual resources instances currently
        available.
        """
        cleaned: typing.List[NamedResourcesInstance] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NamedResourcesInstance,
                    NamedResourcesInstance().from_dict(item),
                )
            cleaned.append(typing.cast(NamedResourcesInstance, item))
        self._properties["instances"] = cleaned

    def __enter__(self) -> "NamedResourcesResources":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedResourcesStringSlice(_kuber_definitions.Definition):
    """
    NamedResourcesStringSlice contains a slice of strings.
    """

    def __init__(
        self,
        strings: typing.Optional[typing.List[str]] = None,
    ):
        """Create NamedResourcesStringSlice instance."""
        super(NamedResourcesStringSlice, self).__init__(
            api_version="resource/v1alpha2", kind="NamedResourcesStringSlice"
        )
        self._properties = {
            "strings": strings if strings is not None else [],
        }
        self._types = {
            "strings": (list, str),
        }

    @property
    def strings(self) -> typing.List[str]:
        """
        Strings is the slice of strings.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("strings"),
        )

    @strings.setter
    def strings(self, value: typing.List[str]):
        """
        Strings is the slice of strings.
        """
        self._properties["strings"] = value

    def __enter__(self) -> "NamedResourcesStringSlice":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContext(_kuber_definitions.Resource):
    """
    PodSchedulingContext objects hold information that is needed
    to schedule a Pod with ResourceClaims that use
    "WaitForFirstConsumer" allocation mode.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["PodSchedulingContextSpec"] = None,
        status: typing.Optional["PodSchedulingContextStatus"] = None,
    ):
        """Create PodSchedulingContext instance."""
        super(PodSchedulingContext, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContext"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else PodSchedulingContextSpec(),
            "status": status if status is not None else PodSchedulingContextStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (PodSchedulingContextSpec, None),
            "status": (PodSchedulingContextStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "PodSchedulingContextSpec":
        """
        Spec describes where resources for the Pod are needed.
        """
        return typing.cast(
            "PodSchedulingContextSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["PodSchedulingContextSpec", dict]):
        """
        Spec describes where resources for the Pod are needed.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodSchedulingContextSpec,
                PodSchedulingContextSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "PodSchedulingContextStatus":
        """
        Status describes where resources for the Pod can be
        allocated.
        """
        return typing.cast(
            "PodSchedulingContextStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["PodSchedulingContextStatus", dict]):
        """
        Status describes where resources for the Pod can be
        allocated.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodSchedulingContextStatus,
                PodSchedulingContextStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Creates the PodSchedulingContext in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_pod_scheduling_context",
            "create_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Replaces the PodSchedulingContext in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_pod_scheduling_context",
            "replace_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Patches the PodSchedulingContext in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_pod_scheduling_context",
            "patch_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "PodSchedulingContextStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_pod_scheduling_context",
            "read_pod_scheduling_context",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = PodSchedulingContextStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the PodSchedulingContext from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_pod_scheduling_context",
            "read_pod_scheduling_context",
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
        Deletes the PodSchedulingContext from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_pod_scheduling_context",
            "delete_pod_scheduling_context",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "PodSchedulingContext":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContextList(_kuber_definitions.Collection):
    """
    PodSchedulingContextList is a collection of Pod scheduling
    objects.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["PodSchedulingContext"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create PodSchedulingContextList instance."""
        super(PodSchedulingContextList, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContextList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, PodSchedulingContext),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["PodSchedulingContext"]:
        """
        Items is the list of PodSchedulingContext objects.
        """
        return typing.cast(
            typing.List["PodSchedulingContext"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["PodSchedulingContext"], typing.List[dict]],
    ):
        """
        Items is the list of PodSchedulingContext objects.
        """
        cleaned: typing.List[PodSchedulingContext] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PodSchedulingContext,
                    PodSchedulingContext().from_dict(item),
                )
            cleaned.append(typing.cast(PodSchedulingContext, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "PodSchedulingContextList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContextSpec(_kuber_definitions.Definition):
    """
    PodSchedulingContextSpec describes where resources for the
    Pod are needed.
    """

    def __init__(
        self,
        potential_nodes: typing.Optional[typing.List[str]] = None,
        selected_node: typing.Optional[str] = None,
    ):
        """Create PodSchedulingContextSpec instance."""
        super(PodSchedulingContextSpec, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContextSpec"
        )
        self._properties = {
            "potentialNodes": potential_nodes if potential_nodes is not None else [],
            "selectedNode": selected_node if selected_node is not None else "",
        }
        self._types = {
            "potentialNodes": (list, str),
            "selectedNode": (str, None),
        }

    @property
    def potential_nodes(self) -> typing.List[str]:
        """
        PotentialNodes lists nodes where the Pod might be able to
        run.

        The size of this field is limited to 128. This is large
        enough for many clusters. Larger clusters may need more
        attempts to find a node that suits all pending resources.
        This may get increased in the future, but not reduced.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("potentialNodes"),
        )

    @potential_nodes.setter
    def potential_nodes(self, value: typing.List[str]):
        """
        PotentialNodes lists nodes where the Pod might be able to
        run.

        The size of this field is limited to 128. This is large
        enough for many clusters. Larger clusters may need more
        attempts to find a node that suits all pending resources.
        This may get increased in the future, but not reduced.
        """
        self._properties["potentialNodes"] = value

    @property
    def selected_node(self) -> str:
        """
        SelectedNode is the node for which allocation of
        ResourceClaims that are referenced by the Pod and that use
        "WaitForFirstConsumer" allocation is to be attempted.
        """
        return typing.cast(
            str,
            self._properties.get("selectedNode"),
        )

    @selected_node.setter
    def selected_node(self, value: str):
        """
        SelectedNode is the node for which allocation of
        ResourceClaims that are referenced by the Pod and that use
        "WaitForFirstConsumer" allocation is to be attempted.
        """
        self._properties["selectedNode"] = value

    def __enter__(self) -> "PodSchedulingContextSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContextStatus(_kuber_definitions.Definition):
    """
    PodSchedulingContextStatus describes where resources for the
    Pod can be allocated.
    """

    def __init__(
        self,
        resource_claims: typing.Optional[
            typing.List["ResourceClaimSchedulingStatus"]
        ] = None,
    ):
        """Create PodSchedulingContextStatus instance."""
        super(PodSchedulingContextStatus, self).__init__(
            api_version="resource/v1alpha2", kind="PodSchedulingContextStatus"
        )
        self._properties = {
            "resourceClaims": resource_claims if resource_claims is not None else [],
        }
        self._types = {
            "resourceClaims": (list, ResourceClaimSchedulingStatus),
        }

    @property
    def resource_claims(self) -> typing.List["ResourceClaimSchedulingStatus"]:
        """
        ResourceClaims describes resource availability for each
        pod.spec.resourceClaim entry where the corresponding
        ResourceClaim uses "WaitForFirstConsumer" allocation mode.
        """
        return typing.cast(
            typing.List["ResourceClaimSchedulingStatus"],
            self._properties.get("resourceClaims"),
        )

    @resource_claims.setter
    def resource_claims(
        self,
        value: typing.Union[
            typing.List["ResourceClaimSchedulingStatus"], typing.List[dict]
        ],
    ):
        """
        ResourceClaims describes resource availability for each
        pod.spec.resourceClaim entry where the corresponding
        ResourceClaim uses "WaitForFirstConsumer" allocation mode.
        """
        cleaned: typing.List[ResourceClaimSchedulingStatus] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaimSchedulingStatus,
                    ResourceClaimSchedulingStatus().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaimSchedulingStatus, item))
        self._properties["resourceClaims"] = cleaned

    def __enter__(self) -> "PodSchedulingContextStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaim(_kuber_definitions.Resource):
    """
    ResourceClaim describes which resources are needed by a
    resource consumer. Its status tracks whether the resource
    has been allocated and what the resulting attributes are.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceClaimSpec"] = None,
        status: typing.Optional["ResourceClaimStatus"] = None,
    ):
        """Create ResourceClaim instance."""
        super(ResourceClaim, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaim"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ResourceClaimSpec(),
            "status": status if status is not None else ResourceClaimStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ResourceClaimSpec, None),
            "status": (ResourceClaimStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ResourceClaimSpec":
        """
        Spec describes the desired attributes of a resource that
        then needs to be allocated. It can only be set once when
        creating the ResourceClaim.
        """
        return typing.cast(
            "ResourceClaimSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceClaimSpec", dict]):
        """
        Spec describes the desired attributes of a resource that
        then needs to be allocated. It can only be set once when
        creating the ResourceClaim.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimSpec,
                ResourceClaimSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "ResourceClaimStatus":
        """
        Status describes whether the resource is available and with
        which attributes.
        """
        return typing.cast(
            "ResourceClaimStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["ResourceClaimStatus", dict]):
        """
        Status describes whether the resource is available and with
        which attributes.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimStatus,
                ResourceClaimStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Creates the ResourceClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_resource_claim", "create_resource_claim"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Replaces the ResourceClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_resource_claim", "replace_resource_claim"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Patches the ResourceClaim in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_resource_claim", "patch_resource_claim"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "ResourceClaimStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_resource_claim",
            "read_resource_claim",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = ResourceClaimStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the ResourceClaim from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_claim",
            "read_resource_claim",
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
        Deletes the ResourceClaim from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_claim",
            "delete_resource_claim",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaim":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimConsumerReference(_kuber_definitions.Definition):
    """
    ResourceClaimConsumerReference contains enough information
    to let you locate the consumer of a ResourceClaim. The user
    must be a resource in the same namespace as the
    ResourceClaim.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        uid: typing.Optional[str] = None,
    ):
        """Create ResourceClaimConsumerReference instance."""
        super(ResourceClaimConsumerReference, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimConsumerReference"
        )
        self._properties = {
            "apiGroup": api_group if api_group is not None else "",
            "name": name if name is not None else "",
            "resource": resource if resource is not None else "",
            "uid": uid if uid is not None else "",
        }
        self._types = {
            "apiGroup": (str, None),
            "name": (str, None),
            "resource": (str, None),
            "uid": (str, None),
        }

    @property
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        self._properties["apiGroup"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced.
        """
        self._properties["name"] = value

    @property
    def resource(self) -> str:
        """
        Resource is the type of resource being referenced, for
        example "pods".
        """
        return typing.cast(
            str,
            self._properties.get("resource"),
        )

    @resource.setter
    def resource(self, value: str):
        """
        Resource is the type of resource being referenced, for
        example "pods".
        """
        self._properties["resource"] = value

    @property
    def uid(self) -> str:
        """
        UID identifies exactly one incarnation of the resource.
        """
        return typing.cast(
            str,
            self._properties.get("uid"),
        )

    @uid.setter
    def uid(self, value: str):
        """
        UID identifies exactly one incarnation of the resource.
        """
        self._properties["uid"] = value

    def __enter__(self) -> "ResourceClaimConsumerReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimList(_kuber_definitions.Collection):
    """
    ResourceClaimList is a collection of claims.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClaim"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClaimList instance."""
        super(ResourceClaimList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClaim),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClaim"]:
        """
        Items is the list of resource claims.
        """
        return typing.cast(
            typing.List["ResourceClaim"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ResourceClaim"], typing.List[dict]]
    ):
        """
        Items is the list of resource claims.
        """
        cleaned: typing.List[ResourceClaim] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaim,
                    ResourceClaim().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaim, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimParameters(_kuber_definitions.Resource):
    """
    ResourceClaimParameters defines resource requests for a
    ResourceClaim in an in-tree format understood by Kubernetes.
    """

    def __init__(
        self,
        driver_requests: typing.Optional[typing.List["DriverRequests"]] = None,
        generated_from: typing.Optional["ResourceClaimParametersReference"] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        shareable: typing.Optional[bool] = None,
    ):
        """Create ResourceClaimParameters instance."""
        super(ResourceClaimParameters, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimParameters"
        )
        self._properties = {
            "driverRequests": driver_requests if driver_requests is not None else [],
            "generatedFrom": (
                generated_from
                if generated_from is not None
                else ResourceClaimParametersReference()
            ),
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "shareable": shareable if shareable is not None else None,
        }
        self._types = {
            "apiVersion": (str, None),
            "driverRequests": (list, DriverRequests),
            "generatedFrom": (ResourceClaimParametersReference, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "shareable": (bool, None),
        }

    @property
    def driver_requests(self) -> typing.List["DriverRequests"]:
        """
        DriverRequests describes all resources that are needed for
        the allocated claim. A single claim may use resources coming
        from different drivers. For each driver, this array has at
        most one entry which then may have one or more per-driver
        requests.

        May be empty, in which case the claim can always be
        allocated.
        """
        return typing.cast(
            typing.List["DriverRequests"],
            self._properties.get("driverRequests"),
        )

    @driver_requests.setter
    def driver_requests(
        self, value: typing.Union[typing.List["DriverRequests"], typing.List[dict]]
    ):
        """
        DriverRequests describes all resources that are needed for
        the allocated claim. A single claim may use resources coming
        from different drivers. For each driver, this array has at
        most one entry which then may have one or more per-driver
        requests.

        May be empty, in which case the claim can always be
        allocated.
        """
        cleaned: typing.List[DriverRequests] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DriverRequests,
                    DriverRequests().from_dict(item),
                )
            cleaned.append(typing.cast(DriverRequests, item))
        self._properties["driverRequests"] = cleaned

    @property
    def generated_from(self) -> "ResourceClaimParametersReference":
        """
        If this object was created from some other resource, then
        this links back to that resource. This field is used to find
        the in-tree representation of the claim parameters when the
        parameter reference of the claim refers to some unknown
        type.
        """
        return typing.cast(
            "ResourceClaimParametersReference",
            self._properties.get("generatedFrom"),
        )

    @generated_from.setter
    def generated_from(
        self, value: typing.Union["ResourceClaimParametersReference", dict]
    ):
        """
        If this object was created from some other resource, then
        this links back to that resource. This field is used to find
        the in-tree representation of the claim parameters when the
        parameter reference of the claim refers to some unknown
        type.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimParametersReference,
                ResourceClaimParametersReference().from_dict(value),
            )
        self._properties["generatedFrom"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def shareable(self) -> bool:
        """
        Shareable indicates whether the allocated claim is meant to
        be shareable by multiple consumers at the same time.
        """
        return typing.cast(
            bool,
            self._properties.get("shareable"),
        )

    @shareable.setter
    def shareable(self, value: bool):
        """
        Shareable indicates whether the allocated claim is meant to
        be shareable by multiple consumers at the same time.
        """
        self._properties["shareable"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ResourceClaimParameters in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_resource_claim_parameters",
            "create_resource_claim_parameters",
        ]

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
        Replaces the ResourceClaimParameters in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_resource_claim_parameters",
            "replace_resource_claim_parameters",
        ]

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
        Patches the ResourceClaimParameters in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_resource_claim_parameters",
            "patch_resource_claim_parameters",
        ]

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
        Reads the ResourceClaimParameters from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_claim_parameters",
            "read_resource_claim_parameters",
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
        Deletes the ResourceClaimParameters from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_claim_parameters",
            "delete_resource_claim_parameters",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimParameters":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimParametersList(_kuber_definitions.Collection):
    """
    ResourceClaimParametersList is a collection of
    ResourceClaimParameters.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClaimParameters"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClaimParametersList instance."""
        super(ResourceClaimParametersList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimParametersList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClaimParameters),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClaimParameters"]:
        """
        Items is the list of node resource capacity objects.
        """
        return typing.cast(
            typing.List["ResourceClaimParameters"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["ResourceClaimParameters"], typing.List[dict]],
    ):
        """
        Items is the list of node resource capacity objects.
        """
        cleaned: typing.List[ResourceClaimParameters] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaimParameters,
                    ResourceClaimParameters().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaimParameters, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimParametersList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimParametersReference(_kuber_definitions.Definition):
    """
    ResourceClaimParametersReference contains enough information
    to let you locate the parameters for a ResourceClaim. The
    object must be in the same namespace as the ResourceClaim.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ):
        """Create ResourceClaimParametersReference instance."""
        super(ResourceClaimParametersReference, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimParametersReference"
        )
        self._properties = {
            "apiGroup": api_group if api_group is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
        }
        self._types = {
            "apiGroup": (str, None),
            "kind": (str, None),
            "name": (str, None),
        }

    @property
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        self._properties["apiGroup"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata, for
        example "ConfigMap".
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata, for
        example "ConfigMap".
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced.
        """
        self._properties["name"] = value

    def __enter__(self) -> "ResourceClaimParametersReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimSchedulingStatus(_kuber_definitions.Definition):
    """
    ResourceClaimSchedulingStatus contains information about one
    particular ResourceClaim with "WaitForFirstConsumer"
    allocation mode.
    """

    def __init__(
        self,
        name: typing.Optional[str] = None,
        unsuitable_nodes: typing.Optional[typing.List[str]] = None,
    ):
        """Create ResourceClaimSchedulingStatus instance."""
        super(ResourceClaimSchedulingStatus, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimSchedulingStatus"
        )
        self._properties = {
            "name": name if name is not None else "",
            "unsuitableNodes": unsuitable_nodes if unsuitable_nodes is not None else [],
        }
        self._types = {
            "name": (str, None),
            "unsuitableNodes": (list, str),
        }

    @property
    def name(self) -> str:
        """
        Name matches the pod.spec.resourceClaims[*].Name field.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name matches the pod.spec.resourceClaims[*].Name field.
        """
        self._properties["name"] = value

    @property
    def unsuitable_nodes(self) -> typing.List[str]:
        """
        UnsuitableNodes lists nodes that the ResourceClaim cannot be
        allocated for.

        The size of this field is limited to 128, the same as for
        PodSchedulingSpec.PotentialNodes. This may get increased in
        the future, but not reduced.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("unsuitableNodes"),
        )

    @unsuitable_nodes.setter
    def unsuitable_nodes(self, value: typing.List[str]):
        """
        UnsuitableNodes lists nodes that the ResourceClaim cannot be
        allocated for.

        The size of this field is limited to 128, the same as for
        PodSchedulingSpec.PotentialNodes. This may get increased in
        the future, but not reduced.
        """
        self._properties["unsuitableNodes"] = value

    def __enter__(self) -> "ResourceClaimSchedulingStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimSpec(_kuber_definitions.Definition):
    """
    ResourceClaimSpec defines how a resource is to be allocated.
    """

    def __init__(
        self,
        allocation_mode: typing.Optional[str] = None,
        parameters_ref: typing.Optional["ResourceClaimParametersReference"] = None,
        resource_class_name: typing.Optional[str] = None,
    ):
        """Create ResourceClaimSpec instance."""
        super(ResourceClaimSpec, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimSpec"
        )
        self._properties = {
            "allocationMode": allocation_mode if allocation_mode is not None else "",
            "parametersRef": (
                parameters_ref
                if parameters_ref is not None
                else ResourceClaimParametersReference()
            ),
            "resourceClassName": (
                resource_class_name if resource_class_name is not None else ""
            ),
        }
        self._types = {
            "allocationMode": (str, None),
            "parametersRef": (ResourceClaimParametersReference, None),
            "resourceClassName": (str, None),
        }

    @property
    def allocation_mode(self) -> str:
        """
        Allocation can start immediately or when a Pod wants to use
        the resource. "WaitForFirstConsumer" is the default.
        """
        return typing.cast(
            str,
            self._properties.get("allocationMode"),
        )

    @allocation_mode.setter
    def allocation_mode(self, value: str):
        """
        Allocation can start immediately or when a Pod wants to use
        the resource. "WaitForFirstConsumer" is the default.
        """
        self._properties["allocationMode"] = value

    @property
    def parameters_ref(self) -> "ResourceClaimParametersReference":
        """
        ParametersRef references a separate object with arbitrary
        parameters that will be used by the driver when allocating a
        resource for the claim.

        The object must be in the same namespace as the
        ResourceClaim.
        """
        return typing.cast(
            "ResourceClaimParametersReference",
            self._properties.get("parametersRef"),
        )

    @parameters_ref.setter
    def parameters_ref(
        self, value: typing.Union["ResourceClaimParametersReference", dict]
    ):
        """
        ParametersRef references a separate object with arbitrary
        parameters that will be used by the driver when allocating a
        resource for the claim.

        The object must be in the same namespace as the
        ResourceClaim.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimParametersReference,
                ResourceClaimParametersReference().from_dict(value),
            )
        self._properties["parametersRef"] = value

    @property
    def resource_class_name(self) -> str:
        """
        ResourceClassName references the driver and additional
        parameters via the name of a ResourceClass that was created
        as part of the driver deployment.
        """
        return typing.cast(
            str,
            self._properties.get("resourceClassName"),
        )

    @resource_class_name.setter
    def resource_class_name(self, value: str):
        """
        ResourceClassName references the driver and additional
        parameters via the name of a ResourceClass that was created
        as part of the driver deployment.
        """
        self._properties["resourceClassName"] = value

    def __enter__(self) -> "ResourceClaimSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimStatus(_kuber_definitions.Definition):
    """
    ResourceClaimStatus tracks whether the resource has been
    allocated and what the resulting attributes are.
    """

    def __init__(
        self,
        allocation: typing.Optional["AllocationResult"] = None,
        deallocation_requested: typing.Optional[bool] = None,
        driver_name: typing.Optional[str] = None,
        reserved_for: typing.Optional[
            typing.List["ResourceClaimConsumerReference"]
        ] = None,
    ):
        """Create ResourceClaimStatus instance."""
        super(ResourceClaimStatus, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimStatus"
        )
        self._properties = {
            "allocation": allocation if allocation is not None else AllocationResult(),
            "deallocationRequested": (
                deallocation_requested if deallocation_requested is not None else None
            ),
            "driverName": driver_name if driver_name is not None else "",
            "reservedFor": reserved_for if reserved_for is not None else [],
        }
        self._types = {
            "allocation": (AllocationResult, None),
            "deallocationRequested": (bool, None),
            "driverName": (str, None),
            "reservedFor": (list, ResourceClaimConsumerReference),
        }

    @property
    def allocation(self) -> "AllocationResult":
        """
        Allocation is set by the resource driver once a resource or
        set of resources has been allocated successfully. If this is
        not specified, the resources have not been allocated yet.
        """
        return typing.cast(
            "AllocationResult",
            self._properties.get("allocation"),
        )

    @allocation.setter
    def allocation(self, value: typing.Union["AllocationResult", dict]):
        """
        Allocation is set by the resource driver once a resource or
        set of resources has been allocated successfully. If this is
        not specified, the resources have not been allocated yet.
        """
        if isinstance(value, dict):
            value = typing.cast(
                AllocationResult,
                AllocationResult().from_dict(value),
            )
        self._properties["allocation"] = value

    @property
    def deallocation_requested(self) -> bool:
        """
        DeallocationRequested indicates that a ResourceClaim is to
        be deallocated.

        The driver then must deallocate this claim and reset the
        field together with clearing the Allocation field.

        While DeallocationRequested is set, no new consumers may be
        added to ReservedFor.
        """
        return typing.cast(
            bool,
            self._properties.get("deallocationRequested"),
        )

    @deallocation_requested.setter
    def deallocation_requested(self, value: bool):
        """
        DeallocationRequested indicates that a ResourceClaim is to
        be deallocated.

        The driver then must deallocate this claim and reset the
        field together with clearing the Allocation field.

        While DeallocationRequested is set, no new consumers may be
        added to ReservedFor.
        """
        self._properties["deallocationRequested"] = value

    @property
    def driver_name(self) -> str:
        """
        DriverName is a copy of the driver name from the
        ResourceClass at the time when allocation started.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName is a copy of the driver name from the
        ResourceClass at the time when allocation started.
        """
        self._properties["driverName"] = value

    @property
    def reserved_for(self) -> typing.List["ResourceClaimConsumerReference"]:
        """
        ReservedFor indicates which entities are currently allowed
        to use the claim. A Pod which references a ResourceClaim
        which is not reserved for that Pod will not be started.

        There can be at most 32 such reservations. This may get
        increased in the future, but not reduced.
        """
        return typing.cast(
            typing.List["ResourceClaimConsumerReference"],
            self._properties.get("reservedFor"),
        )

    @reserved_for.setter
    def reserved_for(
        self,
        value: typing.Union[
            typing.List["ResourceClaimConsumerReference"], typing.List[dict]
        ],
    ):
        """
        ReservedFor indicates which entities are currently allowed
        to use the claim. A Pod which references a ResourceClaim
        which is not reserved for that Pod will not be started.

        There can be at most 32 such reservations. This may get
        increased in the future, but not reduced.
        """
        cleaned: typing.List[ResourceClaimConsumerReference] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaimConsumerReference,
                    ResourceClaimConsumerReference().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaimConsumerReference, item))
        self._properties["reservedFor"] = cleaned

    def __enter__(self) -> "ResourceClaimStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimTemplate(_kuber_definitions.Resource):
    """
    ResourceClaimTemplate is used to produce ResourceClaim
    objects.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceClaimTemplateSpec"] = None,
    ):
        """Create ResourceClaimTemplate instance."""
        super(ResourceClaimTemplate, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimTemplate"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ResourceClaimTemplateSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ResourceClaimTemplateSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ResourceClaimTemplateSpec":
        """
        Describes the ResourceClaim that is to be generated.

        This field is immutable. A ResourceClaim will get created by
        the control plane for a Pod when needed and then not get
        updated anymore.
        """
        return typing.cast(
            "ResourceClaimTemplateSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceClaimTemplateSpec", dict]):
        """
        Describes the ResourceClaim that is to be generated.

        This field is immutable. A ResourceClaim will get created by
        the control plane for a Pod when needed and then not get
        updated anymore.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimTemplateSpec,
                ResourceClaimTemplateSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ResourceClaimTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_resource_claim_template",
            "create_resource_claim_template",
        ]

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
        Replaces the ResourceClaimTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_resource_claim_template",
            "replace_resource_claim_template",
        ]

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
        Patches the ResourceClaimTemplate in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_resource_claim_template",
            "patch_resource_claim_template",
        ]

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
        Reads the ResourceClaimTemplate from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_claim_template",
            "read_resource_claim_template",
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
        Deletes the ResourceClaimTemplate from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_claim_template",
            "delete_resource_claim_template",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimTemplate":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimTemplateList(_kuber_definitions.Collection):
    """
    ResourceClaimTemplateList is a collection of claim
    templates.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClaimTemplate"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClaimTemplateList instance."""
        super(ResourceClaimTemplateList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimTemplateList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClaimTemplate),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClaimTemplate"]:
        """
        Items is the list of resource claim templates.
        """
        return typing.cast(
            typing.List["ResourceClaimTemplate"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["ResourceClaimTemplate"], typing.List[dict]],
    ):
        """
        Items is the list of resource claim templates.
        """
        cleaned: typing.List[ResourceClaimTemplate] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClaimTemplate,
                    ResourceClaimTemplate().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClaimTemplate, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClaimTemplateList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimTemplateSpec(_kuber_definitions.Definition):
    """
    ResourceClaimTemplateSpec contains the metadata and fields
    for a ResourceClaim.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceClaimSpec"] = None,
    ):
        """Create ResourceClaimTemplateSpec instance."""
        super(ResourceClaimTemplateSpec, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClaimTemplateSpec"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ResourceClaimSpec(),
        }
        self._types = {
            "metadata": (ObjectMeta, None),
            "spec": (ResourceClaimSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        ObjectMeta may contain labels and annotations that will be
        copied into the PVC when creating it. No other fields are
        allowed and will be rejected during validation.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        ObjectMeta may contain labels and annotations that will be
        copied into the PVC when creating it. No other fields are
        allowed and will be rejected during validation.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def spec(self) -> "ResourceClaimSpec":
        """
        Spec for the ResourceClaim. The entire content is copied
        unchanged into the ResourceClaim that gets created from this
        template. The same fields as in a ResourceClaim are also
        valid here.
        """
        return typing.cast(
            "ResourceClaimSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceClaimSpec", dict]):
        """
        Spec for the ResourceClaim. The entire content is copied
        unchanged into the ResourceClaim that gets created from this
        template. The same fields as in a ResourceClaim are also
        valid here.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClaimSpec,
                ResourceClaimSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def __enter__(self) -> "ResourceClaimTemplateSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClass(_kuber_definitions.Resource):
    """
    ResourceClass is used by administrators to influence how
    resources are allocated.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        driver_name: typing.Optional[str] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        parameters_ref: typing.Optional["ResourceClassParametersReference"] = None,
        structured_parameters: typing.Optional[bool] = None,
        suitable_nodes: typing.Optional["NodeSelector"] = None,
    ):
        """Create ResourceClass instance."""
        super(ResourceClass, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClass"
        )
        self._properties = {
            "driverName": driver_name if driver_name is not None else "",
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "parametersRef": (
                parameters_ref
                if parameters_ref is not None
                else ResourceClassParametersReference()
            ),
            "structuredParameters": (
                structured_parameters if structured_parameters is not None else None
            ),
            "suitableNodes": (
                suitable_nodes if suitable_nodes is not None else NodeSelector()
            ),
        }
        self._types = {
            "apiVersion": (str, None),
            "driverName": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "parametersRef": (ResourceClassParametersReference, None),
            "structuredParameters": (bool, None),
            "suitableNodes": (NodeSelector, None),
        }

    @property
    def driver_name(self) -> str:
        """
        DriverName defines the name of the dynamic resource driver
        that is used for allocation of a ResourceClaim that uses
        this class.

        Resource drivers have a unique name in forward domain order
        (acme.example.com).
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName defines the name of the dynamic resource driver
        that is used for allocation of a ResourceClaim that uses
        this class.

        Resource drivers have a unique name in forward domain order
        (acme.example.com).
        """
        self._properties["driverName"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def parameters_ref(self) -> "ResourceClassParametersReference":
        """
        ParametersRef references an arbitrary separate object that
        may hold parameters that will be used by the driver when
        allocating a resource that uses this class. A dynamic
        resource driver can distinguish between parameters stored
        here and and those stored in ResourceClaimSpec.
        """
        return typing.cast(
            "ResourceClassParametersReference",
            self._properties.get("parametersRef"),
        )

    @parameters_ref.setter
    def parameters_ref(
        self, value: typing.Union["ResourceClassParametersReference", dict]
    ):
        """
        ParametersRef references an arbitrary separate object that
        may hold parameters that will be used by the driver when
        allocating a resource that uses this class. A dynamic
        resource driver can distinguish between parameters stored
        here and and those stored in ResourceClaimSpec.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClassParametersReference,
                ResourceClassParametersReference().from_dict(value),
            )
        self._properties["parametersRef"] = value

    @property
    def structured_parameters(self) -> bool:
        """
        If and only if allocation of claims using this class is
        handled via structured parameters, then StructuredParameters
        must be set to true.
        """
        return typing.cast(
            bool,
            self._properties.get("structuredParameters"),
        )

    @structured_parameters.setter
    def structured_parameters(self, value: bool):
        """
        If and only if allocation of claims using this class is
        handled via structured parameters, then StructuredParameters
        must be set to true.
        """
        self._properties["structuredParameters"] = value

    @property
    def suitable_nodes(self) -> "NodeSelector":
        """
        Only nodes matching the selector will be considered by the
        scheduler when trying to find a Node that fits a Pod when
        that Pod uses a ResourceClaim that has not been allocated
        yet.

        Setting this field is optional. If null, all nodes are
        candidates.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("suitableNodes"),
        )

    @suitable_nodes.setter
    def suitable_nodes(self, value: typing.Union["NodeSelector", dict]):
        """
        Only nodes matching the selector will be considered by the
        scheduler when trying to find a Node that fits a Pod when
        that Pod uses a ResourceClaim that has not been allocated
        yet.

        Setting this field is optional. If null, all nodes are
        candidates.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["suitableNodes"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ResourceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_resource_class", "create_resource_class"]

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
        Replaces the ResourceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_resource_class", "replace_resource_class"]

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
        Patches the ResourceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_resource_class", "patch_resource_class"]

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
        Reads the ResourceClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_class",
            "read_resource_class",
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
        Deletes the ResourceClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_class",
            "delete_resource_class",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClassList(_kuber_definitions.Collection):
    """
    ResourceClassList is a collection of classes.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClass"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClassList instance."""
        super(ResourceClassList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClass"]:
        """
        Items is the list of resource classes.
        """
        return typing.cast(
            typing.List["ResourceClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ResourceClass"], typing.List[dict]]
    ):
        """
        Items is the list of resource classes.
        """
        cleaned: typing.List[ResourceClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClass,
                    ResourceClass().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClass, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClassParameters(_kuber_definitions.Resource):
    """
    ResourceClassParameters defines resource requests for a
    ResourceClass in an in-tree format understood by Kubernetes.
    """

    def __init__(
        self,
        filters: typing.Optional[typing.List["ResourceFilter"]] = None,
        generated_from: typing.Optional["ResourceClassParametersReference"] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        vendor_parameters: typing.Optional[typing.List["VendorParameters"]] = None,
    ):
        """Create ResourceClassParameters instance."""
        super(ResourceClassParameters, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClassParameters"
        )
        self._properties = {
            "filters": filters if filters is not None else [],
            "generatedFrom": (
                generated_from
                if generated_from is not None
                else ResourceClassParametersReference()
            ),
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "vendorParameters": (
                vendor_parameters if vendor_parameters is not None else []
            ),
        }
        self._types = {
            "apiVersion": (str, None),
            "filters": (list, ResourceFilter),
            "generatedFrom": (ResourceClassParametersReference, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "vendorParameters": (list, VendorParameters),
        }

    @property
    def filters(self) -> typing.List["ResourceFilter"]:
        """
        Filters describes additional contraints that must be met
        when using the class.
        """
        return typing.cast(
            typing.List["ResourceFilter"],
            self._properties.get("filters"),
        )

    @filters.setter
    def filters(
        self, value: typing.Union[typing.List["ResourceFilter"], typing.List[dict]]
    ):
        """
        Filters describes additional contraints that must be met
        when using the class.
        """
        cleaned: typing.List[ResourceFilter] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceFilter,
                    ResourceFilter().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceFilter, item))
        self._properties["filters"] = cleaned

    @property
    def generated_from(self) -> "ResourceClassParametersReference":
        """
        If this object was created from some other resource, then
        this links back to that resource. This field is used to find
        the in-tree representation of the class parameters when the
        parameter reference of the class refers to some unknown
        type.
        """
        return typing.cast(
            "ResourceClassParametersReference",
            self._properties.get("generatedFrom"),
        )

    @generated_from.setter
    def generated_from(
        self, value: typing.Union["ResourceClassParametersReference", dict]
    ):
        """
        If this object was created from some other resource, then
        this links back to that resource. This field is used to find
        the in-tree representation of the class parameters when the
        parameter reference of the class refers to some unknown
        type.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceClassParametersReference,
                ResourceClassParametersReference().from_dict(value),
            )
        self._properties["generatedFrom"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def vendor_parameters(self) -> typing.List["VendorParameters"]:
        """
        VendorParameters are arbitrary setup parameters for all
        claims using this class. They are ignored while allocating
        the claim. There must not be more than one entry per driver.
        """
        return typing.cast(
            typing.List["VendorParameters"],
            self._properties.get("vendorParameters"),
        )

    @vendor_parameters.setter
    def vendor_parameters(
        self, value: typing.Union[typing.List["VendorParameters"], typing.List[dict]]
    ):
        """
        VendorParameters are arbitrary setup parameters for all
        claims using this class. They are ignored while allocating
        the claim. There must not be more than one entry per driver.
        """
        cleaned: typing.List[VendorParameters] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    VendorParameters,
                    VendorParameters().from_dict(item),
                )
            cleaned.append(typing.cast(VendorParameters, item))
        self._properties["vendorParameters"] = cleaned

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ResourceClassParameters in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_resource_class_parameters",
            "create_resource_class_parameters",
        ]

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
        Replaces the ResourceClassParameters in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_resource_class_parameters",
            "replace_resource_class_parameters",
        ]

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
        Patches the ResourceClassParameters in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_resource_class_parameters",
            "patch_resource_class_parameters",
        ]

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
        Reads the ResourceClassParameters from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_class_parameters",
            "read_resource_class_parameters",
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
        Deletes the ResourceClassParameters from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_class_parameters",
            "delete_resource_class_parameters",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClassParameters":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClassParametersList(_kuber_definitions.Collection):
    """
    ResourceClassParametersList is a collection of
    ResourceClassParameters.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceClassParameters"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceClassParametersList instance."""
        super(ResourceClassParametersList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClassParametersList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceClassParameters),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceClassParameters"]:
        """
        Items is the list of node resource capacity objects.
        """
        return typing.cast(
            typing.List["ResourceClassParameters"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[typing.List["ResourceClassParameters"], typing.List[dict]],
    ):
        """
        Items is the list of node resource capacity objects.
        """
        cleaned: typing.List[ResourceClassParameters] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceClassParameters,
                    ResourceClassParameters().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceClassParameters, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceClassParametersList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClassParametersReference(_kuber_definitions.Definition):
    """
    ResourceClassParametersReference contains enough information
    to let you locate the parameters for a ResourceClass.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
    ):
        """Create ResourceClassParametersReference instance."""
        super(ResourceClassParametersReference, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceClassParametersReference"
        )
        self._properties = {
            "apiGroup": api_group if api_group is not None else "",
            "kind": kind if kind is not None else "",
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
        }
        self._types = {
            "apiGroup": (str, None),
            "kind": (str, None),
            "name": (str, None),
            "namespace": (str, None),
        }

    @property
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced. It
        is empty for the core API. This matches the group in the
        APIVersion that is used when creating the resources.
        """
        self._properties["apiGroup"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the type of resource being referenced. This is the
        same value as in the parameter object's metadata.
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        Namespace that contains the referenced resource. Must be
        empty for cluster-scoped resources and non-empty for
        namespaced resources.
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace that contains the referenced resource. Must be
        empty for cluster-scoped resources and non-empty for
        namespaced resources.
        """
        self._properties["namespace"] = value

    def __enter__(self) -> "ResourceClassParametersReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceFilter(_kuber_definitions.Definition):
    """
    ResourceFilter is a filter for resources from one particular
    driver.
    """

    def __init__(
        self,
        driver_name: typing.Optional[str] = None,
        named_resources: typing.Optional["NamedResourcesFilter"] = None,
    ):
        """Create ResourceFilter instance."""
        super(ResourceFilter, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceFilter"
        )
        self._properties = {
            "driverName": driver_name if driver_name is not None else "",
            "namedResources": (
                named_resources
                if named_resources is not None
                else NamedResourcesFilter()
            ),
        }
        self._types = {
            "driverName": (str, None),
            "namedResources": (NamedResourcesFilter, None),
        }

    @property
    def driver_name(self) -> str:
        """
        DriverName is the name used by the DRA driver kubelet
        plugin.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName is the name used by the DRA driver kubelet
        plugin.
        """
        self._properties["driverName"] = value

    @property
    def named_resources(self) -> "NamedResourcesFilter":
        """
        NamedResources describes a resource filter using the named
        resources model.
        """
        return typing.cast(
            "NamedResourcesFilter",
            self._properties.get("namedResources"),
        )

    @named_resources.setter
    def named_resources(self, value: typing.Union["NamedResourcesFilter", dict]):
        """
        NamedResources describes a resource filter using the named
        resources model.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NamedResourcesFilter,
                NamedResourcesFilter().from_dict(value),
            )
        self._properties["namedResources"] = value

    def __enter__(self) -> "ResourceFilter":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceHandle(_kuber_definitions.Definition):
    """
    ResourceHandle holds opaque resource data for processing by
    a specific kubelet plugin.
    """

    def __init__(
        self,
        data: typing.Optional[str] = None,
        driver_name: typing.Optional[str] = None,
        structured_data: typing.Optional["StructuredResourceHandle"] = None,
    ):
        """Create ResourceHandle instance."""
        super(ResourceHandle, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceHandle"
        )
        self._properties = {
            "data": data if data is not None else "",
            "driverName": driver_name if driver_name is not None else "",
            "structuredData": (
                structured_data
                if structured_data is not None
                else StructuredResourceHandle()
            ),
        }
        self._types = {
            "data": (str, None),
            "driverName": (str, None),
            "structuredData": (StructuredResourceHandle, None),
        }

    @property
    def data(self) -> str:
        """
        Data contains the opaque data associated with this
        ResourceHandle. It is set by the controller component of the
        resource driver whose name matches the DriverName set in the
        ResourceClaimStatus this ResourceHandle is embedded in. It
        is set at allocation time and is intended for processing by
        the kubelet plugin whose name matches the DriverName set in
        this ResourceHandle.

        The maximum size of this field is 16KiB. This may get
        increased in the future, but not reduced.
        """
        return typing.cast(
            str,
            self._properties.get("data"),
        )

    @data.setter
    def data(self, value: str):
        """
        Data contains the opaque data associated with this
        ResourceHandle. It is set by the controller component of the
        resource driver whose name matches the DriverName set in the
        ResourceClaimStatus this ResourceHandle is embedded in. It
        is set at allocation time and is intended for processing by
        the kubelet plugin whose name matches the DriverName set in
        this ResourceHandle.

        The maximum size of this field is 16KiB. This may get
        increased in the future, but not reduced.
        """
        self._properties["data"] = value

    @property
    def driver_name(self) -> str:
        """
        DriverName specifies the name of the resource driver whose
        kubelet plugin should be invoked to process this
        ResourceHandle's data once it lands on a node. This may
        differ from the DriverName set in ResourceClaimStatus this
        ResourceHandle is embedded in.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName specifies the name of the resource driver whose
        kubelet plugin should be invoked to process this
        ResourceHandle's data once it lands on a node. This may
        differ from the DriverName set in ResourceClaimStatus this
        ResourceHandle is embedded in.
        """
        self._properties["driverName"] = value

    @property
    def structured_data(self) -> "StructuredResourceHandle":
        """
        If StructuredData is set, then it needs to be used instead
        of Data.
        """
        return typing.cast(
            "StructuredResourceHandle",
            self._properties.get("structuredData"),
        )

    @structured_data.setter
    def structured_data(self, value: typing.Union["StructuredResourceHandle", dict]):
        """
        If StructuredData is set, then it needs to be used instead
        of Data.
        """
        if isinstance(value, dict):
            value = typing.cast(
                StructuredResourceHandle,
                StructuredResourceHandle().from_dict(value),
            )
        self._properties["structuredData"] = value

    def __enter__(self) -> "ResourceHandle":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceRequest(_kuber_definitions.Definition):
    """
    ResourceRequest is a request for resources from one
    particular driver.
    """

    def __init__(
        self,
        named_resources: typing.Optional["NamedResourcesRequest"] = None,
        vendor_parameters: typing.Optional["RawExtension"] = None,
    ):
        """Create ResourceRequest instance."""
        super(ResourceRequest, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceRequest"
        )
        self._properties = {
            "namedResources": (
                named_resources
                if named_resources is not None
                else NamedResourcesRequest()
            ),
            "vendorParameters": (
                vendor_parameters if vendor_parameters is not None else RawExtension()
            ),
        }
        self._types = {
            "namedResources": (NamedResourcesRequest, None),
            "vendorParameters": (RawExtension, None),
        }

    @property
    def named_resources(self) -> "NamedResourcesRequest":
        """
        NamedResources describes a request for resources with the
        named resources model.
        """
        return typing.cast(
            "NamedResourcesRequest",
            self._properties.get("namedResources"),
        )

    @named_resources.setter
    def named_resources(self, value: typing.Union["NamedResourcesRequest", dict]):
        """
        NamedResources describes a request for resources with the
        named resources model.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NamedResourcesRequest,
                NamedResourcesRequest().from_dict(value),
            )
        self._properties["namedResources"] = value

    @property
    def vendor_parameters(self) -> "RawExtension":
        """
        VendorParameters are arbitrary setup parameters for the
        requested resource. They are ignored while allocating a
        claim.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("vendorParameters"),
        )

    @vendor_parameters.setter
    def vendor_parameters(self, value: typing.Union["RawExtension", dict]):
        """
        VendorParameters are arbitrary setup parameters for the
        requested resource. They are ignored while allocating a
        claim.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["vendorParameters"] = value

    def __enter__(self) -> "ResourceRequest":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceSlice(_kuber_definitions.Resource):
    """
    ResourceSlice provides information about available resources
    on individual nodes.
    """

    def __init__(
        self,
        driver_name: typing.Optional[str] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        named_resources: typing.Optional["NamedResourcesResources"] = None,
        node_name: typing.Optional[str] = None,
    ):
        """Create ResourceSlice instance."""
        super(ResourceSlice, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceSlice"
        )
        self._properties = {
            "driverName": driver_name if driver_name is not None else "",
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "namedResources": (
                named_resources
                if named_resources is not None
                else NamedResourcesResources()
            ),
            "nodeName": node_name if node_name is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "driverName": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "namedResources": (NamedResourcesResources, None),
            "nodeName": (str, None),
        }

    @property
    def driver_name(self) -> str:
        """
        DriverName identifies the DRA driver providing the capacity
        information. A field selector can be used to list only
        ResourceSlice objects with a certain driver name.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName identifies the DRA driver providing the capacity
        information. A field selector can be used to list only
        ResourceSlice objects with a certain driver name.
        """
        self._properties["driverName"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def named_resources(self) -> "NamedResourcesResources":
        """
        NamedResources describes available resources using the named
        resources model.
        """
        return typing.cast(
            "NamedResourcesResources",
            self._properties.get("namedResources"),
        )

    @named_resources.setter
    def named_resources(self, value: typing.Union["NamedResourcesResources", dict]):
        """
        NamedResources describes available resources using the named
        resources model.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NamedResourcesResources,
                NamedResourcesResources().from_dict(value),
            )
        self._properties["namedResources"] = value

    @property
    def node_name(self) -> str:
        """
        NodeName identifies the node which provides the resources if
        they are local to a node.

        A field selector can be used to list only ResourceSlice
        objects with a certain node name.
        """
        return typing.cast(
            str,
            self._properties.get("nodeName"),
        )

    @node_name.setter
    def node_name(self, value: str):
        """
        NodeName identifies the node which provides the resources if
        they are local to a node.

        A field selector can be used to list only ResourceSlice
        objects with a certain node name.
        """
        self._properties["nodeName"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ResourceSlice in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_resource_slice", "create_resource_slice"]

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
        Replaces the ResourceSlice in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_resource_slice", "replace_resource_slice"]

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
        Patches the ResourceSlice in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_resource_slice", "patch_resource_slice"]

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
        Reads the ResourceSlice from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_resource_slice",
            "read_resource_slice",
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
        Deletes the ResourceSlice from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_resource_slice",
            "delete_resource_slice",
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceSlice":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceSliceList(_kuber_definitions.Collection):
    """
    ResourceSliceList is a collection of ResourceSlices.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ResourceSlice"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ResourceSliceList instance."""
        super(ResourceSliceList, self).__init__(
            api_version="resource/v1alpha2", kind="ResourceSliceList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ResourceSlice),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ResourceSlice"]:
        """
        Items is the list of node resource capacity objects.
        """
        return typing.cast(
            typing.List["ResourceSlice"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ResourceSlice"], typing.List[dict]]
    ):
        """
        Items is the list of node resource capacity objects.
        """
        cleaned: typing.List[ResourceSlice] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourceSlice,
                    ResourceSlice().from_dict(item),
                )
            cleaned.append(typing.cast(ResourceSlice, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard list metadata
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
    ) -> "client.ResourceV1alpha2Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha2Api(**kwargs)

    def __enter__(self) -> "ResourceSliceList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class StructuredResourceHandle(_kuber_definitions.Definition):
    """
    StructuredResourceHandle is the in-tree representation of
    the allocation result.
    """

    def __init__(
        self,
        node_name: typing.Optional[str] = None,
        results: typing.Optional[typing.List["DriverAllocationResult"]] = None,
        vendor_claim_parameters: typing.Optional["RawExtension"] = None,
        vendor_class_parameters: typing.Optional["RawExtension"] = None,
    ):
        """Create StructuredResourceHandle instance."""
        super(StructuredResourceHandle, self).__init__(
            api_version="resource/v1alpha2", kind="StructuredResourceHandle"
        )
        self._properties = {
            "nodeName": node_name if node_name is not None else "",
            "results": results if results is not None else [],
            "vendorClaimParameters": (
                vendor_claim_parameters
                if vendor_claim_parameters is not None
                else RawExtension()
            ),
            "vendorClassParameters": (
                vendor_class_parameters
                if vendor_class_parameters is not None
                else RawExtension()
            ),
        }
        self._types = {
            "nodeName": (str, None),
            "results": (list, DriverAllocationResult),
            "vendorClaimParameters": (RawExtension, None),
            "vendorClassParameters": (RawExtension, None),
        }

    @property
    def node_name(self) -> str:
        """
        NodeName is the name of the node providing the necessary
        resources if the resources are local to a node.
        """
        return typing.cast(
            str,
            self._properties.get("nodeName"),
        )

    @node_name.setter
    def node_name(self, value: str):
        """
        NodeName is the name of the node providing the necessary
        resources if the resources are local to a node.
        """
        self._properties["nodeName"] = value

    @property
    def results(self) -> typing.List["DriverAllocationResult"]:
        """
        Results lists all allocated driver resources.
        """
        return typing.cast(
            typing.List["DriverAllocationResult"],
            self._properties.get("results"),
        )

    @results.setter
    def results(
        self,
        value: typing.Union[typing.List["DriverAllocationResult"], typing.List[dict]],
    ):
        """
        Results lists all allocated driver resources.
        """
        cleaned: typing.List[DriverAllocationResult] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DriverAllocationResult,
                    DriverAllocationResult().from_dict(item),
                )
            cleaned.append(typing.cast(DriverAllocationResult, item))
        self._properties["results"] = cleaned

    @property
    def vendor_claim_parameters(self) -> "RawExtension":
        """
        VendorClaimParameters are the per-claim configuration
        parameters from the resource claim parameters at the time
        that the claim was allocated.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("vendorClaimParameters"),
        )

    @vendor_claim_parameters.setter
    def vendor_claim_parameters(self, value: typing.Union["RawExtension", dict]):
        """
        VendorClaimParameters are the per-claim configuration
        parameters from the resource claim parameters at the time
        that the claim was allocated.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["vendorClaimParameters"] = value

    @property
    def vendor_class_parameters(self) -> "RawExtension":
        """
        VendorClassParameters are the per-claim configuration
        parameters from the resource class at the time that the
        claim was allocated.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("vendorClassParameters"),
        )

    @vendor_class_parameters.setter
    def vendor_class_parameters(self, value: typing.Union["RawExtension", dict]):
        """
        VendorClassParameters are the per-claim configuration
        parameters from the resource class at the time that the
        claim was allocated.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["vendorClassParameters"] = value

    def __enter__(self) -> "StructuredResourceHandle":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VendorParameters(_kuber_definitions.Definition):
    """
    VendorParameters are opaque parameters for one particular
    driver.
    """

    def __init__(
        self,
        driver_name: typing.Optional[str] = None,
        parameters: typing.Optional["RawExtension"] = None,
    ):
        """Create VendorParameters instance."""
        super(VendorParameters, self).__init__(
            api_version="resource/v1alpha2", kind="VendorParameters"
        )
        self._properties = {
            "driverName": driver_name if driver_name is not None else "",
            "parameters": parameters if parameters is not None else RawExtension(),
        }
        self._types = {
            "driverName": (str, None),
            "parameters": (RawExtension, None),
        }

    @property
    def driver_name(self) -> str:
        """
        DriverName is the name used by the DRA driver kubelet
        plugin.
        """
        return typing.cast(
            str,
            self._properties.get("driverName"),
        )

    @driver_name.setter
    def driver_name(self, value: str):
        """
        DriverName is the name used by the DRA driver kubelet
        plugin.
        """
        self._properties["driverName"] = value

    @property
    def parameters(self) -> "RawExtension":
        """
        Parameters can be arbitrary setup parameters. They are
        ignored while allocating a claim.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("parameters"),
        )

    @parameters.setter
    def parameters(self, value: typing.Union["RawExtension", dict]):
        """
        Parameters can be arbitrary setup parameters. They are
        ignored while allocating a claim.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["parameters"] = value

    def __enter__(self) -> "VendorParameters":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
