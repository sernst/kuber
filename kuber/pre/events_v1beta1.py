import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.pre.core_v1 import EventSource
from kuber.pre.meta_v1 import ListMeta
from kuber.pre.meta_v1 import MicroTime
from kuber.pre.meta_v1 import ObjectMeta
from kuber.pre.core_v1 import ObjectReference


class Event(_kuber_definitions.Resource):
    """
    Event is a report of an event somewhere in the cluster. It
    generally denotes some state change in the system. Events
    have a limited retention time and triggers and messages may
    evolve with time.  Event consumers should not rely on the
    timing of an event with a given Reason reflecting a
    consistent underlying trigger, or the continued existence of
    events with that Reason.  Events should be treated as
    informative, best-effort, supplemental data.
    """

    def __init__(
        self,
        action: str = None,
        deprecated_count: int = None,
        deprecated_first_timestamp: str = None,
        deprecated_last_timestamp: str = None,
        deprecated_source: "EventSource" = None,
        event_time: "MicroTime" = None,
        metadata: "ObjectMeta" = None,
        note: str = None,
        reason: str = None,
        regarding: "ObjectReference" = None,
        related: "ObjectReference" = None,
        reporting_controller: str = None,
        reporting_instance: str = None,
        series: "EventSeries" = None,
        type_: str = None,
    ):
        """Create Event instance."""
        super(Event, self).__init__(api_version="events/v1beta1", kind="Event")
        self._properties = {
            "action": action if action is not None else "",
            "deprecatedCount": deprecated_count
            if deprecated_count is not None
            else None,
            "deprecatedFirstTimestamp": deprecated_first_timestamp
            if deprecated_first_timestamp is not None
            else None,
            "deprecatedLastTimestamp": deprecated_last_timestamp
            if deprecated_last_timestamp is not None
            else None,
            "deprecatedSource": deprecated_source
            if deprecated_source is not None
            else EventSource(),
            "eventTime": event_time if event_time is not None else MicroTime(),
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "note": note if note is not None else "",
            "reason": reason if reason is not None else "",
            "regarding": regarding if regarding is not None else ObjectReference(),
            "related": related if related is not None else ObjectReference(),
            "reportingController": reporting_controller
            if reporting_controller is not None
            else "",
            "reportingInstance": reporting_instance
            if reporting_instance is not None
            else "",
            "series": series if series is not None else EventSeries(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "action": (str, None),
            "apiVersion": (str, None),
            "deprecatedCount": (int, None),
            "deprecatedFirstTimestamp": (str, None),
            "deprecatedLastTimestamp": (str, None),
            "deprecatedSource": (EventSource, None),
            "eventTime": (MicroTime, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "note": (str, None),
            "reason": (str, None),
            "regarding": (ObjectReference, None),
            "related": (ObjectReference, None),
            "reportingController": (str, None),
            "reportingInstance": (str, None),
            "series": (EventSeries, None),
            "type": (str, None),
        }

    @property
    def action(self) -> str:
        """
        action is what action was taken/failed regarding to the
        regarding object. It is machine-readable. This field can
        have at most 128 characters.
        """
        return typing.cast(
            str,
            self._properties.get("action"),
        )

    @action.setter
    def action(self, value: str):
        """
        action is what action was taken/failed regarding to the
        regarding object. It is machine-readable. This field can
        have at most 128 characters.
        """
        self._properties["action"] = value

    @property
    def deprecated_count(self) -> int:
        """
        deprecatedCount is the deprecated field assuring backward
        compatibility with core.v1 Event type.
        """
        return typing.cast(
            int,
            self._properties.get("deprecatedCount"),
        )

    @deprecated_count.setter
    def deprecated_count(self, value: int):
        """
        deprecatedCount is the deprecated field assuring backward
        compatibility with core.v1 Event type.
        """
        self._properties["deprecatedCount"] = value

    @property
    def deprecated_first_timestamp(self) -> str:
        """
        deprecatedFirstTimestamp is the deprecated field assuring
        backward compatibility with core.v1 Event type.
        """
        return typing.cast(
            str,
            self._properties.get("deprecatedFirstTimestamp"),
        )

    @deprecated_first_timestamp.setter
    def deprecated_first_timestamp(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        deprecatedFirstTimestamp is the deprecated field assuring
        backward compatibility with core.v1 Event type.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["deprecatedFirstTimestamp"] = value

    @property
    def deprecated_last_timestamp(self) -> str:
        """
        deprecatedLastTimestamp is the deprecated field assuring
        backward compatibility with core.v1 Event type.
        """
        return typing.cast(
            str,
            self._properties.get("deprecatedLastTimestamp"),
        )

    @deprecated_last_timestamp.setter
    def deprecated_last_timestamp(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        deprecatedLastTimestamp is the deprecated field assuring
        backward compatibility with core.v1 Event type.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["deprecatedLastTimestamp"] = value

    @property
    def deprecated_source(self) -> "EventSource":
        """
        deprecatedSource is the deprecated field assuring backward
        compatibility with core.v1 Event type.
        """
        return typing.cast(
            "EventSource",
            self._properties.get("deprecatedSource"),
        )

    @deprecated_source.setter
    def deprecated_source(self, value: typing.Union["EventSource", dict]):
        """
        deprecatedSource is the deprecated field assuring backward
        compatibility with core.v1 Event type.
        """
        if isinstance(value, dict):
            value = typing.cast(
                EventSource,
                EventSource().from_dict(value),
            )
        self._properties["deprecatedSource"] = value

    @property
    def event_time(self) -> "MicroTime":
        """
        eventTime is the time when this Event was first observed. It
        is required.
        """
        return typing.cast(
            "MicroTime",
            self._properties.get("eventTime"),
        )

    @event_time.setter
    def event_time(self, value: typing.Union["MicroTime", dict]):
        """
        eventTime is the time when this Event was first observed. It
        is required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MicroTime,
                MicroTime().from_dict(value),
            )
        self._properties["eventTime"] = value

    @property
    def metadata(self) -> "ObjectMeta":
        """"""
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def note(self) -> str:
        """
        note is a human-readable description of the status of this
        operation. Maximal length of the note is 1kB, but libraries
        should be prepared to handle values up to 64kB.
        """
        return typing.cast(
            str,
            self._properties.get("note"),
        )

    @note.setter
    def note(self, value: str):
        """
        note is a human-readable description of the status of this
        operation. Maximal length of the note is 1kB, but libraries
        should be prepared to handle values up to 64kB.
        """
        self._properties["note"] = value

    @property
    def reason(self) -> str:
        """
        reason is why the action was taken. It is human-readable.
        This field can have at most 128 characters.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        reason is why the action was taken. It is human-readable.
        This field can have at most 128 characters.
        """
        self._properties["reason"] = value

    @property
    def regarding(self) -> "ObjectReference":
        """
        regarding contains the object this Event is about. In most
        cases it's an Object reporting controller implements, e.g.
        ReplicaSetController implements ReplicaSets and this event
        is emitted because it acts on some changes in a ReplicaSet
        object.
        """
        return typing.cast(
            "ObjectReference",
            self._properties.get("regarding"),
        )

    @regarding.setter
    def regarding(self, value: typing.Union["ObjectReference", dict]):
        """
        regarding contains the object this Event is about. In most
        cases it's an Object reporting controller implements, e.g.
        ReplicaSetController implements ReplicaSets and this event
        is emitted because it acts on some changes in a ReplicaSet
        object.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectReference,
                ObjectReference().from_dict(value),
            )
        self._properties["regarding"] = value

    @property
    def related(self) -> "ObjectReference":
        """
        related is the optional secondary object for more complex
        actions. E.g. when regarding object triggers a creation or
        deletion of related object.
        """
        return typing.cast(
            "ObjectReference",
            self._properties.get("related"),
        )

    @related.setter
    def related(self, value: typing.Union["ObjectReference", dict]):
        """
        related is the optional secondary object for more complex
        actions. E.g. when regarding object triggers a creation or
        deletion of related object.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectReference,
                ObjectReference().from_dict(value),
            )
        self._properties["related"] = value

    @property
    def reporting_controller(self) -> str:
        """
        reportingController is the name of the controller that
        emitted this Event, e.g. `kubernetes.io/kubelet`. This field
        cannot be empty for new Events.
        """
        return typing.cast(
            str,
            self._properties.get("reportingController"),
        )

    @reporting_controller.setter
    def reporting_controller(self, value: str):
        """
        reportingController is the name of the controller that
        emitted this Event, e.g. `kubernetes.io/kubelet`. This field
        cannot be empty for new Events.
        """
        self._properties["reportingController"] = value

    @property
    def reporting_instance(self) -> str:
        """
        reportingInstance is the ID of the controller instance, e.g.
        `kubelet-xyzf`. This field cannot be empty for new Events
        and it can have at most 128 characters.
        """
        return typing.cast(
            str,
            self._properties.get("reportingInstance"),
        )

    @reporting_instance.setter
    def reporting_instance(self, value: str):
        """
        reportingInstance is the ID of the controller instance, e.g.
        `kubelet-xyzf`. This field cannot be empty for new Events
        and it can have at most 128 characters.
        """
        self._properties["reportingInstance"] = value

    @property
    def series(self) -> "EventSeries":
        """
        series is data about the Event series this event represents
        or nil if it's a singleton Event.
        """
        return typing.cast(
            "EventSeries",
            self._properties.get("series"),
        )

    @series.setter
    def series(self, value: typing.Union["EventSeries", dict]):
        """
        series is data about the Event series this event represents
        or nil if it's a singleton Event.
        """
        if isinstance(value, dict):
            value = typing.cast(
                EventSeries,
                EventSeries().from_dict(value),
            )
        self._properties["series"] = value

    @property
    def type_(self) -> str:
        """
        type is the type of this event (Normal, Warning), new types
        could be added in the future. It is machine-readable.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        type is the type of this event (Normal, Warning), new types
        could be added in the future. It is machine-readable.
        """
        self._properties["type"] = value

    def create_resource(self, namespace: "str" = None):
        """
        Creates the Event in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_event", "create_event"]

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
        Replaces the Event in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_event", "replace_event"]

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
        Patches the Event in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_event", "patch_event"]

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
        Reads the Event from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_event",
            "read_event",
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
        Deletes the Event from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_event",
            "delete_event",
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
    ) -> "client.EventsV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.EventsV1beta1Api(**kwargs)

    def __enter__(self) -> "Event":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EventList(_kuber_definitions.Collection):
    """
    EventList is a list of Event objects.
    """

    def __init__(
        self,
        items: typing.List["Event"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create EventList instance."""
        super(EventList, self).__init__(api_version="events/v1beta1", kind="EventList")
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, Event),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["Event"]:
        """
        items is a list of schema objects.
        """
        return typing.cast(
            typing.List["Event"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["Event"], typing.List[dict]]):
        """
        items is a list of schema objects.
        """
        cleaned: typing.List[Event] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Event,
                    Event().from_dict(item),
                )
            cleaned.append(typing.cast(Event, item))
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
    ) -> "client.EventsV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.EventsV1beta1Api(**kwargs)

    def __enter__(self) -> "EventList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class EventSeries(_kuber_definitions.Definition):
    """
    EventSeries contain information on series of events, i.e.
    thing that was/is happening continuously for some time.
    """

    def __init__(
        self,
        count: int = None,
        last_observed_time: "MicroTime" = None,
    ):
        """Create EventSeries instance."""
        super(EventSeries, self).__init__(
            api_version="events/v1beta1", kind="EventSeries"
        )
        self._properties = {
            "count": count if count is not None else None,
            "lastObservedTime": last_observed_time
            if last_observed_time is not None
            else MicroTime(),
        }
        self._types = {
            "count": (int, None),
            "lastObservedTime": (MicroTime, None),
        }

    @property
    def count(self) -> int:
        """
        count is the number of occurrences in this series up to the
        last heartbeat time.
        """
        return typing.cast(
            int,
            self._properties.get("count"),
        )

    @count.setter
    def count(self, value: int):
        """
        count is the number of occurrences in this series up to the
        last heartbeat time.
        """
        self._properties["count"] = value

    @property
    def last_observed_time(self) -> "MicroTime":
        """
        lastObservedTime is the time when last Event from the series
        was seen before last heartbeat.
        """
        return typing.cast(
            "MicroTime",
            self._properties.get("lastObservedTime"),
        )

    @last_observed_time.setter
    def last_observed_time(self, value: typing.Union["MicroTime", dict]):
        """
        lastObservedTime is the time when last Event from the series
        was seen before last heartbeat.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MicroTime,
                MicroTime().from_dict(value),
            )
        self._properties["lastObservedTime"] = value

    def __enter__(self) -> "EventSeries":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
