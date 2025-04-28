import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_31.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_31.core_v1 import NodeSelector  # noqa: F401
from kuber.v1_31.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_31.apimachinery_runtime import RawExtension  # noqa: F401
from kuber.v1_31.meta_v1 import Status  # noqa: F401
from kuber.v1_31.meta_v1 import StatusDetails  # noqa: F401


class AllocationResult(_kuber_definitions.Definition):
    """
    AllocationResult contains attributes of an allocated
    resource.
    """

    def __init__(
        self,
        controller: typing.Optional[str] = None,
        devices: typing.Optional["DeviceAllocationResult"] = None,
        node_selector: typing.Optional["NodeSelector"] = None,
    ):
        """Create AllocationResult instance."""
        super(AllocationResult, self).__init__(
            api_version="resource/v1alpha3", kind="AllocationResult"
        )
        self._properties = {
            "controller": controller if controller is not None else "",
            "devices": devices if devices is not None else DeviceAllocationResult(),
            "nodeSelector": (
                node_selector if node_selector is not None else NodeSelector()
            ),
        }
        self._types = {
            "controller": (str, None),
            "devices": (DeviceAllocationResult, None),
            "nodeSelector": (NodeSelector, None),
        }

    @property
    def controller(self) -> str:
        """
        Controller is the name of the DRA driver which handled the
        allocation. That driver is also responsible for deallocating
        the claim. It is empty when the claim can be deallocated
        without involving a driver.

        A driver may allocate devices provided by other drivers, so
        this driver name here can be different from the driver names
        listed for the results.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
        """
        return typing.cast(
            str,
            self._properties.get("controller"),
        )

    @controller.setter
    def controller(self, value: str):
        """
        Controller is the name of the DRA driver which handled the
        allocation. That driver is also responsible for deallocating
        the claim. It is empty when the claim can be deallocated
        without involving a driver.

        A driver may allocate devices provided by other drivers, so
        this driver name here can be different from the driver names
        listed for the results.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
        """
        self._properties["controller"] = value

    @property
    def devices(self) -> "DeviceAllocationResult":
        """
        Devices is the result of allocating devices.
        """
        return typing.cast(
            "DeviceAllocationResult",
            self._properties.get("devices"),
        )

    @devices.setter
    def devices(self, value: typing.Union["DeviceAllocationResult", dict]):
        """
        Devices is the result of allocating devices.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeviceAllocationResult,
                DeviceAllocationResult().from_dict(value),
            )
        self._properties["devices"] = value

    @property
    def node_selector(self) -> "NodeSelector":
        """
        NodeSelector defines where the allocated resources are
        available. If unset, they are available everywhere.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("nodeSelector"),
        )

    @node_selector.setter
    def node_selector(self, value: typing.Union["NodeSelector", dict]):
        """
        NodeSelector defines where the allocated resources are
        available. If unset, they are available everywhere.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["nodeSelector"] = value

    def __enter__(self) -> "AllocationResult":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class BasicDevice(_kuber_definitions.Definition):
    """
    BasicDevice defines one device instance.
    """

    def __init__(
        self,
        attributes: typing.Optional[dict] = None,
        capacity: typing.Optional[dict] = None,
    ):
        """Create BasicDevice instance."""
        super(BasicDevice, self).__init__(
            api_version="resource/v1alpha3", kind="BasicDevice"
        )
        self._properties = {
            "attributes": attributes if attributes is not None else {},
            "capacity": capacity if capacity is not None else {},
        }
        self._types = {
            "attributes": (dict, None),
            "capacity": (dict, None),
        }

    @property
    def attributes(self) -> dict:
        """
        Attributes defines the set of attributes for this device.
        The name of each attribute must be unique in that set.

        The maximum number of attributes and capacities combined is
        32.
        """
        return typing.cast(
            dict,
            self._properties.get("attributes"),
        )

    @attributes.setter
    def attributes(self, value: dict):
        """
        Attributes defines the set of attributes for this device.
        The name of each attribute must be unique in that set.

        The maximum number of attributes and capacities combined is
        32.
        """
        self._properties["attributes"] = value

    @property
    def capacity(self) -> dict:
        """
        Capacity defines the set of capacities for this device. The
        name of each capacity must be unique in that set.

        The maximum number of attributes and capacities combined is
        32.
        """
        return typing.cast(
            dict,
            self._properties.get("capacity"),
        )

    @capacity.setter
    def capacity(self, value: dict):
        """
        Capacity defines the set of capacities for this device. The
        name of each capacity must be unique in that set.

        The maximum number of attributes and capacities combined is
        32.
        """
        self._properties["capacity"] = value

    def __enter__(self) -> "BasicDevice":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CELDeviceSelector(_kuber_definitions.Definition):
    """
    CELDeviceSelector contains a CEL expression for selecting a
    device.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
    ):
        """Create CELDeviceSelector instance."""
        super(CELDeviceSelector, self).__init__(
            api_version="resource/v1alpha3", kind="CELDeviceSelector"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
        }
        self._types = {
            "expression": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        Expression is a CEL expression which evaluates a single
        device. It must evaluate to true when the device under
        consideration satisfies the desired criteria, and false when
        it does not. Any other result is an error and causes
        allocation of devices to abort.

        The expression's input is an object named "device", which
        carries the following properties:
         - driver (string): the name of the driver which defines
        this device.
         - attributes (map[string]object): the device's attributes,
        grouped by prefix
           (e.g. device.attributes["dra.example.com"] evaluates to
        an object with all
           of the attributes which were prefixed by
        "dra.example.com".
         - capacity (map[string]object): the device's capacities,
        grouped by prefix.

        Example: Consider a device with driver="dra.example.com",
        which exposes two attributes named "model" and
        "ext.example.com/family" and which exposes one capacity
        named "modules". This input to this expression would have
        the following fields:

            device.driver
            device.attributes["dra.example.com"].model
            device.attributes["ext.example.com"].family
            device.capacity["dra.example.com"].modules

        The device.driver field can be used to check for a specific
        driver, either as a high-level precondition (i.e. you only
        want to consider devices from this driver) or as part of a
        multi-clause expression that is meant to consider devices
        from different drivers.

        The value type of each attribute is defined by the device
        definition, and users who write these expressions must
        consult the documentation for their specific drivers. The
        value type of each capacity is Quantity.

        If an unknown prefix is used as a lookup in either
        device.attributes or device.capacity, an empty map will be
        returned. Any reference to an unknown field will cause an
        evaluation error and allocation to abort.

        A robust expression should check for the existence of
        attributes before referencing them.

        For ease of use, the cel.bind() function is enabled, and can
        be used to simplify expressions that access multiple
        attributes with the same domain. For example:

            cel.bind(dra, device.attributes["dra.example.com"],
        dra.someBool && dra.anotherBool)
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        Expression is a CEL expression which evaluates a single
        device. It must evaluate to true when the device under
        consideration satisfies the desired criteria, and false when
        it does not. Any other result is an error and causes
        allocation of devices to abort.

        The expression's input is an object named "device", which
        carries the following properties:
         - driver (string): the name of the driver which defines
        this device.
         - attributes (map[string]object): the device's attributes,
        grouped by prefix
           (e.g. device.attributes["dra.example.com"] evaluates to
        an object with all
           of the attributes which were prefixed by
        "dra.example.com".
         - capacity (map[string]object): the device's capacities,
        grouped by prefix.

        Example: Consider a device with driver="dra.example.com",
        which exposes two attributes named "model" and
        "ext.example.com/family" and which exposes one capacity
        named "modules". This input to this expression would have
        the following fields:

            device.driver
            device.attributes["dra.example.com"].model
            device.attributes["ext.example.com"].family
            device.capacity["dra.example.com"].modules

        The device.driver field can be used to check for a specific
        driver, either as a high-level precondition (i.e. you only
        want to consider devices from this driver) or as part of a
        multi-clause expression that is meant to consider devices
        from different drivers.

        The value type of each attribute is defined by the device
        definition, and users who write these expressions must
        consult the documentation for their specific drivers. The
        value type of each capacity is Quantity.

        If an unknown prefix is used as a lookup in either
        device.attributes or device.capacity, an empty map will be
        returned. Any reference to an unknown field will cause an
        evaluation error and allocation to abort.

        A robust expression should check for the existence of
        attributes before referencing them.

        For ease of use, the cel.bind() function is enabled, and can
        be used to simplify expressions that access multiple
        attributes with the same domain. For example:

            cel.bind(dra, device.attributes["dra.example.com"],
        dra.someBool && dra.anotherBool)
        """
        self._properties["expression"] = value

    def __enter__(self) -> "CELDeviceSelector":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Device(_kuber_definitions.Definition):
    """
    Device represents one individual hardware instance that can
    be selected based on its attributes. Besides the name,
    exactly one field must be set.
    """

    def __init__(
        self,
        basic: typing.Optional["BasicDevice"] = None,
        name: typing.Optional[str] = None,
    ):
        """Create Device instance."""
        super(Device, self).__init__(api_version="resource/v1alpha3", kind="Device")
        self._properties = {
            "basic": basic if basic is not None else BasicDevice(),
            "name": name if name is not None else "",
        }
        self._types = {
            "basic": (BasicDevice, None),
            "name": (str, None),
        }

    @property
    def basic(self) -> "BasicDevice":
        """
        Basic defines one device instance.
        """
        return typing.cast(
            "BasicDevice",
            self._properties.get("basic"),
        )

    @basic.setter
    def basic(self, value: typing.Union["BasicDevice", dict]):
        """
        Basic defines one device instance.
        """
        if isinstance(value, dict):
            value = typing.cast(
                BasicDevice,
                BasicDevice().from_dict(value),
            )
        self._properties["basic"] = value

    @property
    def name(self) -> str:
        """
        Name is unique identifier among all devices managed by the
        driver in the pool. It must be a DNS label.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is unique identifier among all devices managed by the
        driver in the pool. It must be a DNS label.
        """
        self._properties["name"] = value

    def __enter__(self) -> "Device":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceAllocationConfiguration(_kuber_definitions.Definition):
    """
    DeviceAllocationConfiguration gets embedded in an
    AllocationResult.
    """

    def __init__(
        self,
        opaque: typing.Optional["OpaqueDeviceConfiguration"] = None,
        requests: typing.Optional[typing.List[str]] = None,
        source: typing.Optional[str] = None,
    ):
        """Create DeviceAllocationConfiguration instance."""
        super(DeviceAllocationConfiguration, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceAllocationConfiguration"
        )
        self._properties = {
            "opaque": opaque if opaque is not None else OpaqueDeviceConfiguration(),
            "requests": requests if requests is not None else [],
            "source": source if source is not None else "",
        }
        self._types = {
            "opaque": (OpaqueDeviceConfiguration, None),
            "requests": (list, str),
            "source": (str, None),
        }

    @property
    def opaque(self) -> "OpaqueDeviceConfiguration":
        """
        Opaque provides driver-specific configuration parameters.
        """
        return typing.cast(
            "OpaqueDeviceConfiguration",
            self._properties.get("opaque"),
        )

    @opaque.setter
    def opaque(self, value: typing.Union["OpaqueDeviceConfiguration", dict]):
        """
        Opaque provides driver-specific configuration parameters.
        """
        if isinstance(value, dict):
            value = typing.cast(
                OpaqueDeviceConfiguration,
                OpaqueDeviceConfiguration().from_dict(value),
            )
        self._properties["opaque"] = value

    @property
    def requests(self) -> typing.List[str]:
        """
        Requests lists the names of requests where the configuration
        applies. If empty, its applies to all requests.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("requests"),
        )

    @requests.setter
    def requests(self, value: typing.List[str]):
        """
        Requests lists the names of requests where the configuration
        applies. If empty, its applies to all requests.
        """
        self._properties["requests"] = value

    @property
    def source(self) -> str:
        """
        Source records whether the configuration comes from a class
        and thus is not something that a normal user would have been
        able to set or from a claim.
        """
        return typing.cast(
            str,
            self._properties.get("source"),
        )

    @source.setter
    def source(self, value: str):
        """
        Source records whether the configuration comes from a class
        and thus is not something that a normal user would have been
        able to set or from a claim.
        """
        self._properties["source"] = value

    def __enter__(self) -> "DeviceAllocationConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceAllocationResult(_kuber_definitions.Definition):
    """
    DeviceAllocationResult is the result of allocating devices.
    """

    def __init__(
        self,
        config: typing.Optional[typing.List["DeviceAllocationConfiguration"]] = None,
        results: typing.Optional[typing.List["DeviceRequestAllocationResult"]] = None,
    ):
        """Create DeviceAllocationResult instance."""
        super(DeviceAllocationResult, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceAllocationResult"
        )
        self._properties = {
            "config": config if config is not None else [],
            "results": results if results is not None else [],
        }
        self._types = {
            "config": (list, DeviceAllocationConfiguration),
            "results": (list, DeviceRequestAllocationResult),
        }

    @property
    def config(self) -> typing.List["DeviceAllocationConfiguration"]:
        """
        This field is a combination of all the claim and class
        configuration parameters. Drivers can distinguish between
        those based on a flag.

        This includes configuration parameters for drivers which
        have no allocated devices in the result because it is up to
        the drivers which configuration parameters they support.
        They can silently ignore unknown configuration parameters.
        """
        return typing.cast(
            typing.List["DeviceAllocationConfiguration"],
            self._properties.get("config"),
        )

    @config.setter
    def config(
        self,
        value: typing.Union[
            typing.List["DeviceAllocationConfiguration"], typing.List[dict]
        ],
    ):
        """
        This field is a combination of all the claim and class
        configuration parameters. Drivers can distinguish between
        those based on a flag.

        This includes configuration parameters for drivers which
        have no allocated devices in the result because it is up to
        the drivers which configuration parameters they support.
        They can silently ignore unknown configuration parameters.
        """
        cleaned: typing.List[DeviceAllocationConfiguration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceAllocationConfiguration,
                    DeviceAllocationConfiguration().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceAllocationConfiguration, item))
        self._properties["config"] = cleaned

    @property
    def results(self) -> typing.List["DeviceRequestAllocationResult"]:
        """
        Results lists all allocated devices.
        """
        return typing.cast(
            typing.List["DeviceRequestAllocationResult"],
            self._properties.get("results"),
        )

    @results.setter
    def results(
        self,
        value: typing.Union[
            typing.List["DeviceRequestAllocationResult"], typing.List[dict]
        ],
    ):
        """
        Results lists all allocated devices.
        """
        cleaned: typing.List[DeviceRequestAllocationResult] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceRequestAllocationResult,
                    DeviceRequestAllocationResult().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceRequestAllocationResult, item))
        self._properties["results"] = cleaned

    def __enter__(self) -> "DeviceAllocationResult":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceAttribute(_kuber_definitions.Definition):
    """
    DeviceAttribute must have exactly one field set.
    """

    def __init__(
        self,
        bool_: typing.Optional[bool] = None,
        int_: typing.Optional[int] = None,
        string: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
    ):
        """Create DeviceAttribute instance."""
        super(DeviceAttribute, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceAttribute"
        )
        self._properties = {
            "bool": bool_ if bool_ is not None else None,
            "int": int_ if int_ is not None else None,
            "string": string if string is not None else "",
            "version": version if version is not None else "",
        }
        self._types = {
            "bool": (bool, None),
            "int": (int, None),
            "string": (str, None),
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
        IntValue is a number.
        """
        return typing.cast(
            int,
            self._properties.get("int"),
        )

    @int_.setter
    def int_(self, value: int):
        """
        IntValue is a number.
        """
        self._properties["int"] = value

    @property
    def string(self) -> str:
        """
        StringValue is a string. Must not be longer than 64
        characters.
        """
        return typing.cast(
            str,
            self._properties.get("string"),
        )

    @string.setter
    def string(self, value: str):
        """
        StringValue is a string. Must not be longer than 64
        characters.
        """
        self._properties["string"] = value

    @property
    def version(self) -> str:
        """
        VersionValue is a semantic version according to semver.org
        spec 2.0.0. Must not be longer than 64 characters.
        """
        return typing.cast(
            str,
            self._properties.get("version"),
        )

    @version.setter
    def version(self, value: str):
        """
        VersionValue is a semantic version according to semver.org
        spec 2.0.0. Must not be longer than 64 characters.
        """
        self._properties["version"] = value

    def __enter__(self) -> "DeviceAttribute":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceClaim(_kuber_definitions.Definition):
    """
    DeviceClaim defines how to request devices with a
    ResourceClaim.
    """

    def __init__(
        self,
        config: typing.Optional[typing.List["DeviceClaimConfiguration"]] = None,
        constraints: typing.Optional[typing.List["DeviceConstraint"]] = None,
        requests: typing.Optional[typing.List["DeviceRequest"]] = None,
    ):
        """Create DeviceClaim instance."""
        super(DeviceClaim, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceClaim"
        )
        self._properties = {
            "config": config if config is not None else [],
            "constraints": constraints if constraints is not None else [],
            "requests": requests if requests is not None else [],
        }
        self._types = {
            "config": (list, DeviceClaimConfiguration),
            "constraints": (list, DeviceConstraint),
            "requests": (list, DeviceRequest),
        }

    @property
    def config(self) -> typing.List["DeviceClaimConfiguration"]:
        """
        This field holds configuration for multiple potential
        drivers which could satisfy requests in this claim. It is
        ignored while allocating the claim.
        """
        return typing.cast(
            typing.List["DeviceClaimConfiguration"],
            self._properties.get("config"),
        )

    @config.setter
    def config(
        self,
        value: typing.Union[typing.List["DeviceClaimConfiguration"], typing.List[dict]],
    ):
        """
        This field holds configuration for multiple potential
        drivers which could satisfy requests in this claim. It is
        ignored while allocating the claim.
        """
        cleaned: typing.List[DeviceClaimConfiguration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceClaimConfiguration,
                    DeviceClaimConfiguration().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceClaimConfiguration, item))
        self._properties["config"] = cleaned

    @property
    def constraints(self) -> typing.List["DeviceConstraint"]:
        """
        These constraints must be satisfied by the set of devices
        that get allocated for the claim.
        """
        return typing.cast(
            typing.List["DeviceConstraint"],
            self._properties.get("constraints"),
        )

    @constraints.setter
    def constraints(
        self, value: typing.Union[typing.List["DeviceConstraint"], typing.List[dict]]
    ):
        """
        These constraints must be satisfied by the set of devices
        that get allocated for the claim.
        """
        cleaned: typing.List[DeviceConstraint] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceConstraint,
                    DeviceConstraint().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceConstraint, item))
        self._properties["constraints"] = cleaned

    @property
    def requests(self) -> typing.List["DeviceRequest"]:
        """
        Requests represent individual requests for distinct devices
        which must all be satisfied. If empty, nothing needs to be
        allocated.
        """
        return typing.cast(
            typing.List["DeviceRequest"],
            self._properties.get("requests"),
        )

    @requests.setter
    def requests(
        self, value: typing.Union[typing.List["DeviceRequest"], typing.List[dict]]
    ):
        """
        Requests represent individual requests for distinct devices
        which must all be satisfied. If empty, nothing needs to be
        allocated.
        """
        cleaned: typing.List[DeviceRequest] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceRequest,
                    DeviceRequest().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceRequest, item))
        self._properties["requests"] = cleaned

    def __enter__(self) -> "DeviceClaim":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceClaimConfiguration(_kuber_definitions.Definition):
    """
    DeviceClaimConfiguration is used for configuration
    parameters in DeviceClaim.
    """

    def __init__(
        self,
        opaque: typing.Optional["OpaqueDeviceConfiguration"] = None,
        requests: typing.Optional[typing.List[str]] = None,
    ):
        """Create DeviceClaimConfiguration instance."""
        super(DeviceClaimConfiguration, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceClaimConfiguration"
        )
        self._properties = {
            "opaque": opaque if opaque is not None else OpaqueDeviceConfiguration(),
            "requests": requests if requests is not None else [],
        }
        self._types = {
            "opaque": (OpaqueDeviceConfiguration, None),
            "requests": (list, str),
        }

    @property
    def opaque(self) -> "OpaqueDeviceConfiguration":
        """
        Opaque provides driver-specific configuration parameters.
        """
        return typing.cast(
            "OpaqueDeviceConfiguration",
            self._properties.get("opaque"),
        )

    @opaque.setter
    def opaque(self, value: typing.Union["OpaqueDeviceConfiguration", dict]):
        """
        Opaque provides driver-specific configuration parameters.
        """
        if isinstance(value, dict):
            value = typing.cast(
                OpaqueDeviceConfiguration,
                OpaqueDeviceConfiguration().from_dict(value),
            )
        self._properties["opaque"] = value

    @property
    def requests(self) -> typing.List[str]:
        """
        Requests lists the names of requests where the configuration
        applies. If empty, it applies to all requests.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("requests"),
        )

    @requests.setter
    def requests(self, value: typing.List[str]):
        """
        Requests lists the names of requests where the configuration
        applies. If empty, it applies to all requests.
        """
        self._properties["requests"] = value

    def __enter__(self) -> "DeviceClaimConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceClass(_kuber_definitions.Resource):
    """
    DeviceClass is a vendor- or admin-provided resource that
    contains device configuration and selectors. It can be
    referenced in the device requests of a claim to apply these
    presets. Cluster scoped.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["DeviceClassSpec"] = None,
    ):
        """Create DeviceClass instance."""
        super(DeviceClass, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceClass"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else DeviceClassSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (DeviceClassSpec, None),
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
    def spec(self) -> "DeviceClassSpec":
        """
        Spec defines what can be allocated and how to configure it.

        This is mutable. Consumers have to be prepared for classes
        changing at any time, either because they get updated or
        replaced. Claim allocations are done once based on whatever
        was set in classes at the time of allocation.

        Changing the spec automatically increments the
        metadata.generation number.
        """
        return typing.cast(
            "DeviceClassSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["DeviceClassSpec", dict]):
        """
        Spec defines what can be allocated and how to configure it.

        This is mutable. Consumers have to be prepared for classes
        changing at any time, either because they get updated or
        replaced. Claim allocations are done once based on whatever
        was set in classes at the time of allocation.

        Changing the spec automatically increments the
        metadata.generation number.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeviceClassSpec,
                DeviceClassSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the DeviceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_device_class", "create_device_class"]

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
        Replaces the DeviceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_device_class", "replace_device_class"]

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
        Patches the DeviceClass in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_device_class", "patch_device_class"]

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
        Reads the DeviceClass from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_device_class",
            "read_device_class",
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
        Deletes the DeviceClass from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_device_class",
            "delete_device_class",
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

    def __enter__(self) -> "DeviceClass":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceClassConfiguration(_kuber_definitions.Definition):
    """
    DeviceClassConfiguration is used in DeviceClass.
    """

    def __init__(
        self,
        opaque: typing.Optional["OpaqueDeviceConfiguration"] = None,
    ):
        """Create DeviceClassConfiguration instance."""
        super(DeviceClassConfiguration, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceClassConfiguration"
        )
        self._properties = {
            "opaque": opaque if opaque is not None else OpaqueDeviceConfiguration(),
        }
        self._types = {
            "opaque": (OpaqueDeviceConfiguration, None),
        }

    @property
    def opaque(self) -> "OpaqueDeviceConfiguration":
        """
        Opaque provides driver-specific configuration parameters.
        """
        return typing.cast(
            "OpaqueDeviceConfiguration",
            self._properties.get("opaque"),
        )

    @opaque.setter
    def opaque(self, value: typing.Union["OpaqueDeviceConfiguration", dict]):
        """
        Opaque provides driver-specific configuration parameters.
        """
        if isinstance(value, dict):
            value = typing.cast(
                OpaqueDeviceConfiguration,
                OpaqueDeviceConfiguration().from_dict(value),
            )
        self._properties["opaque"] = value

    def __enter__(self) -> "DeviceClassConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceClassList(_kuber_definitions.Collection):
    """
    DeviceClassList is a collection of classes.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["DeviceClass"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create DeviceClassList instance."""
        super(DeviceClassList, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceClassList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, DeviceClass),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["DeviceClass"]:
        """
        Items is the list of resource classes.
        """
        return typing.cast(
            typing.List["DeviceClass"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["DeviceClass"], typing.List[dict]]):
        """
        Items is the list of resource classes.
        """
        cleaned: typing.List[DeviceClass] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceClass,
                    DeviceClass().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceClass, item))
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

    def __enter__(self) -> "DeviceClassList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceClassSpec(_kuber_definitions.Definition):
    """
    DeviceClassSpec is used in a [DeviceClass] to define what
    can be allocated and how to configure it.
    """

    def __init__(
        self,
        config: typing.Optional[typing.List["DeviceClassConfiguration"]] = None,
        selectors: typing.Optional[typing.List["DeviceSelector"]] = None,
        suitable_nodes: typing.Optional["NodeSelector"] = None,
    ):
        """Create DeviceClassSpec instance."""
        super(DeviceClassSpec, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceClassSpec"
        )
        self._properties = {
            "config": config if config is not None else [],
            "selectors": selectors if selectors is not None else [],
            "suitableNodes": (
                suitable_nodes if suitable_nodes is not None else NodeSelector()
            ),
        }
        self._types = {
            "config": (list, DeviceClassConfiguration),
            "selectors": (list, DeviceSelector),
            "suitableNodes": (NodeSelector, None),
        }

    @property
    def config(self) -> typing.List["DeviceClassConfiguration"]:
        """
        Config defines configuration parameters that apply to each
        device that is claimed via this class. Some classses may
        potentially be satisfied by multiple drivers, so each
        instance of a vendor configuration applies to exactly one
        driver.

        They are passed to the driver, but are not considered while
        allocating the claim.
        """
        return typing.cast(
            typing.List["DeviceClassConfiguration"],
            self._properties.get("config"),
        )

    @config.setter
    def config(
        self,
        value: typing.Union[typing.List["DeviceClassConfiguration"], typing.List[dict]],
    ):
        """
        Config defines configuration parameters that apply to each
        device that is claimed via this class. Some classses may
        potentially be satisfied by multiple drivers, so each
        instance of a vendor configuration applies to exactly one
        driver.

        They are passed to the driver, but are not considered while
        allocating the claim.
        """
        cleaned: typing.List[DeviceClassConfiguration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceClassConfiguration,
                    DeviceClassConfiguration().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceClassConfiguration, item))
        self._properties["config"] = cleaned

    @property
    def selectors(self) -> typing.List["DeviceSelector"]:
        """
        Each selector must be satisfied by a device which is claimed
        via this class.
        """
        return typing.cast(
            typing.List["DeviceSelector"],
            self._properties.get("selectors"),
        )

    @selectors.setter
    def selectors(
        self, value: typing.Union[typing.List["DeviceSelector"], typing.List[dict]]
    ):
        """
        Each selector must be satisfied by a device which is claimed
        via this class.
        """
        cleaned: typing.List[DeviceSelector] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceSelector,
                    DeviceSelector().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceSelector, item))
        self._properties["selectors"] = cleaned

    @property
    def suitable_nodes(self) -> "NodeSelector":
        """
        Only nodes matching the selector will be considered by the
        scheduler when trying to find a Node that fits a Pod when
        that Pod uses a claim that has not been allocated yet *and*
        that claim gets allocated through a control plane
        controller. It is ignored when the claim does not use a
        control plane controller for allocation.

        Setting this field is optional. If unset, all Nodes are
        candidates.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
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
        that Pod uses a claim that has not been allocated yet *and*
        that claim gets allocated through a control plane
        controller. It is ignored when the claim does not use a
        control plane controller for allocation.

        Setting this field is optional. If unset, all Nodes are
        candidates.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["suitableNodes"] = value

    def __enter__(self) -> "DeviceClassSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceConstraint(_kuber_definitions.Definition):
    """
    DeviceConstraint must have exactly one field set besides
    Requests.
    """

    def __init__(
        self,
        match_attribute: typing.Optional[str] = None,
        requests: typing.Optional[typing.List[str]] = None,
    ):
        """Create DeviceConstraint instance."""
        super(DeviceConstraint, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceConstraint"
        )
        self._properties = {
            "matchAttribute": match_attribute if match_attribute is not None else "",
            "requests": requests if requests is not None else [],
        }
        self._types = {
            "matchAttribute": (str, None),
            "requests": (list, str),
        }

    @property
    def match_attribute(self) -> str:
        """
        MatchAttribute requires that all devices in question have
        this attribute and that its type and value are the same
        across those devices.

        For example, if you specified "dra.example.com/numa" (a
        hypothetical example!), then only devices in the same NUMA
        node will be chosen. A device which does not have that
        attribute will not be chosen. All devices should use a value
        of the same type for this attribute because that is part of
        its specification, but if one device doesn't, then it also
        will not be chosen.

        Must include the domain qualifier.
        """
        return typing.cast(
            str,
            self._properties.get("matchAttribute"),
        )

    @match_attribute.setter
    def match_attribute(self, value: str):
        """
        MatchAttribute requires that all devices in question have
        this attribute and that its type and value are the same
        across those devices.

        For example, if you specified "dra.example.com/numa" (a
        hypothetical example!), then only devices in the same NUMA
        node will be chosen. A device which does not have that
        attribute will not be chosen. All devices should use a value
        of the same type for this attribute because that is part of
        its specification, but if one device doesn't, then it also
        will not be chosen.

        Must include the domain qualifier.
        """
        self._properties["matchAttribute"] = value

    @property
    def requests(self) -> typing.List[str]:
        """
        Requests is a list of the one or more requests in this claim
        which must co-satisfy this constraint. If a request is
        fulfilled by multiple devices, then all of the devices must
        satisfy the constraint. If this is not specified, this
        constraint applies to all requests in this claim.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("requests"),
        )

    @requests.setter
    def requests(self, value: typing.List[str]):
        """
        Requests is a list of the one or more requests in this claim
        which must co-satisfy this constraint. If a request is
        fulfilled by multiple devices, then all of the devices must
        satisfy the constraint. If this is not specified, this
        constraint applies to all requests in this claim.
        """
        self._properties["requests"] = value

    def __enter__(self) -> "DeviceConstraint":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceRequest(_kuber_definitions.Definition):
    """
    DeviceRequest is a request for devices required for a claim.
    This is typically a request for a single resource like a
    device, but can also ask for several identical devices.

    A DeviceClassName is currently required. Clients must check
    that it is indeed set. It's absence indicates that something
    changed in a way that is not supported by the client yet, in
    which case it must refuse to handle the request.
    """

    def __init__(
        self,
        admin_access: typing.Optional[bool] = None,
        allocation_mode: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        device_class_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        selectors: typing.Optional[typing.List["DeviceSelector"]] = None,
    ):
        """Create DeviceRequest instance."""
        super(DeviceRequest, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceRequest"
        )
        self._properties = {
            "adminAccess": admin_access if admin_access is not None else None,
            "allocationMode": allocation_mode if allocation_mode is not None else "",
            "count": count if count is not None else None,
            "deviceClassName": (
                device_class_name if device_class_name is not None else ""
            ),
            "name": name if name is not None else "",
            "selectors": selectors if selectors is not None else [],
        }
        self._types = {
            "adminAccess": (bool, None),
            "allocationMode": (str, None),
            "count": (int, None),
            "deviceClassName": (str, None),
            "name": (str, None),
            "selectors": (list, DeviceSelector),
        }

    @property
    def admin_access(self) -> bool:
        """
        AdminAccess indicates that this is a claim for
        administrative access to the device(s). Claims with
        AdminAccess are expected to be used for monitoring or other
        management services for a device.  They ignore all ordinary
        claims to the device with respect to access modes and any
        resource allocations.
        """
        return typing.cast(
            bool,
            self._properties.get("adminAccess"),
        )

    @admin_access.setter
    def admin_access(self, value: bool):
        """
        AdminAccess indicates that this is a claim for
        administrative access to the device(s). Claims with
        AdminAccess are expected to be used for monitoring or other
        management services for a device.  They ignore all ordinary
        claims to the device with respect to access modes and any
        resource allocations.
        """
        self._properties["adminAccess"] = value

    @property
    def allocation_mode(self) -> str:
        """
        AllocationMode and its related fields define how devices are
        allocated to satisfy this request. Supported values are:

        - ExactCount: This request is for a specific number of
        devices.
          This is the default. The exact number is provided in the
          count field.

        - All: This request is for all of the matching devices in a
        pool.
          Allocation will fail if some devices are already
        allocated,
          unless adminAccess is requested.

        If AlloctionMode is not specified, the default mode is
        ExactCount. If the mode is ExactCount and count is not
        specified, the default count is one. Any other requests must
        specify this field.

        More modes may get added in the future. Clients must refuse
        to handle requests with unknown modes.
        """
        return typing.cast(
            str,
            self._properties.get("allocationMode"),
        )

    @allocation_mode.setter
    def allocation_mode(self, value: str):
        """
        AllocationMode and its related fields define how devices are
        allocated to satisfy this request. Supported values are:

        - ExactCount: This request is for a specific number of
        devices.
          This is the default. The exact number is provided in the
          count field.

        - All: This request is for all of the matching devices in a
        pool.
          Allocation will fail if some devices are already
        allocated,
          unless adminAccess is requested.

        If AlloctionMode is not specified, the default mode is
        ExactCount. If the mode is ExactCount and count is not
        specified, the default count is one. Any other requests must
        specify this field.

        More modes may get added in the future. Clients must refuse
        to handle requests with unknown modes.
        """
        self._properties["allocationMode"] = value

    @property
    def count(self) -> int:
        """
        Count is used only when the count mode is "ExactCount". Must
        be greater than zero. If AllocationMode is ExactCount and
        this field is not specified, the default is one.
        """
        return typing.cast(
            int,
            self._properties.get("count"),
        )

    @count.setter
    def count(self, value: int):
        """
        Count is used only when the count mode is "ExactCount". Must
        be greater than zero. If AllocationMode is ExactCount and
        this field is not specified, the default is one.
        """
        self._properties["count"] = value

    @property
    def device_class_name(self) -> str:
        """
        DeviceClassName references a specific DeviceClass, which can
        define additional configuration and selectors to be
        inherited by this request.

        A class is required. Which classes are available depends on
        the cluster.

        Administrators may use this to restrict which devices may
        get requested by only installing classes with selectors for
        permitted devices. If users are free to request anything
        without restrictions, then administrators can create an
        empty DeviceClass for users to reference.
        """
        return typing.cast(
            str,
            self._properties.get("deviceClassName"),
        )

    @device_class_name.setter
    def device_class_name(self, value: str):
        """
        DeviceClassName references a specific DeviceClass, which can
        define additional configuration and selectors to be
        inherited by this request.

        A class is required. Which classes are available depends on
        the cluster.

        Administrators may use this to restrict which devices may
        get requested by only installing classes with selectors for
        permitted devices. If users are free to request anything
        without restrictions, then administrators can create an
        empty DeviceClass for users to reference.
        """
        self._properties["deviceClassName"] = value

    @property
    def name(self) -> str:
        """
        Name can be used to reference this request in a
        pod.spec.containers[].resources.claims entry and in a
        constraint of the claim.

        Must be a DNS label.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name can be used to reference this request in a
        pod.spec.containers[].resources.claims entry and in a
        constraint of the claim.

        Must be a DNS label.
        """
        self._properties["name"] = value

    @property
    def selectors(self) -> typing.List["DeviceSelector"]:
        """
        Selectors define criteria which must be satisfied by a
        specific device in order for that device to be considered
        for this request. All selectors must be satisfied for a
        device to be considered.
        """
        return typing.cast(
            typing.List["DeviceSelector"],
            self._properties.get("selectors"),
        )

    @selectors.setter
    def selectors(
        self, value: typing.Union[typing.List["DeviceSelector"], typing.List[dict]]
    ):
        """
        Selectors define criteria which must be satisfied by a
        specific device in order for that device to be considered
        for this request. All selectors must be satisfied for a
        device to be considered.
        """
        cleaned: typing.List[DeviceSelector] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceSelector,
                    DeviceSelector().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceSelector, item))
        self._properties["selectors"] = cleaned

    def __enter__(self) -> "DeviceRequest":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceRequestAllocationResult(_kuber_definitions.Definition):
    """
    DeviceRequestAllocationResult contains the allocation result
    for one request.
    """

    def __init__(
        self,
        device: typing.Optional[str] = None,
        driver: typing.Optional[str] = None,
        pool: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
    ):
        """Create DeviceRequestAllocationResult instance."""
        super(DeviceRequestAllocationResult, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceRequestAllocationResult"
        )
        self._properties = {
            "device": device if device is not None else "",
            "driver": driver if driver is not None else "",
            "pool": pool if pool is not None else "",
            "request": request if request is not None else "",
        }
        self._types = {
            "device": (str, None),
            "driver": (str, None),
            "pool": (str, None),
            "request": (str, None),
        }

    @property
    def device(self) -> str:
        """
        Device references one device instance via its name in the
        driver's resource pool. It must be a DNS label.
        """
        return typing.cast(
            str,
            self._properties.get("device"),
        )

    @device.setter
    def device(self, value: str):
        """
        Device references one device instance via its name in the
        driver's resource pool. It must be a DNS label.
        """
        self._properties["device"] = value

    @property
    def driver(self) -> str:
        """
        Driver specifies the name of the DRA driver whose kubelet
        plugin should be invoked to process the allocation once the
        claim is needed on a node.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver.
        """
        return typing.cast(
            str,
            self._properties.get("driver"),
        )

    @driver.setter
    def driver(self, value: str):
        """
        Driver specifies the name of the DRA driver whose kubelet
        plugin should be invoked to process the allocation once the
        claim is needed on a node.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver.
        """
        self._properties["driver"] = value

    @property
    def pool(self) -> str:
        """
        This name together with the driver name and the device name
        field identify which device was allocated (`<driver
        name>/<pool name>/<device name>`).

        Must not be longer than 253 characters and may contain one
        or more DNS sub-domains separated by slashes.
        """
        return typing.cast(
            str,
            self._properties.get("pool"),
        )

    @pool.setter
    def pool(self, value: str):
        """
        This name together with the driver name and the device name
        field identify which device was allocated (`<driver
        name>/<pool name>/<device name>`).

        Must not be longer than 253 characters and may contain one
        or more DNS sub-domains separated by slashes.
        """
        self._properties["pool"] = value

    @property
    def request(self) -> str:
        """
        Request is the name of the request in the claim which caused
        this device to be allocated. Multiple devices may have been
        allocated per request.
        """
        return typing.cast(
            str,
            self._properties.get("request"),
        )

    @request.setter
    def request(self, value: str):
        """
        Request is the name of the request in the claim which caused
        this device to be allocated. Multiple devices may have been
        allocated per request.
        """
        self._properties["request"] = value

    def __enter__(self) -> "DeviceRequestAllocationResult":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceSelector(_kuber_definitions.Definition):
    """
    DeviceSelector must have exactly one field set.
    """

    def __init__(
        self,
        cel: typing.Optional["CELDeviceSelector"] = None,
    ):
        """Create DeviceSelector instance."""
        super(DeviceSelector, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceSelector"
        )
        self._properties = {
            "cel": cel if cel is not None else CELDeviceSelector(),
        }
        self._types = {
            "cel": (CELDeviceSelector, None),
        }

    @property
    def cel(self) -> "CELDeviceSelector":
        """
        CEL contains a CEL expression for selecting a device.
        """
        return typing.cast(
            "CELDeviceSelector",
            self._properties.get("cel"),
        )

    @cel.setter
    def cel(self, value: typing.Union["CELDeviceSelector", dict]):
        """
        CEL contains a CEL expression for selecting a device.
        """
        if isinstance(value, dict):
            value = typing.cast(
                CELDeviceSelector,
                CELDeviceSelector().from_dict(value),
            )
        self._properties["cel"] = value

    def __enter__(self) -> "DeviceSelector":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class OpaqueDeviceConfiguration(_kuber_definitions.Definition):
    """
    OpaqueDeviceConfiguration contains configuration parameters
    for a driver in a format defined by the driver vendor.
    """

    def __init__(
        self,
        driver: typing.Optional[str] = None,
        parameters: typing.Optional["RawExtension"] = None,
    ):
        """Create OpaqueDeviceConfiguration instance."""
        super(OpaqueDeviceConfiguration, self).__init__(
            api_version="resource/v1alpha3", kind="OpaqueDeviceConfiguration"
        )
        self._properties = {
            "driver": driver if driver is not None else "",
            "parameters": parameters if parameters is not None else RawExtension(),
        }
        self._types = {
            "driver": (str, None),
            "parameters": (RawExtension, None),
        }

    @property
    def driver(self) -> str:
        """
        Driver is used to determine which kubelet plugin needs to be
        passed these configuration parameters.

        An admission policy provided by the driver developer could
        use this to decide whether it needs to validate them.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver.
        """
        return typing.cast(
            str,
            self._properties.get("driver"),
        )

    @driver.setter
    def driver(self, value: str):
        """
        Driver is used to determine which kubelet plugin needs to be
        passed these configuration parameters.

        An admission policy provided by the driver developer could
        use this to decide whether it needs to validate them.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver.
        """
        self._properties["driver"] = value

    @property
    def parameters(self) -> "RawExtension":
        """
        Parameters can contain arbitrary data. It is the
        responsibility of the driver developer to handle validation
        and versioning. Typically this includes self-identification
        and a version ("kind" + "apiVersion" for Kubernetes types),
        with conversion between different versions.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("parameters"),
        )

    @parameters.setter
    def parameters(self, value: typing.Union["RawExtension", dict]):
        """
        Parameters can contain arbitrary data. It is the
        responsibility of the driver developer to handle validation
        and versioning. Typically this includes self-identification
        and a version ("kind" + "apiVersion" for Kubernetes types),
        with conversion between different versions.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["parameters"] = value

    def __enter__(self) -> "OpaqueDeviceConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodSchedulingContext(_kuber_definitions.Resource):
    """
    PodSchedulingContext objects hold information that is needed
    to schedule a Pod with ResourceClaims that use
    "WaitForFirstConsumer" allocation mode.

    This is an alpha type and requires enabling the
    DRAControlPlaneController feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["PodSchedulingContextSpec"] = None,
        status: typing.Optional["PodSchedulingContextStatus"] = None,
    ):
        """Create PodSchedulingContext instance."""
        super(PodSchedulingContext, self).__init__(
            api_version="resource/v1alpha3", kind="PodSchedulingContext"
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

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
            api_version="resource/v1alpha3", kind="PodSchedulingContextList"
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

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
            api_version="resource/v1alpha3", kind="PodSchedulingContextSpec"
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
            api_version="resource/v1alpha3", kind="PodSchedulingContextStatus"
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
    ResourceClaim describes a request for access to resources in
    the cluster, for use by workloads. For example, if a
    workload needs an accelerator device with specific
    properties, this is how that request is expressed. The
    status stanza tracks whether this claim has been satisfied
    and what specific resources have been allocated.

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
            api_version="resource/v1alpha3", kind="ResourceClaim"
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
        Spec describes what is being requested and how to configure
        it. The spec is immutable.
        """
        return typing.cast(
            "ResourceClaimSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceClaimSpec", dict]):
        """
        Spec describes what is being requested and how to configure
        it. The spec is immutable.
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
        Status describes whether the claim is ready to use and what
        has been allocated.
        """
        return typing.cast(
            "ResourceClaimStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["ResourceClaimStatus", dict]):
        """
        Status describes whether the claim is ready to use and what
        has been allocated.
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

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
            api_version="resource/v1alpha3", kind="ResourceClaimConsumerReference"
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
            api_version="resource/v1alpha3", kind="ResourceClaimList"
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

    def __enter__(self) -> "ResourceClaimList":
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
            api_version="resource/v1alpha3", kind="ResourceClaimSchedulingStatus"
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
    ResourceClaimSpec defines what is being requested in a
    ResourceClaim and how to configure it.
    """

    def __init__(
        self,
        controller: typing.Optional[str] = None,
        devices: typing.Optional["DeviceClaim"] = None,
    ):
        """Create ResourceClaimSpec instance."""
        super(ResourceClaimSpec, self).__init__(
            api_version="resource/v1alpha3", kind="ResourceClaimSpec"
        )
        self._properties = {
            "controller": controller if controller is not None else "",
            "devices": devices if devices is not None else DeviceClaim(),
        }
        self._types = {
            "controller": (str, None),
            "devices": (DeviceClaim, None),
        }

    @property
    def controller(self) -> str:
        """
        Controller is the name of the DRA driver that is meant to
        handle allocation of this claim. If empty, allocation is
        handled by the scheduler while scheduling a pod.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
        """
        return typing.cast(
            str,
            self._properties.get("controller"),
        )

    @controller.setter
    def controller(self, value: str):
        """
        Controller is the name of the DRA driver that is meant to
        handle allocation of this claim. If empty, allocation is
        handled by the scheduler while scheduling a pod.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
        """
        self._properties["controller"] = value

    @property
    def devices(self) -> "DeviceClaim":
        """
        Devices defines how to request devices.
        """
        return typing.cast(
            "DeviceClaim",
            self._properties.get("devices"),
        )

    @devices.setter
    def devices(self, value: typing.Union["DeviceClaim", dict]):
        """
        Devices defines how to request devices.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeviceClaim,
                DeviceClaim().from_dict(value),
            )
        self._properties["devices"] = value

    def __enter__(self) -> "ResourceClaimSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceClaimStatus(_kuber_definitions.Definition):
    """
    ResourceClaimStatus tracks whether the resource has been
    allocated and what the result of that was.
    """

    def __init__(
        self,
        allocation: typing.Optional["AllocationResult"] = None,
        deallocation_requested: typing.Optional[bool] = None,
        reserved_for: typing.Optional[
            typing.List["ResourceClaimConsumerReference"]
        ] = None,
    ):
        """Create ResourceClaimStatus instance."""
        super(ResourceClaimStatus, self).__init__(
            api_version="resource/v1alpha3", kind="ResourceClaimStatus"
        )
        self._properties = {
            "allocation": allocation if allocation is not None else AllocationResult(),
            "deallocationRequested": (
                deallocation_requested if deallocation_requested is not None else None
            ),
            "reservedFor": reserved_for if reserved_for is not None else [],
        }
        self._types = {
            "allocation": (AllocationResult, None),
            "deallocationRequested": (bool, None),
            "reservedFor": (list, ResourceClaimConsumerReference),
        }

    @property
    def allocation(self) -> "AllocationResult":
        """
        Allocation is set once the claim has been allocated
        successfully.
        """
        return typing.cast(
            "AllocationResult",
            self._properties.get("allocation"),
        )

    @allocation.setter
    def allocation(self, value: typing.Union["AllocationResult", dict]):
        """
        Allocation is set once the claim has been allocated
        successfully.
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
        Indicates that a claim is to be deallocated. While this is
        set, no new consumers may be added to ReservedFor.

        This is only used if the claim needs to be deallocated by a
        DRA driver. That driver then must deallocate this claim and
        reset the field together with clearing the Allocation field.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
        """
        return typing.cast(
            bool,
            self._properties.get("deallocationRequested"),
        )

    @deallocation_requested.setter
    def deallocation_requested(self, value: bool):
        """
        Indicates that a claim is to be deallocated. While this is
        set, no new consumers may be added to ReservedFor.

        This is only used if the claim needs to be deallocated by a
        DRA driver. That driver then must deallocate this claim and
        reset the field together with clearing the Allocation field.

        This is an alpha field and requires enabling the
        DRAControlPlaneController feature gate.
        """
        self._properties["deallocationRequested"] = value

    @property
    def reserved_for(self) -> typing.List["ResourceClaimConsumerReference"]:
        """
        ReservedFor indicates which entities are currently allowed
        to use the claim. A Pod which references a ResourceClaim
        which is not reserved for that Pod will not be started. A
        claim that is in use or might be in use because it has been
        reserved must not get deallocated.

        In a cluster with multiple scheduler instances, two pods
        might get scheduled concurrently by different schedulers.
        When they reference the same ResourceClaim which already has
        reached its maximum number of consumers, only one pod can be
        scheduled.

        Both schedulers try to add their pod to the
        claim.status.reservedFor field, but only the update that
        reaches the API server first gets stored. The other one
        fails with an error and the scheduler which issued it knows
        that it must put the pod back into the queue, waiting for
        the ResourceClaim to become usable again.

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
        which is not reserved for that Pod will not be started. A
        claim that is in use or might be in use because it has been
        reserved must not get deallocated.

        In a cluster with multiple scheduler instances, two pods
        might get scheduled concurrently by different schedulers.
        When they reference the same ResourceClaim which already has
        reached its maximum number of consumers, only one pod can be
        scheduled.

        Both schedulers try to add their pod to the
        claim.status.reservedFor field, but only the update that
        reaches the API server first gets stored. The other one
        fails with an error and the scheduler which issued it knows
        that it must put the pod back into the queue, waiting for
        the ResourceClaim to become usable again.

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

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceClaimTemplateSpec"] = None,
    ):
        """Create ResourceClaimTemplate instance."""
        super(ResourceClaimTemplate, self).__init__(
            api_version="resource/v1alpha3", kind="ResourceClaimTemplate"
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

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
            api_version="resource/v1alpha3", kind="ResourceClaimTemplateList"
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

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
            api_version="resource/v1alpha3", kind="ResourceClaimTemplateSpec"
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


class ResourcePool(_kuber_definitions.Definition):
    """
    ResourcePool describes the pool that ResourceSlices belong
    to.
    """

    def __init__(
        self,
        generation: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        resource_slice_count: typing.Optional[int] = None,
    ):
        """Create ResourcePool instance."""
        super(ResourcePool, self).__init__(
            api_version="resource/v1alpha3", kind="ResourcePool"
        )
        self._properties = {
            "generation": generation if generation is not None else None,
            "name": name if name is not None else "",
            "resourceSliceCount": (
                resource_slice_count if resource_slice_count is not None else None
            ),
        }
        self._types = {
            "generation": (int, None),
            "name": (str, None),
            "resourceSliceCount": (int, None),
        }

    @property
    def generation(self) -> int:
        """
        Generation tracks the change in a pool over time. Whenever a
        driver changes something about one or more of the resources
        in a pool, it must change the generation in all
        ResourceSlices which are part of that pool. Consumers of
        ResourceSlices should only consider resources from the pool
        with the highest generation number. The generation may be
        reset by drivers, which should be fine for consumers,
        assuming that all ResourceSlices in a pool are updated to
        match or deleted.

        Combined with ResourceSliceCount, this mechanism enables
        consumers to detect pools which are comprised of multiple
        ResourceSlices and are in an incomplete state.
        """
        return typing.cast(
            int,
            self._properties.get("generation"),
        )

    @generation.setter
    def generation(self, value: int):
        """
        Generation tracks the change in a pool over time. Whenever a
        driver changes something about one or more of the resources
        in a pool, it must change the generation in all
        ResourceSlices which are part of that pool. Consumers of
        ResourceSlices should only consider resources from the pool
        with the highest generation number. The generation may be
        reset by drivers, which should be fine for consumers,
        assuming that all ResourceSlices in a pool are updated to
        match or deleted.

        Combined with ResourceSliceCount, this mechanism enables
        consumers to detect pools which are comprised of multiple
        ResourceSlices and are in an incomplete state.
        """
        self._properties["generation"] = value

    @property
    def name(self) -> str:
        """
        Name is used to identify the pool. For node-local devices,
        this is often the node name, but this is not required.

        It must not be longer than 253 characters and must consist
        of one or more DNS sub-domains separated by slashes. This
        field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is used to identify the pool. For node-local devices,
        this is often the node name, but this is not required.

        It must not be longer than 253 characters and must consist
        of one or more DNS sub-domains separated by slashes. This
        field is immutable.
        """
        self._properties["name"] = value

    @property
    def resource_slice_count(self) -> int:
        """
        ResourceSliceCount is the total number of ResourceSlices in
        the pool at this generation number. Must be greater than
        zero.

        Consumers can use this to check whether they have seen all
        ResourceSlices belonging to the same pool.
        """
        return typing.cast(
            int,
            self._properties.get("resourceSliceCount"),
        )

    @resource_slice_count.setter
    def resource_slice_count(self, value: int):
        """
        ResourceSliceCount is the total number of ResourceSlices in
        the pool at this generation number. Must be greater than
        zero.

        Consumers can use this to check whether they have seen all
        ResourceSlices belonging to the same pool.
        """
        self._properties["resourceSliceCount"] = value

    def __enter__(self) -> "ResourcePool":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceSlice(_kuber_definitions.Resource):
    """
    ResourceSlice represents one or more resources in a pool of
    similar resources, managed by a common driver. A pool may
    span more than one ResourceSlice, and exactly how many
    ResourceSlices comprise a pool is determined by the driver.

    At the moment, the only supported resources are devices with
    attributes and capacities. Each device in a given pool,
    regardless of how many ResourceSlices, must have a unique
    name. The ResourceSlice in which a device gets published may
    change over time. The unique identifier for a device is the
    tuple <driver name>, <pool name>, <device name>.

    Whenever a driver needs to update a pool, it increments the
    pool.Spec.Pool.Generation number and updates all
    ResourceSlices with that new number and new resource
    definitions. A consumer must only use ResourceSlices with
    the highest generation number and ignore all others.

    When allocating all resources in a pool matching certain
    criteria or when looking for the best solution among several
    different alternatives, a consumer should check the number
    of ResourceSlices in a pool (included in each ResourceSlice)
    to determine whether its view of a pool is complete and if
    not, should wait until the driver has completed updating the
    pool.

    For resources that are not local to a node, the node name is
    not set. Instead, the driver may use a node selector to
    specify where the devices are available.

    This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ResourceSliceSpec"] = None,
    ):
        """Create ResourceSlice instance."""
        super(ResourceSlice, self).__init__(
            api_version="resource/v1alpha3", kind="ResourceSlice"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ResourceSliceSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ResourceSliceSpec, None),
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
    def spec(self) -> "ResourceSliceSpec":
        """
        Contains the information published by the driver.

        Changing the spec automatically increments the
        metadata.generation number.
        """
        return typing.cast(
            "ResourceSliceSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ResourceSliceSpec", dict]):
        """
        Contains the information published by the driver.

        Changing the spec automatically increments the
        metadata.generation number.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourceSliceSpec,
                ResourceSliceSpec().from_dict(value),
            )
        self._properties["spec"] = value

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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

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
            api_version="resource/v1alpha3", kind="ResourceSliceList"
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
        Items is the list of resource ResourceSlices.
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
        Items is the list of resource ResourceSlices.
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
    ) -> "client.ResourceV1alpha3Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.ResourceV1alpha3Api(**kwargs)

    def __enter__(self) -> "ResourceSliceList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceSliceSpec(_kuber_definitions.Definition):
    """
    ResourceSliceSpec contains the information published by the
    driver in one ResourceSlice.
    """

    def __init__(
        self,
        all_nodes: typing.Optional[bool] = None,
        devices: typing.Optional[typing.List["Device"]] = None,
        driver: typing.Optional[str] = None,
        node_name: typing.Optional[str] = None,
        node_selector: typing.Optional["NodeSelector"] = None,
        pool: typing.Optional["ResourcePool"] = None,
    ):
        """Create ResourceSliceSpec instance."""
        super(ResourceSliceSpec, self).__init__(
            api_version="resource/v1alpha3", kind="ResourceSliceSpec"
        )
        self._properties = {
            "allNodes": all_nodes if all_nodes is not None else None,
            "devices": devices if devices is not None else [],
            "driver": driver if driver is not None else "",
            "nodeName": node_name if node_name is not None else "",
            "nodeSelector": (
                node_selector if node_selector is not None else NodeSelector()
            ),
            "pool": pool if pool is not None else ResourcePool(),
        }
        self._types = {
            "allNodes": (bool, None),
            "devices": (list, Device),
            "driver": (str, None),
            "nodeName": (str, None),
            "nodeSelector": (NodeSelector, None),
            "pool": (ResourcePool, None),
        }

    @property
    def all_nodes(self) -> bool:
        """
        AllNodes indicates that all nodes have access to the
        resources in the pool.

        Exactly one of NodeName, NodeSelector and AllNodes must be
        set.
        """
        return typing.cast(
            bool,
            self._properties.get("allNodes"),
        )

    @all_nodes.setter
    def all_nodes(self, value: bool):
        """
        AllNodes indicates that all nodes have access to the
        resources in the pool.

        Exactly one of NodeName, NodeSelector and AllNodes must be
        set.
        """
        self._properties["allNodes"] = value

    @property
    def devices(self) -> typing.List["Device"]:
        """
        Devices lists some or all of the devices in this pool.

        Must not have more than 128 entries.
        """
        return typing.cast(
            typing.List["Device"],
            self._properties.get("devices"),
        )

    @devices.setter
    def devices(self, value: typing.Union[typing.List["Device"], typing.List[dict]]):
        """
        Devices lists some or all of the devices in this pool.

        Must not have more than 128 entries.
        """
        cleaned: typing.List[Device] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Device,
                    Device().from_dict(item),
                )
            cleaned.append(typing.cast(Device, item))
        self._properties["devices"] = cleaned

    @property
    def driver(self) -> str:
        """
        Driver identifies the DRA driver providing the capacity
        information. A field selector can be used to list only
        ResourceSlice objects with a certain driver name.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver. This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("driver"),
        )

    @driver.setter
    def driver(self, value: str):
        """
        Driver identifies the DRA driver providing the capacity
        information. A field selector can be used to list only
        ResourceSlice objects with a certain driver name.

        Must be a DNS subdomain and should end with a DNS domain
        owned by the vendor of the driver. This field is immutable.
        """
        self._properties["driver"] = value

    @property
    def node_name(self) -> str:
        """
        NodeName identifies the node which provides the resources in
        this pool. A field selector can be used to list only
        ResourceSlice objects belonging to a certain node.

        This field can be used to limit access from nodes to
        ResourceSlices with the same node name. It also indicates to
        autoscalers that adding new nodes of the same type as some
        old node might also make new resources available.

        Exactly one of NodeName, NodeSelector and AllNodes must be
        set. This field is immutable.
        """
        return typing.cast(
            str,
            self._properties.get("nodeName"),
        )

    @node_name.setter
    def node_name(self, value: str):
        """
        NodeName identifies the node which provides the resources in
        this pool. A field selector can be used to list only
        ResourceSlice objects belonging to a certain node.

        This field can be used to limit access from nodes to
        ResourceSlices with the same node name. It also indicates to
        autoscalers that adding new nodes of the same type as some
        old node might also make new resources available.

        Exactly one of NodeName, NodeSelector and AllNodes must be
        set. This field is immutable.
        """
        self._properties["nodeName"] = value

    @property
    def node_selector(self) -> "NodeSelector":
        """
        NodeSelector defines which nodes have access to the
        resources in the pool, when that pool is not limited to a
        single node.

        Must use exactly one term.

        Exactly one of NodeName, NodeSelector and AllNodes must be
        set.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("nodeSelector"),
        )

    @node_selector.setter
    def node_selector(self, value: typing.Union["NodeSelector", dict]):
        """
        NodeSelector defines which nodes have access to the
        resources in the pool, when that pool is not limited to a
        single node.

        Must use exactly one term.

        Exactly one of NodeName, NodeSelector and AllNodes must be
        set.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["nodeSelector"] = value

    @property
    def pool(self) -> "ResourcePool":
        """
        Pool describes the pool that this ResourceSlice belongs to.
        """
        return typing.cast(
            "ResourcePool",
            self._properties.get("pool"),
        )

    @pool.setter
    def pool(self, value: typing.Union["ResourcePool", dict]):
        """
        Pool describes the pool that this ResourceSlice belongs to.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ResourcePool,
                ResourcePool().from_dict(value),
            )
        self._properties["pool"] = value

    def __enter__(self) -> "ResourceSliceSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
