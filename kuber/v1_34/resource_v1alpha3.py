import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_34.meta_v1 import Condition  # noqa: F401
from kuber.v1_34.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_34.core_v1 import NodeSelector  # noqa: F401
from kuber.v1_34.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_34.apimachinery_runtime import RawExtension  # noqa: F401
from kuber.v1_34.meta_v1 import Status  # noqa: F401
from kuber.v1_34.meta_v1 import StatusDetails  # noqa: F401


class AllocatedDeviceStatus(_kuber_definitions.Definition):
    """
    AllocatedDeviceStatus contains the status of an allocated
    device, if the driver chooses to report it. This may include
    driver-specific information.
    """

    def __init__(
        self,
        conditions: typing.Optional[typing.List["Condition"]] = None,
        data: typing.Optional["RawExtension"] = None,
        device: typing.Optional[str] = None,
        driver: typing.Optional[str] = None,
        network_data: typing.Optional["NetworkDeviceData"] = None,
        pool: typing.Optional[str] = None,
    ):
        """Create AllocatedDeviceStatus instance."""
        super(AllocatedDeviceStatus, self).__init__(
            api_version="resource/v1alpha3", kind="AllocatedDeviceStatus"
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
            "data": data if data is not None else RawExtension(),
            "device": device if device is not None else "",
            "driver": driver if driver is not None else "",
            "networkData": (
                network_data if network_data is not None else NetworkDeviceData()
            ),
            "pool": pool if pool is not None else "",
        }
        self._types = {
            "conditions": (list, Condition),
            "data": (RawExtension, None),
            "device": (str, None),
            "driver": (str, None),
            "networkData": (NetworkDeviceData, None),
            "pool": (str, None),
        }

    @property
    def conditions(self) -> typing.List["Condition"]:
        """
        Conditions contains the latest observation of the device's
        state. If the device has been configured according to the
        class and claim config references, the `Ready` condition
        should be True.

        Must not contain more than 8 entries.
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
        Conditions contains the latest observation of the device's
        state. If the device has been configured according to the
        class and claim config references, the `Ready` condition
        should be True.

        Must not contain more than 8 entries.
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

    @property
    def data(self) -> "RawExtension":
        """
        Data contains arbitrary driver-specific data.

        The length of the raw data must be smaller or equal to 10
        Ki.
        """
        return typing.cast(
            "RawExtension",
            self._properties.get("data"),
        )

    @data.setter
    def data(self, value: typing.Union["RawExtension", dict]):
        """
        Data contains arbitrary driver-specific data.

        The length of the raw data must be smaller or equal to 10
        Ki.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RawExtension,
                RawExtension().from_dict(value),
            )
        self._properties["data"] = value

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
    def network_data(self) -> "NetworkDeviceData":
        """
        NetworkData contains network-related information specific to
        the device.
        """
        return typing.cast(
            "NetworkDeviceData",
            self._properties.get("networkData"),
        )

    @network_data.setter
    def network_data(self, value: typing.Union["NetworkDeviceData", dict]):
        """
        NetworkData contains network-related information specific to
        the device.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NetworkDeviceData,
                NetworkDeviceData().from_dict(value),
            )
        self._properties["networkData"] = value

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

    def __enter__(self) -> "AllocatedDeviceStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class AllocationResult(_kuber_definitions.Definition):
    """
    AllocationResult contains attributes of an allocated
    resource.
    """

    def __init__(
        self,
        devices: typing.Optional["DeviceAllocationResult"] = None,
        node_selector: typing.Optional["NodeSelector"] = None,
    ):
        """Create AllocationResult instance."""
        super(AllocationResult, self).__init__(
            api_version="resource/v1alpha3", kind="AllocationResult"
        )
        self._properties = {
            "devices": devices if devices is not None else DeviceAllocationResult(),
            "nodeSelector": (
                node_selector if node_selector is not None else NodeSelector()
            ),
        }
        self._types = {
            "devices": (DeviceAllocationResult, None),
            "nodeSelector": (NodeSelector, None),
        }

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
        all_nodes: typing.Optional[bool] = None,
        attributes: typing.Optional[dict] = None,
        capacity: typing.Optional[dict] = None,
        consumes_counters: typing.Optional[
            typing.List["DeviceCounterConsumption"]
        ] = None,
        node_name: typing.Optional[str] = None,
        node_selector: typing.Optional["NodeSelector"] = None,
        taints: typing.Optional[typing.List["DeviceTaint"]] = None,
    ):
        """Create BasicDevice instance."""
        super(BasicDevice, self).__init__(
            api_version="resource/v1alpha3", kind="BasicDevice"
        )
        self._properties = {
            "allNodes": all_nodes if all_nodes is not None else None,
            "attributes": attributes if attributes is not None else {},
            "capacity": capacity if capacity is not None else {},
            "consumesCounters": (
                consumes_counters if consumes_counters is not None else []
            ),
            "nodeName": node_name if node_name is not None else "",
            "nodeSelector": (
                node_selector if node_selector is not None else NodeSelector()
            ),
            "taints": taints if taints is not None else [],
        }
        self._types = {
            "allNodes": (bool, None),
            "attributes": (dict, None),
            "capacity": (dict, None),
            "consumesCounters": (list, DeviceCounterConsumption),
            "nodeName": (str, None),
            "nodeSelector": (NodeSelector, None),
            "taints": (list, DeviceTaint),
        }

    @property
    def all_nodes(self) -> bool:
        """
        AllNodes indicates that all nodes have access to the device.

        Must only be set if Spec.PerDeviceNodeSelection is set to
        true. At most one of NodeName, NodeSelector and AllNodes can
        be set.
        """
        return typing.cast(
            bool,
            self._properties.get("allNodes"),
        )

    @all_nodes.setter
    def all_nodes(self, value: bool):
        """
        AllNodes indicates that all nodes have access to the device.

        Must only be set if Spec.PerDeviceNodeSelection is set to
        true. At most one of NodeName, NodeSelector and AllNodes can
        be set.
        """
        self._properties["allNodes"] = value

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

    @property
    def consumes_counters(self) -> typing.List["DeviceCounterConsumption"]:
        """
        ConsumesCounters defines a list of references to
        sharedCounters and the set of counters that the device will
        consume from those counter sets.

        There can only be a single entry per counterSet.

        The total number of device counter consumption entries must
        be <= 32. In addition, the total number in the entire
        ResourceSlice must be <= 1024 (for example, 64 devices with
        16 counters each).
        """
        return typing.cast(
            typing.List["DeviceCounterConsumption"],
            self._properties.get("consumesCounters"),
        )

    @consumes_counters.setter
    def consumes_counters(
        self,
        value: typing.Union[typing.List["DeviceCounterConsumption"], typing.List[dict]],
    ):
        """
        ConsumesCounters defines a list of references to
        sharedCounters and the set of counters that the device will
        consume from those counter sets.

        There can only be a single entry per counterSet.

        The total number of device counter consumption entries must
        be <= 32. In addition, the total number in the entire
        ResourceSlice must be <= 1024 (for example, 64 devices with
        16 counters each).
        """
        cleaned: typing.List[DeviceCounterConsumption] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceCounterConsumption,
                    DeviceCounterConsumption().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceCounterConsumption, item))
        self._properties["consumesCounters"] = cleaned

    @property
    def node_name(self) -> str:
        """
        NodeName identifies the node where the device is available.

        Must only be set if Spec.PerDeviceNodeSelection is set to
        true. At most one of NodeName, NodeSelector and AllNodes can
        be set.
        """
        return typing.cast(
            str,
            self._properties.get("nodeName"),
        )

    @node_name.setter
    def node_name(self, value: str):
        """
        NodeName identifies the node where the device is available.

        Must only be set if Spec.PerDeviceNodeSelection is set to
        true. At most one of NodeName, NodeSelector and AllNodes can
        be set.
        """
        self._properties["nodeName"] = value

    @property
    def node_selector(self) -> "NodeSelector":
        """
        NodeSelector defines the nodes where the device is
        available.

        Must only be set if Spec.PerDeviceNodeSelection is set to
        true. At most one of NodeName, NodeSelector and AllNodes can
        be set.
        """
        return typing.cast(
            "NodeSelector",
            self._properties.get("nodeSelector"),
        )

    @node_selector.setter
    def node_selector(self, value: typing.Union["NodeSelector", dict]):
        """
        NodeSelector defines the nodes where the device is
        available.

        Must only be set if Spec.PerDeviceNodeSelection is set to
        true. At most one of NodeName, NodeSelector and AllNodes can
        be set.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["nodeSelector"] = value

    @property
    def taints(self) -> typing.List["DeviceTaint"]:
        """
        If specified, these are the driver-defined taints.

        The maximum number of taints is 4.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        return typing.cast(
            typing.List["DeviceTaint"],
            self._properties.get("taints"),
        )

    @taints.setter
    def taints(
        self, value: typing.Union[typing.List["DeviceTaint"], typing.List[dict]]
    ):
        """
        If specified, these are the driver-defined taints.

        The maximum number of taints is 4.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        cleaned: typing.List[DeviceTaint] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceTaint,
                    DeviceTaint().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceTaint, item))
        self._properties["taints"] = cleaned

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

        The length of the expression must be smaller or equal to 10
        Ki. The cost of evaluating it is also limited based on the
        estimated number of logical steps.
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

        The length of the expression must be smaller or equal to 10
        Ki. The cost of evaluating it is also limited based on the
        estimated number of logical steps.
        """
        self._properties["expression"] = value

    def __enter__(self) -> "CELDeviceSelector":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Counter(_kuber_definitions.Definition):
    """
    Counter describes a quantity associated with a device.
    """

    def __init__(
        self,
        value: typing.Optional[typing.Union[str, int, None]] = None,
    ):
        """Create Counter instance."""
        super(Counter, self).__init__(api_version="resource/v1alpha3", kind="Counter")
        self._properties = {
            "value": value if value is not None else None,
        }
        self._types = {
            "value": (_types.integer_or_string, None),
        }

    @property
    def value(self) -> typing.Optional[str]:
        """
        Value defines how much of a certain device counter is
        available.
        """
        value = self._properties.get("value")
        return f"{value}" if value is not None else None

    @value.setter
    def value(self, value: typing.Union[str, int, None]):
        """
        Value defines how much of a certain device counter is
        available.
        """
        self._properties["value"] = _types.integer_or_string(value)

    def __enter__(self) -> "Counter":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CounterSet(_kuber_definitions.Definition):
    """
    CounterSet defines a named set of counters that are
    available to be used by devices defined in the
    ResourceSlice.

    The counters are not allocatable by themselves, but can be
    referenced by devices. When a device is allocated, the
    portion of counters it uses will no longer be available for
    use by other devices.
    """

    def __init__(
        self,
        counters: typing.Optional[dict] = None,
        name: typing.Optional[str] = None,
    ):
        """Create CounterSet instance."""
        super(CounterSet, self).__init__(
            api_version="resource/v1alpha3", kind="CounterSet"
        )
        self._properties = {
            "counters": counters if counters is not None else {},
            "name": name if name is not None else "",
        }
        self._types = {
            "counters": (dict, None),
            "name": (str, None),
        }

    @property
    def counters(self) -> dict:
        """
        Counters defines the counters that will be consumed by the
        device. The name of each counter must be unique in that set
        and must be a DNS label.

        To ensure this uniqueness, capacities defined by the vendor
        must be listed without the driver name as domain prefix in
        their name. All others must be listed with their domain
        prefix.

        The maximum number of counters is 32.
        """
        return typing.cast(
            dict,
            self._properties.get("counters"),
        )

    @counters.setter
    def counters(self, value: dict):
        """
        Counters defines the counters that will be consumed by the
        device. The name of each counter must be unique in that set
        and must be a DNS label.

        To ensure this uniqueness, capacities defined by the vendor
        must be listed without the driver name as domain prefix in
        their name. All others must be listed with their domain
        prefix.

        The maximum number of counters is 32.
        """
        self._properties["counters"] = value

    @property
    def name(self) -> str:
        """
        CounterSet is the name of the set from which the counters
        defined will be consumed.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        CounterSet is the name of the set from which the counters
        defined will be consumed.
        """
        self._properties["name"] = value

    def __enter__(self) -> "CounterSet":
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

        References to subrequests must include the name of the main
        request and may include the subrequest using the format
        <main request>[/<subrequest>]. If just the main request is
        given, the configuration applies to all subrequests.
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

        References to subrequests must include the name of the main
        request and may include the subrequest using the format
        <main request>[/<subrequest>]. If just the main request is
        given, the configuration applies to all subrequests.
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

        References to subrequests must include the name of the main
        request and may include the subrequest using the format
        <main request>[/<subrequest>]. If just the main request is
        given, the configuration applies to all subrequests.
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

        References to subrequests must include the name of the main
        request and may include the subrequest using the format
        <main request>[/<subrequest>]. If just the main request is
        given, the configuration applies to all subrequests.
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
    ):
        """Create DeviceClassSpec instance."""
        super(DeviceClassSpec, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceClassSpec"
        )
        self._properties = {
            "config": config if config is not None else [],
            "selectors": selectors if selectors is not None else [],
        }
        self._types = {
            "config": (list, DeviceClassConfiguration),
            "selectors": (list, DeviceSelector),
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

        References to subrequests must include the name of the main
        request and may include the subrequest using the format
        <main request>[/<subrequest>]. If just the main request is
        given, the constraint applies to all subrequests.
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

        References to subrequests must include the name of the main
        request and may include the subrequest using the format
        <main request>[/<subrequest>]. If just the main request is
        given, the constraint applies to all subrequests.
        """
        self._properties["requests"] = value

    def __enter__(self) -> "DeviceConstraint":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceCounterConsumption(_kuber_definitions.Definition):
    """
    DeviceCounterConsumption defines a set of counters that a
    device will consume from a CounterSet.
    """

    def __init__(
        self,
        counter_set: typing.Optional[str] = None,
        counters: typing.Optional[dict] = None,
    ):
        """Create DeviceCounterConsumption instance."""
        super(DeviceCounterConsumption, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceCounterConsumption"
        )
        self._properties = {
            "counterSet": counter_set if counter_set is not None else "",
            "counters": counters if counters is not None else {},
        }
        self._types = {
            "counterSet": (str, None),
            "counters": (dict, None),
        }

    @property
    def counter_set(self) -> str:
        """
        CounterSet defines the set from which the counters defined
        will be consumed.
        """
        return typing.cast(
            str,
            self._properties.get("counterSet"),
        )

    @counter_set.setter
    def counter_set(self, value: str):
        """
        CounterSet defines the set from which the counters defined
        will be consumed.
        """
        self._properties["counterSet"] = value

    @property
    def counters(self) -> dict:
        """
        Counters defines the Counter that will be consumed by the
        device.

        The maximum number counters in a device is 32. In addition,
        the maximum number of all counters in all devices is 1024
        (for example, 64 devices with 16 counters each).
        """
        return typing.cast(
            dict,
            self._properties.get("counters"),
        )

    @counters.setter
    def counters(self, value: dict):
        """
        Counters defines the Counter that will be consumed by the
        device.

        The maximum number counters in a device is 32. In addition,
        the maximum number of all counters in all devices is 1024
        (for example, 64 devices with 16 counters each).
        """
        self._properties["counters"] = value

    def __enter__(self) -> "DeviceCounterConsumption":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceRequest(_kuber_definitions.Definition):
    """
    DeviceRequest is a request for devices required for a claim.
    This is typically a request for a single resource like a
    device, but can also ask for several identical devices.
    """

    def __init__(
        self,
        admin_access: typing.Optional[bool] = None,
        allocation_mode: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        device_class_name: typing.Optional[str] = None,
        first_available: typing.Optional[typing.List["DeviceSubRequest"]] = None,
        name: typing.Optional[str] = None,
        selectors: typing.Optional[typing.List["DeviceSelector"]] = None,
        tolerations: typing.Optional[typing.List["DeviceToleration"]] = None,
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
            "firstAvailable": first_available if first_available is not None else [],
            "name": name if name is not None else "",
            "selectors": selectors if selectors is not None else [],
            "tolerations": tolerations if tolerations is not None else [],
        }
        self._types = {
            "adminAccess": (bool, None),
            "allocationMode": (str, None),
            "count": (int, None),
            "deviceClassName": (str, None),
            "firstAvailable": (list, DeviceSubRequest),
            "name": (str, None),
            "selectors": (list, DeviceSelector),
            "tolerations": (list, DeviceToleration),
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

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.

        This is an alpha field and requires enabling the
        DRAAdminAccess feature gate. Admin access is disabled if
        this field is unset or set to false, otherwise it is
        enabled.
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

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.

        This is an alpha field and requires enabling the
        DRAAdminAccess feature gate. Admin access is disabled if
        this field is unset or set to false, otherwise it is
        enabled.
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
          At least one device must exist on the node for the
        allocation to succeed.
          Allocation will fail if some devices are already
        allocated,
          unless adminAccess is requested.

        If AllocationMode is not specified, the default mode is
        ExactCount. If the mode is ExactCount and count is not
        specified, the default count is one. Any other requests must
        specify this field.

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.

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
          At least one device must exist on the node for the
        allocation to succeed.
          Allocation will fail if some devices are already
        allocated,
          unless adminAccess is requested.

        If AllocationMode is not specified, the default mode is
        ExactCount. If the mode is ExactCount and count is not
        specified, the default count is one. Any other requests must
        specify this field.

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.

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

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.
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

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.
        """
        self._properties["count"] = value

    @property
    def device_class_name(self) -> str:
        """
        DeviceClassName references a specific DeviceClass, which can
        define additional configuration and selectors to be
        inherited by this request.

        A class is required if no subrequests are specified in the
        firstAvailable list and no class can be set if subrequests
        are specified in the firstAvailable list. Which classes are
        available depends on the cluster.

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

        A class is required if no subrequests are specified in the
        firstAvailable list and no class can be set if subrequests
        are specified in the firstAvailable list. Which classes are
        available depends on the cluster.

        Administrators may use this to restrict which devices may
        get requested by only installing classes with selectors for
        permitted devices. If users are free to request anything
        without restrictions, then administrators can create an
        empty DeviceClass for users to reference.
        """
        self._properties["deviceClassName"] = value

    @property
    def first_available(self) -> typing.List["DeviceSubRequest"]:
        """
        FirstAvailable contains subrequests, of which exactly one
        will be satisfied by the scheduler to satisfy this request.
        It tries to satisfy them in the order in which they are
        listed here. So if there are two entries in the list, the
        scheduler will only check the second one if it determines
        that the first one cannot be used.

        This field may only be set in the entries of
        DeviceClaim.Requests.

        DRA does not yet implement scoring, so the scheduler will
        select the first set of devices that satisfies all the
        requests in the claim. And if the requirements can be
        satisfied on more than one node, other scheduling features
        will determine which node is chosen. This means that the set
        of devices allocated to a claim might not be the optimal set
        available to the cluster. Scoring will be implemented later.
        """
        return typing.cast(
            typing.List["DeviceSubRequest"],
            self._properties.get("firstAvailable"),
        )

    @first_available.setter
    def first_available(
        self, value: typing.Union[typing.List["DeviceSubRequest"], typing.List[dict]]
    ):
        """
        FirstAvailable contains subrequests, of which exactly one
        will be satisfied by the scheduler to satisfy this request.
        It tries to satisfy them in the order in which they are
        listed here. So if there are two entries in the list, the
        scheduler will only check the second one if it determines
        that the first one cannot be used.

        This field may only be set in the entries of
        DeviceClaim.Requests.

        DRA does not yet implement scoring, so the scheduler will
        select the first set of devices that satisfies all the
        requests in the claim. And if the requirements can be
        satisfied on more than one node, other scheduling features
        will determine which node is chosen. This means that the set
        of devices allocated to a claim might not be the optimal set
        available to the cluster. Scoring will be implemented later.
        """
        cleaned: typing.List[DeviceSubRequest] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceSubRequest,
                    DeviceSubRequest().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceSubRequest, item))
        self._properties["firstAvailable"] = cleaned

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

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.
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

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.
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
    def tolerations(self) -> typing.List["DeviceToleration"]:
        """
        If specified, the request's tolerations.

        Tolerations for NoSchedule are required to allocate a device
        which has a taint with that effect. The same applies to
        NoExecute.

        In addition, should any of the allocated devices get tainted
        with NoExecute after allocation and that effect is not
        tolerated, then all pods consuming the ResourceClaim get
        deleted to evict them. The scheduler will not let new pods
        reserve the claim while it has these tainted devices. Once
        all pods are evicted, the claim will get deallocated.

        The maximum number of tolerations is 16.

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        return typing.cast(
            typing.List["DeviceToleration"],
            self._properties.get("tolerations"),
        )

    @tolerations.setter
    def tolerations(
        self, value: typing.Union[typing.List["DeviceToleration"], typing.List[dict]]
    ):
        """
        If specified, the request's tolerations.

        Tolerations for NoSchedule are required to allocate a device
        which has a taint with that effect. The same applies to
        NoExecute.

        In addition, should any of the allocated devices get tainted
        with NoExecute after allocation and that effect is not
        tolerated, then all pods consuming the ResourceClaim get
        deleted to evict them. The scheduler will not let new pods
        reserve the claim while it has these tainted devices. Once
        all pods are evicted, the claim will get deallocated.

        The maximum number of tolerations is 16.

        This field can only be set when deviceClassName is set and
        no subrequests are specified in the firstAvailable list.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        cleaned: typing.List[DeviceToleration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceToleration,
                    DeviceToleration().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceToleration, item))
        self._properties["tolerations"] = cleaned

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
        admin_access: typing.Optional[bool] = None,
        device: typing.Optional[str] = None,
        driver: typing.Optional[str] = None,
        pool: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        tolerations: typing.Optional[typing.List["DeviceToleration"]] = None,
    ):
        """Create DeviceRequestAllocationResult instance."""
        super(DeviceRequestAllocationResult, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceRequestAllocationResult"
        )
        self._properties = {
            "adminAccess": admin_access if admin_access is not None else None,
            "device": device if device is not None else "",
            "driver": driver if driver is not None else "",
            "pool": pool if pool is not None else "",
            "request": request if request is not None else "",
            "tolerations": tolerations if tolerations is not None else [],
        }
        self._types = {
            "adminAccess": (bool, None),
            "device": (str, None),
            "driver": (str, None),
            "pool": (str, None),
            "request": (str, None),
            "tolerations": (list, DeviceToleration),
        }

    @property
    def admin_access(self) -> bool:
        """
        AdminAccess indicates that this device was allocated for
        administrative access. See the corresponding request field
        for a definition of mode.

        This is an alpha field and requires enabling the
        DRAAdminAccess feature gate. Admin access is disabled if
        this field is unset or set to false, otherwise it is
        enabled.
        """
        return typing.cast(
            bool,
            self._properties.get("adminAccess"),
        )

    @admin_access.setter
    def admin_access(self, value: bool):
        """
        AdminAccess indicates that this device was allocated for
        administrative access. See the corresponding request field
        for a definition of mode.

        This is an alpha field and requires enabling the
        DRAAdminAccess feature gate. Admin access is disabled if
        this field is unset or set to false, otherwise it is
        enabled.
        """
        self._properties["adminAccess"] = value

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
        this device to be allocated. If it references a subrequest
        in the firstAvailable list on a DeviceRequest, this field
        must include both the name of the main request and the
        subrequest using the format <main request>/<subrequest>.

        Multiple devices may have been allocated per request.
        """
        return typing.cast(
            str,
            self._properties.get("request"),
        )

    @request.setter
    def request(self, value: str):
        """
        Request is the name of the request in the claim which caused
        this device to be allocated. If it references a subrequest
        in the firstAvailable list on a DeviceRequest, this field
        must include both the name of the main request and the
        subrequest using the format <main request>/<subrequest>.

        Multiple devices may have been allocated per request.
        """
        self._properties["request"] = value

    @property
    def tolerations(self) -> typing.List["DeviceToleration"]:
        """
        A copy of all tolerations specified in the request at the
        time when the device got allocated.

        The maximum number of tolerations is 16.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        return typing.cast(
            typing.List["DeviceToleration"],
            self._properties.get("tolerations"),
        )

    @tolerations.setter
    def tolerations(
        self, value: typing.Union[typing.List["DeviceToleration"], typing.List[dict]]
    ):
        """
        A copy of all tolerations specified in the request at the
        time when the device got allocated.

        The maximum number of tolerations is 16.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        cleaned: typing.List[DeviceToleration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceToleration,
                    DeviceToleration().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceToleration, item))
        self._properties["tolerations"] = cleaned

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


class DeviceSubRequest(_kuber_definitions.Definition):
    """
    DeviceSubRequest describes a request for device provided in
    the claim.spec.devices.requests[].firstAvailable array. Each
    is typically a request for a single resource like a device,
    but can also ask for several identical devices.

    DeviceSubRequest is similar to Request, but doesn't expose
    the AdminAccess or FirstAvailable fields, as those can only
    be set on the top-level request. AdminAccess is not
    supported for requests with a prioritized list, and
    recursive FirstAvailable fields are not supported.
    """

    def __init__(
        self,
        allocation_mode: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        device_class_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        selectors: typing.Optional[typing.List["DeviceSelector"]] = None,
        tolerations: typing.Optional[typing.List["DeviceToleration"]] = None,
    ):
        """Create DeviceSubRequest instance."""
        super(DeviceSubRequest, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceSubRequest"
        )
        self._properties = {
            "allocationMode": allocation_mode if allocation_mode is not None else "",
            "count": count if count is not None else None,
            "deviceClassName": (
                device_class_name if device_class_name is not None else ""
            ),
            "name": name if name is not None else "",
            "selectors": selectors if selectors is not None else [],
            "tolerations": tolerations if tolerations is not None else [],
        }
        self._types = {
            "allocationMode": (str, None),
            "count": (int, None),
            "deviceClassName": (str, None),
            "name": (str, None),
            "selectors": (list, DeviceSelector),
            "tolerations": (list, DeviceToleration),
        }

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

        If AllocationMode is not specified, the default mode is
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

        If AllocationMode is not specified, the default mode is
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
        inherited by this subrequest.

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
        inherited by this subrequest.

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
        Name can be used to reference this subrequest in the list of
        constraints or the list of configurations for the claim.
        References must use the format <main request>/<subrequest>.

        Must be a DNS label.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name can be used to reference this subrequest in the list of
        constraints or the list of configurations for the claim.
        References must use the format <main request>/<subrequest>.

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

    @property
    def tolerations(self) -> typing.List["DeviceToleration"]:
        """
        If specified, the request's tolerations.

        Tolerations for NoSchedule are required to allocate a device
        which has a taint with that effect. The same applies to
        NoExecute.

        In addition, should any of the allocated devices get tainted
        with NoExecute after allocation and that effect is not
        tolerated, then all pods consuming the ResourceClaim get
        deleted to evict them. The scheduler will not let new pods
        reserve the claim while it has these tainted devices. Once
        all pods are evicted, the claim will get deallocated.

        The maximum number of tolerations is 16.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        return typing.cast(
            typing.List["DeviceToleration"],
            self._properties.get("tolerations"),
        )

    @tolerations.setter
    def tolerations(
        self, value: typing.Union[typing.List["DeviceToleration"], typing.List[dict]]
    ):
        """
        If specified, the request's tolerations.

        Tolerations for NoSchedule are required to allocate a device
        which has a taint with that effect. The same applies to
        NoExecute.

        In addition, should any of the allocated devices get tainted
        with NoExecute after allocation and that effect is not
        tolerated, then all pods consuming the ResourceClaim get
        deleted to evict them. The scheduler will not let new pods
        reserve the claim while it has these tainted devices. Once
        all pods are evicted, the claim will get deallocated.

        The maximum number of tolerations is 16.

        This is an alpha field and requires enabling the
        DRADeviceTaints feature gate.
        """
        cleaned: typing.List[DeviceToleration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceToleration,
                    DeviceToleration().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceToleration, item))
        self._properties["tolerations"] = cleaned

    def __enter__(self) -> "DeviceSubRequest":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceTaint(_kuber_definitions.Definition):
    """
    The device this taint is attached to has the "effect" on any
    claim which does not tolerate the taint and, through the
    claim, to pods using the claim.
    """

    def __init__(
        self,
        effect: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        time_added: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
    ):
        """Create DeviceTaint instance."""
        super(DeviceTaint, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceTaint"
        )
        self._properties = {
            "effect": effect if effect is not None else "",
            "key": key if key is not None else "",
            "timeAdded": time_added if time_added is not None else None,
            "value": value if value is not None else "",
        }
        self._types = {
            "effect": (str, None),
            "key": (str, None),
            "timeAdded": (str, None),
            "value": (str, None),
        }

    @property
    def effect(self) -> str:
        """
        The effect of the taint on claims that do not tolerate the
        taint and through such claims on the pods using them. Valid
        effects are NoSchedule and NoExecute. PreferNoSchedule as
        used for nodes is not valid here.
        """
        return typing.cast(
            str,
            self._properties.get("effect"),
        )

    @effect.setter
    def effect(self, value: str):
        """
        The effect of the taint on claims that do not tolerate the
        taint and through such claims on the pods using them. Valid
        effects are NoSchedule and NoExecute. PreferNoSchedule as
        used for nodes is not valid here.
        """
        self._properties["effect"] = value

    @property
    def key(self) -> str:
        """
        The taint key to be applied to a device. Must be a label
        name.
        """
        return typing.cast(
            str,
            self._properties.get("key"),
        )

    @key.setter
    def key(self, value: str):
        """
        The taint key to be applied to a device. Must be a label
        name.
        """
        self._properties["key"] = value

    @property
    def time_added(self) -> str:
        """
        TimeAdded represents the time at which the taint was added.
        Added automatically during create or update if not set.
        """
        return typing.cast(
            str,
            self._properties.get("timeAdded"),
        )

    @time_added.setter
    def time_added(self, value: typing.Union[str, _datetime.datetime, _datetime.date]):
        """
        TimeAdded represents the time at which the taint was added.
        Added automatically during create or update if not set.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["timeAdded"] = value

    @property
    def value(self) -> str:
        """
        The taint value corresponding to the taint key. Must be a
        label value.
        """
        return typing.cast(
            str,
            self._properties.get("value"),
        )

    @value.setter
    def value(self, value: str):
        """
        The taint value corresponding to the taint key. Must be a
        label value.
        """
        self._properties["value"] = value

    def __enter__(self) -> "DeviceTaint":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceTaintRule(_kuber_definitions.Resource):
    """
    DeviceTaintRule adds one taint to all devices which match
    the selector. This has the same effect as if the taint was
    specified directly in the ResourceSlice by the DRA driver.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["DeviceTaintRuleSpec"] = None,
    ):
        """Create DeviceTaintRule instance."""
        super(DeviceTaintRule, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceTaintRule"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else DeviceTaintRuleSpec(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (DeviceTaintRuleSpec, None),
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
    def spec(self) -> "DeviceTaintRuleSpec":
        """
        Spec specifies the selector and one taint.

        Changing the spec automatically increments the
        metadata.generation number.
        """
        return typing.cast(
            "DeviceTaintRuleSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["DeviceTaintRuleSpec", dict]):
        """
        Spec specifies the selector and one taint.

        Changing the spec automatically increments the
        metadata.generation number.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeviceTaintRuleSpec,
                DeviceTaintRuleSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the DeviceTaintRule in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_device_taint_rule", "create_device_taint_rule"]

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
        Replaces the DeviceTaintRule in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_device_taint_rule", "replace_device_taint_rule"]

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
        Patches the DeviceTaintRule in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_device_taint_rule", "patch_device_taint_rule"]

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
        Reads the DeviceTaintRule from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_device_taint_rule",
            "read_device_taint_rule",
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
        Deletes the DeviceTaintRule from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_device_taint_rule",
            "delete_device_taint_rule",
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

    def __enter__(self) -> "DeviceTaintRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceTaintRuleList(_kuber_definitions.Collection):
    """
    DeviceTaintRuleList is a collection of DeviceTaintRules.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["DeviceTaintRule"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create DeviceTaintRuleList instance."""
        super(DeviceTaintRuleList, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceTaintRuleList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, DeviceTaintRule),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["DeviceTaintRule"]:
        """
        Items is the list of DeviceTaintRules.
        """
        return typing.cast(
            typing.List["DeviceTaintRule"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["DeviceTaintRule"], typing.List[dict]]
    ):
        """
        Items is the list of DeviceTaintRules.
        """
        cleaned: typing.List[DeviceTaintRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    DeviceTaintRule,
                    DeviceTaintRule().from_dict(item),
                )
            cleaned.append(typing.cast(DeviceTaintRule, item))
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

    def __enter__(self) -> "DeviceTaintRuleList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceTaintRuleSpec(_kuber_definitions.Definition):
    """
    DeviceTaintRuleSpec specifies the selector and one taint.
    """

    def __init__(
        self,
        device_selector: typing.Optional["DeviceTaintSelector"] = None,
        taint: typing.Optional["DeviceTaint"] = None,
    ):
        """Create DeviceTaintRuleSpec instance."""
        super(DeviceTaintRuleSpec, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceTaintRuleSpec"
        )
        self._properties = {
            "deviceSelector": (
                device_selector
                if device_selector is not None
                else DeviceTaintSelector()
            ),
            "taint": taint if taint is not None else DeviceTaint(),
        }
        self._types = {
            "deviceSelector": (DeviceTaintSelector, None),
            "taint": (DeviceTaint, None),
        }

    @property
    def device_selector(self) -> "DeviceTaintSelector":
        """
        DeviceSelector defines which device(s) the taint is applied
        to. All selector criteria must be satified for a device to
        match. The empty selector matches all devices. Without a
        selector, no devices are matches.
        """
        return typing.cast(
            "DeviceTaintSelector",
            self._properties.get("deviceSelector"),
        )

    @device_selector.setter
    def device_selector(self, value: typing.Union["DeviceTaintSelector", dict]):
        """
        DeviceSelector defines which device(s) the taint is applied
        to. All selector criteria must be satified for a device to
        match. The empty selector matches all devices. Without a
        selector, no devices are matches.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeviceTaintSelector,
                DeviceTaintSelector().from_dict(value),
            )
        self._properties["deviceSelector"] = value

    @property
    def taint(self) -> "DeviceTaint":
        """
        The taint that gets applied to matching devices.
        """
        return typing.cast(
            "DeviceTaint",
            self._properties.get("taint"),
        )

    @taint.setter
    def taint(self, value: typing.Union["DeviceTaint", dict]):
        """
        The taint that gets applied to matching devices.
        """
        if isinstance(value, dict):
            value = typing.cast(
                DeviceTaint,
                DeviceTaint().from_dict(value),
            )
        self._properties["taint"] = value

    def __enter__(self) -> "DeviceTaintRuleSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceTaintSelector(_kuber_definitions.Definition):
    """
    DeviceTaintSelector defines which device(s) a
    DeviceTaintRule applies to. The empty selector matches all
    devices. Without a selector, no devices are matched.
    """

    def __init__(
        self,
        device: typing.Optional[str] = None,
        device_class_name: typing.Optional[str] = None,
        driver: typing.Optional[str] = None,
        pool: typing.Optional[str] = None,
        selectors: typing.Optional[typing.List["DeviceSelector"]] = None,
    ):
        """Create DeviceTaintSelector instance."""
        super(DeviceTaintSelector, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceTaintSelector"
        )
        self._properties = {
            "device": device if device is not None else "",
            "deviceClassName": (
                device_class_name if device_class_name is not None else ""
            ),
            "driver": driver if driver is not None else "",
            "pool": pool if pool is not None else "",
            "selectors": selectors if selectors is not None else [],
        }
        self._types = {
            "device": (str, None),
            "deviceClassName": (str, None),
            "driver": (str, None),
            "pool": (str, None),
            "selectors": (list, DeviceSelector),
        }

    @property
    def device(self) -> str:
        """
        If device is set, only devices with that name are selected.
        This field corresponds to slice.spec.devices[].name.

        Setting also driver and pool may be required to avoid
        ambiguity, but is not required.
        """
        return typing.cast(
            str,
            self._properties.get("device"),
        )

    @device.setter
    def device(self, value: str):
        """
        If device is set, only devices with that name are selected.
        This field corresponds to slice.spec.devices[].name.

        Setting also driver and pool may be required to avoid
        ambiguity, but is not required.
        """
        self._properties["device"] = value

    @property
    def device_class_name(self) -> str:
        """
        If DeviceClassName is set, the selectors defined there must
        be satisfied by a device to be selected. This field
        corresponds to class.metadata.name.
        """
        return typing.cast(
            str,
            self._properties.get("deviceClassName"),
        )

    @device_class_name.setter
    def device_class_name(self, value: str):
        """
        If DeviceClassName is set, the selectors defined there must
        be satisfied by a device to be selected. This field
        corresponds to class.metadata.name.
        """
        self._properties["deviceClassName"] = value

    @property
    def driver(self) -> str:
        """
        If driver is set, only devices from that driver are
        selected. This fields corresponds to slice.spec.driver.
        """
        return typing.cast(
            str,
            self._properties.get("driver"),
        )

    @driver.setter
    def driver(self, value: str):
        """
        If driver is set, only devices from that driver are
        selected. This fields corresponds to slice.spec.driver.
        """
        self._properties["driver"] = value

    @property
    def pool(self) -> str:
        """
        If pool is set, only devices in that pool are selected.

        Also setting the driver name may be useful to avoid
        ambiguity when different drivers use the same pool name, but
        this is not required because selecting pools from different
        drivers may also be useful, for example when drivers with
        node-local devices use the node name as their pool name.
        """
        return typing.cast(
            str,
            self._properties.get("pool"),
        )

    @pool.setter
    def pool(self, value: str):
        """
        If pool is set, only devices in that pool are selected.

        Also setting the driver name may be useful to avoid
        ambiguity when different drivers use the same pool name, but
        this is not required because selecting pools from different
        drivers may also be useful, for example when drivers with
        node-local devices use the node name as their pool name.
        """
        self._properties["pool"] = value

    @property
    def selectors(self) -> typing.List["DeviceSelector"]:
        """
        Selectors contains the same selection criteria as a
        ResourceClaim. Currently, CEL expressions are supported. All
        of these selectors must be satisfied.
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
        Selectors contains the same selection criteria as a
        ResourceClaim. Currently, CEL expressions are supported. All
        of these selectors must be satisfied.
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

    def __enter__(self) -> "DeviceTaintSelector":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class DeviceToleration(_kuber_definitions.Definition):
    """
    The ResourceClaim this DeviceToleration is attached to
    tolerates any taint that matches the triple
    <key,value,effect> using the matching operator <operator>.
    """

    def __init__(
        self,
        effect: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        operator: typing.Optional[str] = None,
        toleration_seconds: typing.Optional[int] = None,
        value: typing.Optional[str] = None,
    ):
        """Create DeviceToleration instance."""
        super(DeviceToleration, self).__init__(
            api_version="resource/v1alpha3", kind="DeviceToleration"
        )
        self._properties = {
            "effect": effect if effect is not None else "",
            "key": key if key is not None else "",
            "operator": operator if operator is not None else "",
            "tolerationSeconds": (
                toleration_seconds if toleration_seconds is not None else None
            ),
            "value": value if value is not None else "",
        }
        self._types = {
            "effect": (str, None),
            "key": (str, None),
            "operator": (str, None),
            "tolerationSeconds": (int, None),
            "value": (str, None),
        }

    @property
    def effect(self) -> str:
        """
        Effect indicates the taint effect to match. Empty means
        match all taint effects. When specified, allowed values are
        NoSchedule and NoExecute.
        """
        return typing.cast(
            str,
            self._properties.get("effect"),
        )

    @effect.setter
    def effect(self, value: str):
        """
        Effect indicates the taint effect to match. Empty means
        match all taint effects. When specified, allowed values are
        NoSchedule and NoExecute.
        """
        self._properties["effect"] = value

    @property
    def key(self) -> str:
        """
        Key is the taint key that the toleration applies to. Empty
        means match all taint keys. If the key is empty, operator
        must be Exists; this combination means to match all values
        and all keys. Must be a label name.
        """
        return typing.cast(
            str,
            self._properties.get("key"),
        )

    @key.setter
    def key(self, value: str):
        """
        Key is the taint key that the toleration applies to. Empty
        means match all taint keys. If the key is empty, operator
        must be Exists; this combination means to match all values
        and all keys. Must be a label name.
        """
        self._properties["key"] = value

    @property
    def operator(self) -> str:
        """
        Operator represents a key's relationship to the value. Valid
        operators are Exists and Equal. Defaults to Equal. Exists is
        equivalent to wildcard for value, so that a ResourceClaim
        can tolerate all taints of a particular category.
        """
        return typing.cast(
            str,
            self._properties.get("operator"),
        )

    @operator.setter
    def operator(self, value: str):
        """
        Operator represents a key's relationship to the value. Valid
        operators are Exists and Equal. Defaults to Equal. Exists is
        equivalent to wildcard for value, so that a ResourceClaim
        can tolerate all taints of a particular category.
        """
        self._properties["operator"] = value

    @property
    def toleration_seconds(self) -> int:
        """
        TolerationSeconds represents the period of time the
        toleration (which must be of effect NoExecute, otherwise
        this field is ignored) tolerates the taint. By default, it
        is not set, which means tolerate the taint forever (do not
        evict). Zero and negative values will be treated as 0 (evict
        immediately) by the system. If larger than zero, the time
        when the pod needs to be evicted is calculated as <time when
        taint was adedd> + <toleration seconds>.
        """
        return typing.cast(
            int,
            self._properties.get("tolerationSeconds"),
        )

    @toleration_seconds.setter
    def toleration_seconds(self, value: int):
        """
        TolerationSeconds represents the period of time the
        toleration (which must be of effect NoExecute, otherwise
        this field is ignored) tolerates the taint. By default, it
        is not set, which means tolerate the taint forever (do not
        evict). Zero and negative values will be treated as 0 (evict
        immediately) by the system. If larger than zero, the time
        when the pod needs to be evicted is calculated as <time when
        taint was adedd> + <toleration seconds>.
        """
        self._properties["tolerationSeconds"] = value

    @property
    def value(self) -> str:
        """
        Value is the taint value the toleration matches to. If the
        operator is Exists, the value must be empty, otherwise just
        a regular string. Must be a label value.
        """
        return typing.cast(
            str,
            self._properties.get("value"),
        )

    @value.setter
    def value(self, value: str):
        """
        Value is the taint value the toleration matches to. If the
        operator is Exists, the value must be empty, otherwise just
        a regular string. Must be a label value.
        """
        self._properties["value"] = value

    def __enter__(self) -> "DeviceToleration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NetworkDeviceData(_kuber_definitions.Definition):
    """
    NetworkDeviceData provides network-related details for the
    allocated device. This information may be filled by drivers
    or other components to configure or identify the device
    within a network context.
    """

    def __init__(
        self,
        hardware_address: typing.Optional[str] = None,
        interface_name: typing.Optional[str] = None,
        ips: typing.Optional[typing.List[str]] = None,
    ):
        """Create NetworkDeviceData instance."""
        super(NetworkDeviceData, self).__init__(
            api_version="resource/v1alpha3", kind="NetworkDeviceData"
        )
        self._properties = {
            "hardwareAddress": hardware_address if hardware_address is not None else "",
            "interfaceName": interface_name if interface_name is not None else "",
            "ips": ips if ips is not None else [],
        }
        self._types = {
            "hardwareAddress": (str, None),
            "interfaceName": (str, None),
            "ips": (list, str),
        }

    @property
    def hardware_address(self) -> str:
        """
        HardwareAddress represents the hardware address (e.g. MAC
        Address) of the device's network interface.

        Must not be longer than 128 characters.
        """
        return typing.cast(
            str,
            self._properties.get("hardwareAddress"),
        )

    @hardware_address.setter
    def hardware_address(self, value: str):
        """
        HardwareAddress represents the hardware address (e.g. MAC
        Address) of the device's network interface.

        Must not be longer than 128 characters.
        """
        self._properties["hardwareAddress"] = value

    @property
    def interface_name(self) -> str:
        """
        InterfaceName specifies the name of the network interface
        associated with the allocated device. This might be the name
        of a physical or virtual network interface being configured
        in the pod.

        Must not be longer than 256 characters.
        """
        return typing.cast(
            str,
            self._properties.get("interfaceName"),
        )

    @interface_name.setter
    def interface_name(self, value: str):
        """
        InterfaceName specifies the name of the network interface
        associated with the allocated device. This might be the name
        of a physical or virtual network interface being configured
        in the pod.

        Must not be longer than 256 characters.
        """
        self._properties["interfaceName"] = value

    @property
    def ips(self) -> typing.List[str]:
        """
        IPs lists the network addresses assigned to the device's
        network interface. This can include both IPv4 and IPv6
        addresses. The IPs are in the CIDR notation, which includes
        both the address and the associated subnet mask. e.g.:
        "192.0.2.5/24" for IPv4 and "2001:db8::5/64" for IPv6.

        Must not contain more than 16 entries.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("ips"),
        )

    @ips.setter
    def ips(self, value: typing.List[str]):
        """
        IPs lists the network addresses assigned to the device's
        network interface. This can include both IPv4 and IPv6
        addresses. The IPs are in the CIDR notation, which includes
        both the address and the associated subnet mask. e.g.:
        "192.0.2.5/24" for IPv4 and "2001:db8::5/64" for IPv6.

        Must not contain more than 16 entries.
        """
        self._properties["ips"] = value

    def __enter__(self) -> "NetworkDeviceData":
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

        The length of the raw data must be smaller or equal to 10
        Ki.
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

        The length of the raw data must be smaller or equal to 10
        Ki.
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


class ResourceClaimSpec(_kuber_definitions.Definition):
    """
    ResourceClaimSpec defines what is being requested in a
    ResourceClaim and how to configure it.
    """

    def __init__(
        self,
        devices: typing.Optional["DeviceClaim"] = None,
    ):
        """Create ResourceClaimSpec instance."""
        super(ResourceClaimSpec, self).__init__(
            api_version="resource/v1alpha3", kind="ResourceClaimSpec"
        )
        self._properties = {
            "devices": devices if devices is not None else DeviceClaim(),
        }
        self._types = {
            "devices": (DeviceClaim, None),
        }

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
        devices: typing.Optional[typing.List["AllocatedDeviceStatus"]] = None,
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
            "devices": devices if devices is not None else [],
            "reservedFor": reserved_for if reserved_for is not None else [],
        }
        self._types = {
            "allocation": (AllocationResult, None),
            "devices": (list, AllocatedDeviceStatus),
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
    def devices(self) -> typing.List["AllocatedDeviceStatus"]:
        """
        Devices contains the status of each device allocated for
        this claim, as reported by the driver. This can include
        driver-specific information. Entries are owned by their
        respective drivers.
        """
        return typing.cast(
            typing.List["AllocatedDeviceStatus"],
            self._properties.get("devices"),
        )

    @devices.setter
    def devices(
        self,
        value: typing.Union[typing.List["AllocatedDeviceStatus"], typing.List[dict]],
    ):
        """
        Devices contains the status of each device allocated for
        this claim, as reported by the driver. This can include
        driver-specific information. Entries are owned by their
        respective drivers.
        """
        cleaned: typing.List[AllocatedDeviceStatus] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    AllocatedDeviceStatus,
                    AllocatedDeviceStatus().from_dict(item),
                )
            cleaned.append(typing.cast(AllocatedDeviceStatus, item))
        self._properties["devices"] = cleaned

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

        There can be at most 256 such reservations. This may get
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

        There can be at most 256 such reservations. This may get
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
        copied into the ResourceClaim when creating it. No other
        fields are allowed and will be rejected during validation.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        ObjectMeta may contain labels and annotations that will be
        copied into the ResourceClaim when creating it. No other
        fields are allowed and will be rejected during validation.
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
        per_device_node_selection: typing.Optional[bool] = None,
        pool: typing.Optional["ResourcePool"] = None,
        shared_counters: typing.Optional[typing.List["CounterSet"]] = None,
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
            "perDeviceNodeSelection": (
                per_device_node_selection
                if per_device_node_selection is not None
                else None
            ),
            "pool": pool if pool is not None else ResourcePool(),
            "sharedCounters": shared_counters if shared_counters is not None else [],
        }
        self._types = {
            "allNodes": (bool, None),
            "devices": (list, Device),
            "driver": (str, None),
            "nodeName": (str, None),
            "nodeSelector": (NodeSelector, None),
            "perDeviceNodeSelection": (bool, None),
            "pool": (ResourcePool, None),
            "sharedCounters": (list, CounterSet),
        }

    @property
    def all_nodes(self) -> bool:
        """
        AllNodes indicates that all nodes have access to the
        resources in the pool.

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set.
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

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set.
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

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set. This field is immutable.
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

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set. This field is immutable.
        """
        self._properties["nodeName"] = value

    @property
    def node_selector(self) -> "NodeSelector":
        """
        NodeSelector defines which nodes have access to the
        resources in the pool, when that pool is not limited to a
        single node.

        Must use exactly one term.

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set.
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

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set.
        """
        if isinstance(value, dict):
            value = typing.cast(
                NodeSelector,
                NodeSelector().from_dict(value),
            )
        self._properties["nodeSelector"] = value

    @property
    def per_device_node_selection(self) -> bool:
        """
        PerDeviceNodeSelection defines whether the access from nodes
        to resources in the pool is set on the ResourceSlice level
        or on each device. If it is set to true, every device
        defined the ResourceSlice must specify this individually.

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set.
        """
        return typing.cast(
            bool,
            self._properties.get("perDeviceNodeSelection"),
        )

    @per_device_node_selection.setter
    def per_device_node_selection(self, value: bool):
        """
        PerDeviceNodeSelection defines whether the access from nodes
        to resources in the pool is set on the ResourceSlice level
        or on each device. If it is set to true, every device
        defined the ResourceSlice must specify this individually.

        Exactly one of NodeName, NodeSelector, AllNodes, and
        PerDeviceNodeSelection must be set.
        """
        self._properties["perDeviceNodeSelection"] = value

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

    @property
    def shared_counters(self) -> typing.List["CounterSet"]:
        """
        SharedCounters defines a list of counter sets, each of which
        has a name and a list of counters available.

        The names of the SharedCounters must be unique in the
        ResourceSlice.

        The maximum number of SharedCounters is 32.
        """
        return typing.cast(
            typing.List["CounterSet"],
            self._properties.get("sharedCounters"),
        )

    @shared_counters.setter
    def shared_counters(
        self, value: typing.Union[typing.List["CounterSet"], typing.List[dict]]
    ):
        """
        SharedCounters defines a list of counter sets, each of which
        has a name and a list of counters available.

        The names of the SharedCounters must be unique in the
        ResourceSlice.

        The maximum number of SharedCounters is 32.
        """
        cleaned: typing.List[CounterSet] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CounterSet,
                    CounterSet().from_dict(item),
                )
            cleaned.append(typing.cast(CounterSet, item))
        self._properties["sharedCounters"] = cleaned

    def __enter__(self) -> "ResourceSliceSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
