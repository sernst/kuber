import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_17.meta_v1 import ListMeta
from kuber.v1_17.meta_v1 import ObjectMeta
from kuber.v1_17.core_v1 import ObjectReference


class Endpoint(_kuber_definitions.Definition):
    """
    Endpoint represents a single logical "backend" implementing
    a service.
    """

    def __init__(
        self,
        addresses: typing.List[str] = None,
        conditions: "EndpointConditions" = None,
        hostname: str = None,
        target_ref: "ObjectReference" = None,
        topology: dict = None,
    ):
        """Create Endpoint instance."""
        super(Endpoint, self).__init__(api_version="discovery/v1beta1", kind="Endpoint")
        self._properties = {
            "addresses": addresses if addresses is not None else [],
            "conditions": conditions
            if conditions is not None
            else EndpointConditions(),
            "hostname": hostname if hostname is not None else "",
            "targetRef": target_ref if target_ref is not None else ObjectReference(),
            "topology": topology if topology is not None else {},
        }
        self._types = {
            "addresses": (list, str),
            "conditions": (EndpointConditions, None),
            "hostname": (str, None),
            "targetRef": (ObjectReference, None),
            "topology": (dict, None),
        }

    @property
    def addresses(self) -> typing.List[str]:
        """
        addresses of this endpoint. The contents of this field are
        interpreted according to the corresponding EndpointSlice
        addressType field. Consumers must handle different types of
        addresses in the context of their own capabilities. This
        must contain at least one address but no more than 100.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("addresses"),
        )

    @addresses.setter
    def addresses(self, value: typing.List[str]):
        """
        addresses of this endpoint. The contents of this field are
        interpreted according to the corresponding EndpointSlice
        addressType field. Consumers must handle different types of
        addresses in the context of their own capabilities. This
        must contain at least one address but no more than 100.
        """
        self._properties["addresses"] = value

    @property
    def conditions(self) -> "EndpointConditions":
        """
        conditions contains information about the current status of
        the endpoint.
        """
        return typing.cast(
            "EndpointConditions",
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(self, value: typing.Union["EndpointConditions", dict]):
        """
        conditions contains information about the current status of
        the endpoint.
        """
        if isinstance(value, dict):
            value = typing.cast(
                EndpointConditions,
                EndpointConditions().from_dict(value),
            )
        self._properties["conditions"] = value

    @property
    def hostname(self) -> str:
        """
        hostname of this endpoint. This field may be used by
        consumers of endpoints to distinguish endpoints from each
        other (e.g. in DNS names). Multiple endpoints which use the
        same hostname should be considered fungible (e.g. multiple A
        values in DNS). Must pass DNS Label (RFC 1123) validation.
        """
        return typing.cast(
            str,
            self._properties.get("hostname"),
        )

    @hostname.setter
    def hostname(self, value: str):
        """
        hostname of this endpoint. This field may be used by
        consumers of endpoints to distinguish endpoints from each
        other (e.g. in DNS names). Multiple endpoints which use the
        same hostname should be considered fungible (e.g. multiple A
        values in DNS). Must pass DNS Label (RFC 1123) validation.
        """
        self._properties["hostname"] = value

    @property
    def target_ref(self) -> "ObjectReference":
        """
        targetRef is a reference to a Kubernetes object that
        represents this endpoint.
        """
        return typing.cast(
            "ObjectReference",
            self._properties.get("targetRef"),
        )

    @target_ref.setter
    def target_ref(self, value: typing.Union["ObjectReference", dict]):
        """
        targetRef is a reference to a Kubernetes object that
        represents this endpoint.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectReference,
                ObjectReference().from_dict(value),
            )
        self._properties["targetRef"] = value

    @property
    def topology(self) -> dict:
        """
        topology contains arbitrary topology information associated
        with the endpoint. These key/value pairs must conform with
        the label format.
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels Topology may include a maximum of 16
        key/value pairs. This includes, but is not limited to the
        following well known keys: * kubernetes.io/hostname: the
        value indicates the hostname of the node
          where the endpoint is located. This should match the
        corresponding
          node label.
        * topology.kubernetes.io/zone: the value indicates the zone
        where the
          endpoint is located. This should match the corresponding
        node label.
        * topology.kubernetes.io/region: the value indicates the
        region where the
          endpoint is located. This should match the corresponding
        node label.
        """
        return typing.cast(
            dict,
            self._properties.get("topology"),
        )

    @topology.setter
    def topology(self, value: dict):
        """
        topology contains arbitrary topology information associated
        with the endpoint. These key/value pairs must conform with
        the label format.
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels Topology may include a maximum of 16
        key/value pairs. This includes, but is not limited to the
        following well known keys: * kubernetes.io/hostname: the
        value indicates the hostname of the node
          where the endpoint is located. This should match the
        corresponding
          node label.
        * topology.kubernetes.io/zone: the value indicates the zone
        where the
          endpoint is located. This should match the corresponding
        node label.
        * topology.kubernetes.io/region: the value indicates the
        region where the
          endpoint is located. This should match the corresponding
        node label.
        """
        self._properties["topology"] = value

    def __enter__(self) -> "Endpoint":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointConditions(_kuber_definitions.Definition):
    """
    EndpointConditions represents the current condition of an
    endpoint.
    """

    def __init__(
        self,
        ready: bool = None,
    ):
        """Create EndpointConditions instance."""
        super(EndpointConditions, self).__init__(
            api_version="discovery/v1beta1", kind="EndpointConditions"
        )
        self._properties = {
            "ready": ready if ready is not None else None,
        }
        self._types = {
            "ready": (bool, None),
        }

    @property
    def ready(self) -> bool:
        """
        ready indicates that this endpoint is prepared to receive
        traffic, according to whatever system is managing the
        endpoint. A nil value indicates an unknown state. In most
        cases consumers should interpret this unknown state as
        ready.
        """
        return typing.cast(
            bool,
            self._properties.get("ready"),
        )

    @ready.setter
    def ready(self, value: bool):
        """
        ready indicates that this endpoint is prepared to receive
        traffic, according to whatever system is managing the
        endpoint. A nil value indicates an unknown state. In most
        cases consumers should interpret this unknown state as
        ready.
        """
        self._properties["ready"] = value

    def __enter__(self) -> "EndpointConditions":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointPort(_kuber_definitions.Definition):
    """
    EndpointPort represents a Port used by an EndpointSlice
    """

    def __init__(
        self,
        app_protocol: str = None,
        name: str = None,
        port: int = None,
        protocol: str = None,
    ):
        """Create EndpointPort instance."""
        super(EndpointPort, self).__init__(
            api_version="discovery/v1beta1", kind="EndpointPort"
        )
        self._properties = {
            "appProtocol": app_protocol if app_protocol is not None else "",
            "name": name if name is not None else "",
            "port": port if port is not None else None,
            "protocol": protocol if protocol is not None else "",
        }
        self._types = {
            "appProtocol": (str, None),
            "name": (str, None),
            "port": (int, None),
            "protocol": (str, None),
        }

    @property
    def app_protocol(self) -> str:
        """
        The application protocol for this port. This field follows
        standard Kubernetes label syntax. Un-prefixed names are
        reserved for IANA standard service names (as per RFC-6335
        and http://www.iana.org/assignments/service-names). Non-
        standard protocols should use prefixed names. Default is
        empty string.
        """
        return typing.cast(
            str,
            self._properties.get("appProtocol"),
        )

    @app_protocol.setter
    def app_protocol(self, value: str):
        """
        The application protocol for this port. This field follows
        standard Kubernetes label syntax. Un-prefixed names are
        reserved for IANA standard service names (as per RFC-6335
        and http://www.iana.org/assignments/service-names). Non-
        standard protocols should use prefixed names. Default is
        empty string.
        """
        self._properties["appProtocol"] = value

    @property
    def name(self) -> str:
        """
        The name of this port. All ports in an EndpointSlice must
        have a unique name. If the EndpointSlice is dervied from a
        Kubernetes service, this corresponds to the
        Service.ports[].name. Name must either be an empty string or
        pass DNS_LABEL validation: * must be no more than 63
        characters long. * must consist of lower case alphanumeric
        characters or '-'. * must start and end with an alphanumeric
        character. Default is empty string.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        The name of this port. All ports in an EndpointSlice must
        have a unique name. If the EndpointSlice is dervied from a
        Kubernetes service, this corresponds to the
        Service.ports[].name. Name must either be an empty string or
        pass DNS_LABEL validation: * must be no more than 63
        characters long. * must consist of lower case alphanumeric
        characters or '-'. * must start and end with an alphanumeric
        character. Default is empty string.
        """
        self._properties["name"] = value

    @property
    def port(self) -> int:
        """
        The port number of the endpoint. If this is not specified,
        ports are not restricted and must be interpreted in the
        context of the specific consumer.
        """
        return typing.cast(
            int,
            self._properties.get("port"),
        )

    @port.setter
    def port(self, value: int):
        """
        The port number of the endpoint. If this is not specified,
        ports are not restricted and must be interpreted in the
        context of the specific consumer.
        """
        self._properties["port"] = value

    @property
    def protocol(self) -> str:
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP.
        Default is TCP.
        """
        return typing.cast(
            str,
            self._properties.get("protocol"),
        )

    @protocol.setter
    def protocol(self, value: str):
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP.
        Default is TCP.
        """
        self._properties["protocol"] = value

    def __enter__(self) -> "EndpointPort":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointSlice(_kuber_definitions.Resource):
    """
    EndpointSlice represents a subset of the endpoints that
    implement a service. For a given service there may be
    multiple EndpointSlice objects, selected by labels, which
    must be joined to produce the full set of endpoints.
    """

    def __init__(
        self,
        address_type: str = None,
        endpoints: typing.List["Endpoint"] = None,
        metadata: "ObjectMeta" = None,
        ports: typing.List["EndpointPort"] = None,
    ):
        """Create EndpointSlice instance."""
        super(EndpointSlice, self).__init__(
            api_version="discovery/v1beta1", kind="EndpointSlice"
        )
        self._properties = {
            "addressType": address_type if address_type is not None else "",
            "endpoints": endpoints if endpoints is not None else [],
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "ports": ports if ports is not None else [],
        }
        self._types = {
            "addressType": (str, None),
            "apiVersion": (str, None),
            "endpoints": (list, Endpoint),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "ports": (list, EndpointPort),
        }

    @property
    def address_type(self) -> str:
        """
        addressType specifies the type of address carried by this
        EndpointSlice. All addresses in this slice must be the same
        type. This field is immutable after creation. The following
        address types are currently supported: * IPv4: Represents an
        IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN:
        Represents a Fully Qualified Domain Name.
        """
        return typing.cast(
            str,
            self._properties.get("addressType"),
        )

    @address_type.setter
    def address_type(self, value: str):
        """
        addressType specifies the type of address carried by this
        EndpointSlice. All addresses in this slice must be the same
        type. This field is immutable after creation. The following
        address types are currently supported: * IPv4: Represents an
        IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN:
        Represents a Fully Qualified Domain Name.
        """
        self._properties["addressType"] = value

    @property
    def endpoints(self) -> typing.List["Endpoint"]:
        """
        endpoints is a list of unique endpoints in this slice. Each
        slice may include a maximum of 1000 endpoints.
        """
        return typing.cast(
            typing.List["Endpoint"],
            self._properties.get("endpoints"),
        )

    @endpoints.setter
    def endpoints(
        self, value: typing.Union[typing.List["Endpoint"], typing.List[dict]]
    ):
        """
        endpoints is a list of unique endpoints in this slice. Each
        slice may include a maximum of 1000 endpoints.
        """
        cleaned: typing.List[Endpoint] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Endpoint,
                    Endpoint().from_dict(item),
                )
            cleaned.append(typing.cast(Endpoint, item))
        self._properties["endpoints"] = cleaned

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object's metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def ports(self) -> typing.List["EndpointPort"]:
        """
        ports specifies the list of network ports exposed by each
        endpoint in this slice. Each port must have a unique name.
        When ports is empty, it indicates that there are no defined
        ports. When a port is defined with a nil port value, it
        indicates "all ports". Each slice may include a maximum of
        100 ports.
        """
        return typing.cast(
            typing.List["EndpointPort"],
            self._properties.get("ports"),
        )

    @ports.setter
    def ports(
        self, value: typing.Union[typing.List["EndpointPort"], typing.List[dict]]
    ):
        """
        ports specifies the list of network ports exposed by each
        endpoint in this slice. Each port must have a unique name.
        When ports is empty, it indicates that there are no defined
        ports. When a port is defined with a nil port value, it
        indicates "all ports". Each slice may include a maximum of
        100 ports.
        """
        cleaned: typing.List[EndpointPort] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    EndpointPort,
                    EndpointPort().from_dict(item),
                )
            cleaned.append(typing.cast(EndpointPort, item))
        self._properties["ports"] = cleaned

    def create_resource(self, namespace: "str" = None):
        """
        Creates the EndpointSlice in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_endpoint_slice", "create_endpoint_slice"]

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
        Replaces the EndpointSlice in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_endpoint_slice", "replace_endpoint_slice"]

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
        Patches the EndpointSlice in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_endpoint_slice", "patch_endpoint_slice"]

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
        Reads the EndpointSlice from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_endpoint_slice",
            "read_endpoint_slice",
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
        Deletes the EndpointSlice from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_endpoint_slice",
            "delete_endpoint_slice",
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
    ) -> "client.DiscoveryV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.DiscoveryV1beta1Api(**kwargs)

    def __enter__(self) -> "EndpointSlice":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EndpointSliceList(_kuber_definitions.Collection):
    """
    EndpointSliceList represents a list of endpoint slices
    """

    def __init__(
        self,
        items: typing.List["EndpointSlice"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create EndpointSliceList instance."""
        super(EndpointSliceList, self).__init__(
            api_version="discovery/v1beta1", kind="EndpointSliceList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, EndpointSlice),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["EndpointSlice"]:
        """
        List of endpoint slices
        """
        return typing.cast(
            typing.List["EndpointSlice"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["EndpointSlice"], typing.List[dict]]
    ):
        """
        List of endpoint slices
        """
        cleaned: typing.List[EndpointSlice] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    EndpointSlice,
                    EndpointSlice().from_dict(item),
                )
            cleaned.append(typing.cast(EndpointSlice, item))
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
    ) -> "client.DiscoveryV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.DiscoveryV1beta1Api(**kwargs)

    def __enter__(self) -> "EndpointSliceList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
