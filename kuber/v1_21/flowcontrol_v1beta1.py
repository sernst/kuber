import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_21.meta_v1 import ListMeta
from kuber.v1_21.meta_v1 import ObjectMeta
from kuber.v1_21.meta_v1 import Status
from kuber.v1_21.meta_v1 import StatusDetails


class FlowDistinguisherMethod(_kuber_definitions.Definition):
    """
    FlowDistinguisherMethod specifies the method of a flow
    distinguisher.
    """

    def __init__(
        self,
        type_: str = None,
    ):
        """Create FlowDistinguisherMethod instance."""
        super(FlowDistinguisherMethod, self).__init__(
            api_version="flowcontrol/v1beta1", kind="FlowDistinguisherMethod"
        )
        self._properties = {
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "type": (str, None),
        }

    @property
    def type_(self) -> str:
        """
        `type` is the type of flow distinguisher method The
        supported types are "ByUser" and "ByNamespace". Required.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        `type` is the type of flow distinguisher method The
        supported types are "ByUser" and "ByNamespace". Required.
        """
        self._properties["type"] = value

    def __enter__(self) -> "FlowDistinguisherMethod":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlowSchema(_kuber_definitions.Resource):
    """
    FlowSchema defines the schema of a group of flows. Note that
    a flow is made up of a set of inbound API requests with
    similar attributes and is identified by a pair of strings:
    the name of the FlowSchema and a "flow distinguisher".
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "FlowSchemaSpec" = None,
        status: "FlowSchemaStatus" = None,
    ):
        """Create FlowSchema instance."""
        super(FlowSchema, self).__init__(
            api_version="flowcontrol/v1beta1", kind="FlowSchema"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else FlowSchemaSpec(),
            "status": status if status is not None else FlowSchemaStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (FlowSchemaSpec, None),
            "status": (FlowSchemaStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        `metadata` is the standard object's metadata. More info:
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
        `metadata` is the standard object's metadata. More info:
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
    def spec(self) -> "FlowSchemaSpec":
        """
        `spec` is the specification of the desired behavior of a
        FlowSchema. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "FlowSchemaSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["FlowSchemaSpec", dict]):
        """
        `spec` is the specification of the desired behavior of a
        FlowSchema. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                FlowSchemaSpec,
                FlowSchemaSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "FlowSchemaStatus":
        """
        `status` is the current status of a FlowSchema. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "FlowSchemaStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["FlowSchemaStatus", dict]):
        """
        `status` is the current status of a FlowSchema. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                FlowSchemaStatus,
                FlowSchemaStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(self, namespace: "str" = None) -> "FlowSchemaStatus":
        """
        Creates the FlowSchema in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_flow_schema", "create_flow_schema"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = FlowSchemaStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "FlowSchemaStatus":
        """
        Replaces the FlowSchema in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_flow_schema", "replace_flow_schema"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = FlowSchemaStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "FlowSchemaStatus":
        """
        Patches the FlowSchema in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_flow_schema", "patch_flow_schema"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = FlowSchemaStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "FlowSchemaStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_flow_schema", "read_flow_schema"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = FlowSchemaStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the FlowSchema from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_flow_schema",
            "read_flow_schema",
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
        Deletes the FlowSchema from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_flow_schema",
            "delete_flow_schema",
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
    ) -> "client.FlowcontrolV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.FlowcontrolV1beta1Api(**kwargs)

    def __enter__(self) -> "FlowSchema":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlowSchemaCondition(_kuber_definitions.Definition):
    """
    FlowSchemaCondition describes conditions for a FlowSchema.
    """

    def __init__(
        self,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create FlowSchemaCondition instance."""
        super(FlowSchemaCondition, self).__init__(
            api_version="flowcontrol/v1beta1", kind="FlowSchemaCondition"
        )
        self._properties = {
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastTransitionTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def last_transition_time(self) -> str:
        """
        `lastTransitionTime` is the last time the condition
        transitioned from one status to another.
        """
        return typing.cast(
            str,
            self._properties.get("lastTransitionTime"),
        )

    @last_transition_time.setter
    def last_transition_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        `lastTransitionTime` is the last time the condition
        transitioned from one status to another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        `message` is a human-readable message indicating details
        about last transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        `message` is a human-readable message indicating details
        about last transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        `reason` is a unique, one-word, CamelCase reason for the
        condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        `reason` is a unique, one-word, CamelCase reason for the
        condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        `status` is the status of the condition. Can be True, False,
        Unknown. Required.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        `status` is the status of the condition. Can be True, False,
        Unknown. Required.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        `type` is the type of the condition. Required.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        `type` is the type of the condition. Required.
        """
        self._properties["type"] = value

    def __enter__(self) -> "FlowSchemaCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlowSchemaList(_kuber_definitions.Collection):
    """
    FlowSchemaList is a list of FlowSchema objects.
    """

    def __init__(
        self,
        items: typing.List["FlowSchema"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create FlowSchemaList instance."""
        super(FlowSchemaList, self).__init__(
            api_version="flowcontrol/v1beta1", kind="FlowSchemaList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, FlowSchema),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["FlowSchema"]:
        """
        `items` is a list of FlowSchemas.
        """
        return typing.cast(
            typing.List["FlowSchema"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["FlowSchema"], typing.List[dict]]):
        """
        `items` is a list of FlowSchemas.
        """
        cleaned: typing.List[FlowSchema] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    FlowSchema,
                    FlowSchema().from_dict(item),
                )
            cleaned.append(typing.cast(FlowSchema, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        `metadata` is the standard list metadata. More info:
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
        `metadata` is the standard list metadata. More info:
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
    ) -> "client.FlowcontrolV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.FlowcontrolV1beta1Api(**kwargs)

    def __enter__(self) -> "FlowSchemaList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlowSchemaSpec(_kuber_definitions.Definition):
    """
    FlowSchemaSpec describes how the FlowSchema's specification
    looks like.
    """

    def __init__(
        self,
        distinguisher_method: "FlowDistinguisherMethod" = None,
        matching_precedence: int = None,
        priority_level_configuration: "PriorityLevelConfigurationReference" = None,
        rules: typing.List["PolicyRulesWithSubjects"] = None,
    ):
        """Create FlowSchemaSpec instance."""
        super(FlowSchemaSpec, self).__init__(
            api_version="flowcontrol/v1beta1", kind="FlowSchemaSpec"
        )
        self._properties = {
            "distinguisherMethod": distinguisher_method
            if distinguisher_method is not None
            else FlowDistinguisherMethod(),
            "matchingPrecedence": matching_precedence
            if matching_precedence is not None
            else None,
            "priorityLevelConfiguration": priority_level_configuration
            if priority_level_configuration is not None
            else PriorityLevelConfigurationReference(),
            "rules": rules if rules is not None else [],
        }
        self._types = {
            "distinguisherMethod": (FlowDistinguisherMethod, None),
            "matchingPrecedence": (int, None),
            "priorityLevelConfiguration": (PriorityLevelConfigurationReference, None),
            "rules": (list, PolicyRulesWithSubjects),
        }

    @property
    def distinguisher_method(self) -> "FlowDistinguisherMethod":
        """
        `distinguisherMethod` defines how to compute the flow
        distinguisher for requests that match this schema. `nil`
        specifies that the distinguisher is disabled and thus will
        always be the empty string.
        """
        return typing.cast(
            "FlowDistinguisherMethod",
            self._properties.get("distinguisherMethod"),
        )

    @distinguisher_method.setter
    def distinguisher_method(
        self, value: typing.Union["FlowDistinguisherMethod", dict]
    ):
        """
        `distinguisherMethod` defines how to compute the flow
        distinguisher for requests that match this schema. `nil`
        specifies that the distinguisher is disabled and thus will
        always be the empty string.
        """
        if isinstance(value, dict):
            value = typing.cast(
                FlowDistinguisherMethod,
                FlowDistinguisherMethod().from_dict(value),
            )
        self._properties["distinguisherMethod"] = value

    @property
    def matching_precedence(self) -> int:
        """
        `matchingPrecedence` is used to choose among the FlowSchemas
        that match a given request. The chosen FlowSchema is among
        those with the numerically lowest (which we take to be
        logically highest) MatchingPrecedence.  Each
        MatchingPrecedence value must be ranged in [1,10000]. Note
        that if the precedence is not specified, it will be set to
        1000 as default.
        """
        return typing.cast(
            int,
            self._properties.get("matchingPrecedence"),
        )

    @matching_precedence.setter
    def matching_precedence(self, value: int):
        """
        `matchingPrecedence` is used to choose among the FlowSchemas
        that match a given request. The chosen FlowSchema is among
        those with the numerically lowest (which we take to be
        logically highest) MatchingPrecedence.  Each
        MatchingPrecedence value must be ranged in [1,10000]. Note
        that if the precedence is not specified, it will be set to
        1000 as default.
        """
        self._properties["matchingPrecedence"] = value

    @property
    def priority_level_configuration(self) -> "PriorityLevelConfigurationReference":
        """
        `priorityLevelConfiguration` should reference a
        PriorityLevelConfiguration in the cluster. If the reference
        cannot be resolved, the FlowSchema will be ignored and
        marked as invalid in its status. Required.
        """
        return typing.cast(
            "PriorityLevelConfigurationReference",
            self._properties.get("priorityLevelConfiguration"),
        )

    @priority_level_configuration.setter
    def priority_level_configuration(
        self, value: typing.Union["PriorityLevelConfigurationReference", dict]
    ):
        """
        `priorityLevelConfiguration` should reference a
        PriorityLevelConfiguration in the cluster. If the reference
        cannot be resolved, the FlowSchema will be ignored and
        marked as invalid in its status. Required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PriorityLevelConfigurationReference,
                PriorityLevelConfigurationReference().from_dict(value),
            )
        self._properties["priorityLevelConfiguration"] = value

    @property
    def rules(self) -> typing.List["PolicyRulesWithSubjects"]:
        """
        `rules` describes which requests will match this flow
        schema. This FlowSchema matches a request if and only if at
        least one member of rules matches the request. if it is an
        empty slice, there will be no requests matching the
        FlowSchema.
        """
        return typing.cast(
            typing.List["PolicyRulesWithSubjects"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(
        self,
        value: typing.Union[typing.List["PolicyRulesWithSubjects"], typing.List[dict]],
    ):
        """
        `rules` describes which requests will match this flow
        schema. This FlowSchema matches a request if and only if at
        least one member of rules matches the request. if it is an
        empty slice, there will be no requests matching the
        FlowSchema.
        """
        cleaned: typing.List[PolicyRulesWithSubjects] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PolicyRulesWithSubjects,
                    PolicyRulesWithSubjects().from_dict(item),
                )
            cleaned.append(typing.cast(PolicyRulesWithSubjects, item))
        self._properties["rules"] = cleaned

    def __enter__(self) -> "FlowSchemaSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class FlowSchemaStatus(_kuber_definitions.Definition):
    """
    FlowSchemaStatus represents the current state of a
    FlowSchema.
    """

    def __init__(
        self,
        conditions: typing.List["FlowSchemaCondition"] = None,
    ):
        """Create FlowSchemaStatus instance."""
        super(FlowSchemaStatus, self).__init__(
            api_version="flowcontrol/v1beta1", kind="FlowSchemaStatus"
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
        }
        self._types = {
            "conditions": (list, FlowSchemaCondition),
        }

    @property
    def conditions(self) -> typing.List["FlowSchemaCondition"]:
        """
        `conditions` is a list of the current states of FlowSchema.
        """
        return typing.cast(
            typing.List["FlowSchemaCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["FlowSchemaCondition"], typing.List[dict]]
    ):
        """
        `conditions` is a list of the current states of FlowSchema.
        """
        cleaned: typing.List[FlowSchemaCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    FlowSchemaCondition,
                    FlowSchemaCondition().from_dict(item),
                )
            cleaned.append(typing.cast(FlowSchemaCondition, item))
        self._properties["conditions"] = cleaned

    def __enter__(self) -> "FlowSchemaStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class GroupSubject(_kuber_definitions.Definition):
    """
    GroupSubject holds detailed information for group-kind
    subject.
    """

    def __init__(
        self,
        name: str = None,
    ):
        """Create GroupSubject instance."""
        super(GroupSubject, self).__init__(
            api_version="flowcontrol/v1beta1", kind="GroupSubject"
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
        name is the user group that matches, or "*" to match all
        user groups. See https://github.com/kubernetes/apiserver/blo
        b/master/pkg/authentication/user/user.go for some well-known
        group names. Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the user group that matches, or "*" to match all
        user groups. See https://github.com/kubernetes/apiserver/blo
        b/master/pkg/authentication/user/user.go for some well-known
        group names. Required.
        """
        self._properties["name"] = value

    def __enter__(self) -> "GroupSubject":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LimitResponse(_kuber_definitions.Definition):
    """
    LimitResponse defines how to handle requests that can not be
    executed right now.
    """

    def __init__(
        self,
        queuing: "QueuingConfiguration" = None,
        type_: str = None,
    ):
        """Create LimitResponse instance."""
        super(LimitResponse, self).__init__(
            api_version="flowcontrol/v1beta1", kind="LimitResponse"
        )
        self._properties = {
            "queuing": queuing if queuing is not None else QueuingConfiguration(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "queuing": (QueuingConfiguration, None),
            "type": (str, None),
        }

    @property
    def queuing(self) -> "QueuingConfiguration":
        """
        `queuing` holds the configuration parameters for queuing.
        This field may be non-empty only if `type` is `"Queue"`.
        """
        return typing.cast(
            "QueuingConfiguration",
            self._properties.get("queuing"),
        )

    @queuing.setter
    def queuing(self, value: typing.Union["QueuingConfiguration", dict]):
        """
        `queuing` holds the configuration parameters for queuing.
        This field may be non-empty only if `type` is `"Queue"`.
        """
        if isinstance(value, dict):
            value = typing.cast(
                QueuingConfiguration,
                QueuingConfiguration().from_dict(value),
            )
        self._properties["queuing"] = value

    @property
    def type_(self) -> str:
        """
        `type` is "Queue" or "Reject". "Queue" means that requests
        that can not be executed upon arrival are held in a queue
        until they can be executed or a queuing limit is reached.
        "Reject" means that requests that can not be executed upon
        arrival are rejected. Required.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        `type` is "Queue" or "Reject". "Queue" means that requests
        that can not be executed upon arrival are held in a queue
        until they can be executed or a queuing limit is reached.
        "Reject" means that requests that can not be executed upon
        arrival are rejected. Required.
        """
        self._properties["type"] = value

    def __enter__(self) -> "LimitResponse":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class LimitedPriorityLevelConfiguration(_kuber_definitions.Definition):
    """
    LimitedPriorityLevelConfiguration specifies how to handle
    requests that are subject to limits. It addresses two
    issues:
     * How are requests for this priority level limited?
     * What should be done with requests that exceed the limit?
    """

    def __init__(
        self,
        assured_concurrency_shares: int = None,
        limit_response: "LimitResponse" = None,
    ):
        """Create LimitedPriorityLevelConfiguration instance."""
        super(LimitedPriorityLevelConfiguration, self).__init__(
            api_version="flowcontrol/v1beta1", kind="LimitedPriorityLevelConfiguration"
        )
        self._properties = {
            "assuredConcurrencyShares": assured_concurrency_shares
            if assured_concurrency_shares is not None
            else None,
            "limitResponse": limit_response
            if limit_response is not None
            else LimitResponse(),
        }
        self._types = {
            "assuredConcurrencyShares": (int, None),
            "limitResponse": (LimitResponse, None),
        }

    @property
    def assured_concurrency_shares(self) -> int:
        """
        `assuredConcurrencyShares` (ACS) configures the execution
        limit, which is a limit on the number of requests of this
        priority level that may be exeucting at a given time.  ACS
        must be a positive number. The server's concurrency limit
        (SCL) is divided among the concurrency-controlled priority
        levels in proportion to their assured concurrency shares.
        This produces the assured concurrency value (ACV) --- the
        number of requests that may be executing at a time --- for
        each such priority level:

                    ACV(l) = ceil( SCL * ACS(l) / ( sum[priority
        levels k] ACS(k) ) )

        bigger numbers of ACS mean more reserved concurrent requests
        (at the expense of every other PL). This field has a default
        value of 30.
        """
        return typing.cast(
            int,
            self._properties.get("assuredConcurrencyShares"),
        )

    @assured_concurrency_shares.setter
    def assured_concurrency_shares(self, value: int):
        """
        `assuredConcurrencyShares` (ACS) configures the execution
        limit, which is a limit on the number of requests of this
        priority level that may be exeucting at a given time.  ACS
        must be a positive number. The server's concurrency limit
        (SCL) is divided among the concurrency-controlled priority
        levels in proportion to their assured concurrency shares.
        This produces the assured concurrency value (ACV) --- the
        number of requests that may be executing at a time --- for
        each such priority level:

                    ACV(l) = ceil( SCL * ACS(l) / ( sum[priority
        levels k] ACS(k) ) )

        bigger numbers of ACS mean more reserved concurrent requests
        (at the expense of every other PL). This field has a default
        value of 30.
        """
        self._properties["assuredConcurrencyShares"] = value

    @property
    def limit_response(self) -> "LimitResponse":
        """
        `limitResponse` indicates what to do with requests that can
        not be executed right now
        """
        return typing.cast(
            "LimitResponse",
            self._properties.get("limitResponse"),
        )

    @limit_response.setter
    def limit_response(self, value: typing.Union["LimitResponse", dict]):
        """
        `limitResponse` indicates what to do with requests that can
        not be executed right now
        """
        if isinstance(value, dict):
            value = typing.cast(
                LimitResponse,
                LimitResponse().from_dict(value),
            )
        self._properties["limitResponse"] = value

    def __enter__(self) -> "LimitedPriorityLevelConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NonResourcePolicyRule(_kuber_definitions.Definition):
    """
    NonResourcePolicyRule is a predicate that matches non-
    resource requests according to their verb and the target
    non-resource URL. A NonResourcePolicyRule matches a request
    if and only if both (a) at least one member of verbs matches
    the request and (b) at least one member of nonResourceURLs
    matches the request.
    """

    def __init__(
        self,
        non_resource_urls: typing.List[str] = None,
        verbs: typing.List[str] = None,
    ):
        """Create NonResourcePolicyRule instance."""
        super(NonResourcePolicyRule, self).__init__(
            api_version="flowcontrol/v1beta1", kind="NonResourcePolicyRule"
        )
        self._properties = {
            "nonResourceURLs": non_resource_urls
            if non_resource_urls is not None
            else [],
            "verbs": verbs if verbs is not None else [],
        }
        self._types = {
            "nonResourceURLs": (list, str),
            "verbs": (list, str),
        }

    @property
    def non_resource_urls(self) -> typing.List[str]:
        """
        `nonResourceURLs` is a set of url prefixes that a user
        should have access to and may not be empty. For example:
          - "/healthz" is legal
          - "/hea*" is illegal
          - "/hea" is legal but matches nothing
          - "/hea/*" also matches nothing
          - "/healthz/*" matches all per-component health checks.
        "*" matches all non-resource urls. if it is present, it must
        be the only entry. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("nonResourceURLs"),
        )

    @non_resource_urls.setter
    def non_resource_urls(self, value: typing.List[str]):
        """
        `nonResourceURLs` is a set of url prefixes that a user
        should have access to and may not be empty. For example:
          - "/healthz" is legal
          - "/hea*" is illegal
          - "/hea" is legal but matches nothing
          - "/hea/*" also matches nothing
          - "/healthz/*" matches all per-component health checks.
        "*" matches all non-resource urls. if it is present, it must
        be the only entry. Required.
        """
        self._properties["nonResourceURLs"] = value

    @property
    def verbs(self) -> typing.List[str]:
        """
        `verbs` is a list of matching verbs and may not be empty.
        "*" matches all verbs. If it is present, it must be the only
        entry. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("verbs"),
        )

    @verbs.setter
    def verbs(self, value: typing.List[str]):
        """
        `verbs` is a list of matching verbs and may not be empty.
        "*" matches all verbs. If it is present, it must be the only
        entry. Required.
        """
        self._properties["verbs"] = value

    def __enter__(self) -> "NonResourcePolicyRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PolicyRulesWithSubjects(_kuber_definitions.Definition):
    """
    PolicyRulesWithSubjects prescribes a test that applies to a
    request to an apiserver. The test considers the subject
    making the request, the verb being requested, and the
    resource to be acted upon. This PolicyRulesWithSubjects
    matches a request if and only if both (a) at least one
    member of subjects matches the request and (b) at least one
    member of resourceRules or nonResourceRules matches the
    request.
    """

    def __init__(
        self,
        non_resource_rules: typing.List["NonResourcePolicyRule"] = None,
        resource_rules: typing.List["ResourcePolicyRule"] = None,
        subjects: typing.List["Subject"] = None,
    ):
        """Create PolicyRulesWithSubjects instance."""
        super(PolicyRulesWithSubjects, self).__init__(
            api_version="flowcontrol/v1beta1", kind="PolicyRulesWithSubjects"
        )
        self._properties = {
            "nonResourceRules": non_resource_rules
            if non_resource_rules is not None
            else [],
            "resourceRules": resource_rules if resource_rules is not None else [],
            "subjects": subjects if subjects is not None else [],
        }
        self._types = {
            "nonResourceRules": (list, NonResourcePolicyRule),
            "resourceRules": (list, ResourcePolicyRule),
            "subjects": (list, Subject),
        }

    @property
    def non_resource_rules(self) -> typing.List["NonResourcePolicyRule"]:
        """
        `nonResourceRules` is a list of NonResourcePolicyRules that
        identify matching requests according to their verb and the
        target non-resource URL.
        """
        return typing.cast(
            typing.List["NonResourcePolicyRule"],
            self._properties.get("nonResourceRules"),
        )

    @non_resource_rules.setter
    def non_resource_rules(
        self,
        value: typing.Union[typing.List["NonResourcePolicyRule"], typing.List[dict]],
    ):
        """
        `nonResourceRules` is a list of NonResourcePolicyRules that
        identify matching requests according to their verb and the
        target non-resource URL.
        """
        cleaned: typing.List[NonResourcePolicyRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NonResourcePolicyRule,
                    NonResourcePolicyRule().from_dict(item),
                )
            cleaned.append(typing.cast(NonResourcePolicyRule, item))
        self._properties["nonResourceRules"] = cleaned

    @property
    def resource_rules(self) -> typing.List["ResourcePolicyRule"]:
        """
        `resourceRules` is a slice of ResourcePolicyRules that
        identify matching requests according to their verb and the
        target resource. At least one of `resourceRules` and
        `nonResourceRules` has to be non-empty.
        """
        return typing.cast(
            typing.List["ResourcePolicyRule"],
            self._properties.get("resourceRules"),
        )

    @resource_rules.setter
    def resource_rules(
        self, value: typing.Union[typing.List["ResourcePolicyRule"], typing.List[dict]]
    ):
        """
        `resourceRules` is a slice of ResourcePolicyRules that
        identify matching requests according to their verb and the
        target resource. At least one of `resourceRules` and
        `nonResourceRules` has to be non-empty.
        """
        cleaned: typing.List[ResourcePolicyRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ResourcePolicyRule,
                    ResourcePolicyRule().from_dict(item),
                )
            cleaned.append(typing.cast(ResourcePolicyRule, item))
        self._properties["resourceRules"] = cleaned

    @property
    def subjects(self) -> typing.List["Subject"]:
        """
        subjects is the list of normal user, serviceaccount, or
        group that this rule cares about. There must be at least one
        member in this slice. A slice that includes both the
        system:authenticated and system:unauthenticated user groups
        matches every request. Required.
        """
        return typing.cast(
            typing.List["Subject"],
            self._properties.get("subjects"),
        )

    @subjects.setter
    def subjects(self, value: typing.Union[typing.List["Subject"], typing.List[dict]]):
        """
        subjects is the list of normal user, serviceaccount, or
        group that this rule cares about. There must be at least one
        member in this slice. A slice that includes both the
        system:authenticated and system:unauthenticated user groups
        matches every request. Required.
        """
        cleaned: typing.List[Subject] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Subject,
                    Subject().from_dict(item),
                )
            cleaned.append(typing.cast(Subject, item))
        self._properties["subjects"] = cleaned

    def __enter__(self) -> "PolicyRulesWithSubjects":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityLevelConfiguration(_kuber_definitions.Resource):
    """
    PriorityLevelConfiguration represents the configuration of a
    priority level.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "PriorityLevelConfigurationSpec" = None,
        status: "PriorityLevelConfigurationStatus" = None,
    ):
        """Create PriorityLevelConfiguration instance."""
        super(PriorityLevelConfiguration, self).__init__(
            api_version="flowcontrol/v1beta1", kind="PriorityLevelConfiguration"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else PriorityLevelConfigurationSpec(),
            "status": status
            if status is not None
            else PriorityLevelConfigurationStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (PriorityLevelConfigurationSpec, None),
            "status": (PriorityLevelConfigurationStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        `metadata` is the standard object's metadata. More info:
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
        `metadata` is the standard object's metadata. More info:
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
    def spec(self) -> "PriorityLevelConfigurationSpec":
        """
        `spec` is the specification of the desired behavior of a
        "request-priority". More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "PriorityLevelConfigurationSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["PriorityLevelConfigurationSpec", dict]):
        """
        `spec` is the specification of the desired behavior of a
        "request-priority". More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                PriorityLevelConfigurationSpec,
                PriorityLevelConfigurationSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "PriorityLevelConfigurationStatus":
        """
        `status` is the current status of a "request-priority". More
        info: https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "PriorityLevelConfigurationStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["PriorityLevelConfigurationStatus", dict]):
        """
        `status` is the current status of a "request-priority". More
        info: https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                PriorityLevelConfigurationStatus,
                PriorityLevelConfigurationStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: "str" = None
    ) -> "PriorityLevelConfigurationStatus":
        """
        Creates the PriorityLevelConfiguration in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_priority_level_configuration",
            "create_priority_level_configuration",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = PriorityLevelConfigurationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: "str" = None
    ) -> "PriorityLevelConfigurationStatus":
        """
        Replaces the PriorityLevelConfiguration in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_priority_level_configuration",
            "replace_priority_level_configuration",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PriorityLevelConfigurationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: "str" = None
    ) -> "PriorityLevelConfigurationStatus":
        """
        Patches the PriorityLevelConfiguration in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_priority_level_configuration",
            "patch_priority_level_configuration",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = PriorityLevelConfigurationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: "str" = None
    ) -> "PriorityLevelConfigurationStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_priority_level_configuration",
            "read_priority_level_configuration",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = PriorityLevelConfigurationStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the PriorityLevelConfiguration from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_priority_level_configuration",
            "read_priority_level_configuration",
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
        Deletes the PriorityLevelConfiguration from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_priority_level_configuration",
            "delete_priority_level_configuration",
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
    ) -> "client.FlowcontrolV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.FlowcontrolV1beta1Api(**kwargs)

    def __enter__(self) -> "PriorityLevelConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityLevelConfigurationCondition(_kuber_definitions.Definition):
    """
    PriorityLevelConfigurationCondition defines the condition of
    priority level.
    """

    def __init__(
        self,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create PriorityLevelConfigurationCondition instance."""
        super(PriorityLevelConfigurationCondition, self).__init__(
            api_version="flowcontrol/v1beta1",
            kind="PriorityLevelConfigurationCondition",
        )
        self._properties = {
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastTransitionTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def last_transition_time(self) -> str:
        """
        `lastTransitionTime` is the last time the condition
        transitioned from one status to another.
        """
        return typing.cast(
            str,
            self._properties.get("lastTransitionTime"),
        )

    @last_transition_time.setter
    def last_transition_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        `lastTransitionTime` is the last time the condition
        transitioned from one status to another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        `message` is a human-readable message indicating details
        about last transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        `message` is a human-readable message indicating details
        about last transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        `reason` is a unique, one-word, CamelCase reason for the
        condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        `reason` is a unique, one-word, CamelCase reason for the
        condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        `status` is the status of the condition. Can be True, False,
        Unknown. Required.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        `status` is the status of the condition. Can be True, False,
        Unknown. Required.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        `type` is the type of the condition. Required.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        `type` is the type of the condition. Required.
        """
        self._properties["type"] = value

    def __enter__(self) -> "PriorityLevelConfigurationCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityLevelConfigurationList(_kuber_definitions.Collection):
    """
    PriorityLevelConfigurationList is a list of
    PriorityLevelConfiguration objects.
    """

    def __init__(
        self,
        items: typing.List["PriorityLevelConfiguration"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create PriorityLevelConfigurationList instance."""
        super(PriorityLevelConfigurationList, self).__init__(
            api_version="flowcontrol/v1beta1", kind="PriorityLevelConfigurationList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, PriorityLevelConfiguration),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["PriorityLevelConfiguration"]:
        """
        `items` is a list of request-priorities.
        """
        return typing.cast(
            typing.List["PriorityLevelConfiguration"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["PriorityLevelConfiguration"], typing.List[dict]
        ],
    ):
        """
        `items` is a list of request-priorities.
        """
        cleaned: typing.List[PriorityLevelConfiguration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PriorityLevelConfiguration,
                    PriorityLevelConfiguration().from_dict(item),
                )
            cleaned.append(typing.cast(PriorityLevelConfiguration, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        `metadata` is the standard object's metadata. More info:
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
        `metadata` is the standard object's metadata. More info:
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
    ) -> "client.FlowcontrolV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.FlowcontrolV1beta1Api(**kwargs)

    def __enter__(self) -> "PriorityLevelConfigurationList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityLevelConfigurationReference(_kuber_definitions.Definition):
    """
    PriorityLevelConfigurationReference contains information
    that points to the "request-priority" being used.
    """

    def __init__(
        self,
        name: str = None,
    ):
        """Create PriorityLevelConfigurationReference instance."""
        super(PriorityLevelConfigurationReference, self).__init__(
            api_version="flowcontrol/v1beta1",
            kind="PriorityLevelConfigurationReference",
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
        `name` is the name of the priority level configuration being
        referenced Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        `name` is the name of the priority level configuration being
        referenced Required.
        """
        self._properties["name"] = value

    def __enter__(self) -> "PriorityLevelConfigurationReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityLevelConfigurationSpec(_kuber_definitions.Definition):
    """
    PriorityLevelConfigurationSpec specifies the configuration
    of a priority level.
    """

    def __init__(
        self,
        limited: "LimitedPriorityLevelConfiguration" = None,
        type_: str = None,
    ):
        """Create PriorityLevelConfigurationSpec instance."""
        super(PriorityLevelConfigurationSpec, self).__init__(
            api_version="flowcontrol/v1beta1", kind="PriorityLevelConfigurationSpec"
        )
        self._properties = {
            "limited": limited
            if limited is not None
            else LimitedPriorityLevelConfiguration(),
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "limited": (LimitedPriorityLevelConfiguration, None),
            "type": (str, None),
        }

    @property
    def limited(self) -> "LimitedPriorityLevelConfiguration":
        """
        `limited` specifies how requests are handled for a Limited
        priority level. This field must be non-empty if and only if
        `type` is `"Limited"`.
        """
        return typing.cast(
            "LimitedPriorityLevelConfiguration",
            self._properties.get("limited"),
        )

    @limited.setter
    def limited(self, value: typing.Union["LimitedPriorityLevelConfiguration", dict]):
        """
        `limited` specifies how requests are handled for a Limited
        priority level. This field must be non-empty if and only if
        `type` is `"Limited"`.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LimitedPriorityLevelConfiguration,
                LimitedPriorityLevelConfiguration().from_dict(value),
            )
        self._properties["limited"] = value

    @property
    def type_(self) -> str:
        """
        `type` indicates whether this priority level is subject to
        limitation on request execution.  A value of `"Exempt"`
        means that requests of this priority level are not subject
        to a limit (and thus are never queued) and do not detract
        from the capacity made available to other priority levels.
        A value of `"Limited"` means that (a) requests of this
        priority level _are_ subject to limits and (b) some of the
        server's limited capacity is made available exclusively to
        this priority level. Required.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        `type` indicates whether this priority level is subject to
        limitation on request execution.  A value of `"Exempt"`
        means that requests of this priority level are not subject
        to a limit (and thus are never queued) and do not detract
        from the capacity made available to other priority levels.
        A value of `"Limited"` means that (a) requests of this
        priority level _are_ subject to limits and (b) some of the
        server's limited capacity is made available exclusively to
        this priority level. Required.
        """
        self._properties["type"] = value

    def __enter__(self) -> "PriorityLevelConfigurationSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PriorityLevelConfigurationStatus(_kuber_definitions.Definition):
    """
    PriorityLevelConfigurationStatus represents the current
    state of a "request-priority".
    """

    def __init__(
        self,
        conditions: typing.List["PriorityLevelConfigurationCondition"] = None,
    ):
        """Create PriorityLevelConfigurationStatus instance."""
        super(PriorityLevelConfigurationStatus, self).__init__(
            api_version="flowcontrol/v1beta1", kind="PriorityLevelConfigurationStatus"
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
        }
        self._types = {
            "conditions": (list, PriorityLevelConfigurationCondition),
        }

    @property
    def conditions(self) -> typing.List["PriorityLevelConfigurationCondition"]:
        """
        `conditions` is the current state of "request-priority".
        """
        return typing.cast(
            typing.List["PriorityLevelConfigurationCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self,
        value: typing.Union[
            typing.List["PriorityLevelConfigurationCondition"], typing.List[dict]
        ],
    ):
        """
        `conditions` is the current state of "request-priority".
        """
        cleaned: typing.List[PriorityLevelConfigurationCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PriorityLevelConfigurationCondition,
                    PriorityLevelConfigurationCondition().from_dict(item),
                )
            cleaned.append(typing.cast(PriorityLevelConfigurationCondition, item))
        self._properties["conditions"] = cleaned

    def __enter__(self) -> "PriorityLevelConfigurationStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class QueuingConfiguration(_kuber_definitions.Definition):
    """
    QueuingConfiguration holds the configuration parameters for
    queuing
    """

    def __init__(
        self,
        hand_size: int = None,
        queue_length_limit: int = None,
        queues: int = None,
    ):
        """Create QueuingConfiguration instance."""
        super(QueuingConfiguration, self).__init__(
            api_version="flowcontrol/v1beta1", kind="QueuingConfiguration"
        )
        self._properties = {
            "handSize": hand_size if hand_size is not None else None,
            "queueLengthLimit": queue_length_limit
            if queue_length_limit is not None
            else None,
            "queues": queues if queues is not None else None,
        }
        self._types = {
            "handSize": (int, None),
            "queueLengthLimit": (int, None),
            "queues": (int, None),
        }

    @property
    def hand_size(self) -> int:
        """
        `handSize` is a small positive number that configures the
        shuffle sharding of requests into queues.  When enqueuing a
        request at this priority level the request's flow identifier
        (a string pair) is hashed and the hash value is used to
        shuffle the list of queues and deal a hand of the size
        specified here.  The request is put into one of the shortest
        queues in that hand. `handSize` must be no larger than
        `queues`, and should be significantly smaller (so that a few
        heavy flows do not saturate most of the queues).  See the
        user-facing documentation for more extensive guidance on
        setting this field.  This field has a default value of 8.
        """
        return typing.cast(
            int,
            self._properties.get("handSize"),
        )

    @hand_size.setter
    def hand_size(self, value: int):
        """
        `handSize` is a small positive number that configures the
        shuffle sharding of requests into queues.  When enqueuing a
        request at this priority level the request's flow identifier
        (a string pair) is hashed and the hash value is used to
        shuffle the list of queues and deal a hand of the size
        specified here.  The request is put into one of the shortest
        queues in that hand. `handSize` must be no larger than
        `queues`, and should be significantly smaller (so that a few
        heavy flows do not saturate most of the queues).  See the
        user-facing documentation for more extensive guidance on
        setting this field.  This field has a default value of 8.
        """
        self._properties["handSize"] = value

    @property
    def queue_length_limit(self) -> int:
        """
        `queueLengthLimit` is the maximum number of requests allowed
        to be waiting in a given queue of this priority level at a
        time; excess requests are rejected.  This value must be
        positive.  If not specified, it will be defaulted to 50.
        """
        return typing.cast(
            int,
            self._properties.get("queueLengthLimit"),
        )

    @queue_length_limit.setter
    def queue_length_limit(self, value: int):
        """
        `queueLengthLimit` is the maximum number of requests allowed
        to be waiting in a given queue of this priority level at a
        time; excess requests are rejected.  This value must be
        positive.  If not specified, it will be defaulted to 50.
        """
        self._properties["queueLengthLimit"] = value

    @property
    def queues(self) -> int:
        """
        `queues` is the number of queues for this priority level.
        The queues exist independently at each apiserver. The value
        must be positive.  Setting it to 1 effectively precludes
        shufflesharding and thus makes the distinguisher method of
        associated flow schemas irrelevant.  This field has a
        default value of 64.
        """
        return typing.cast(
            int,
            self._properties.get("queues"),
        )

    @queues.setter
    def queues(self, value: int):
        """
        `queues` is the number of queues for this priority level.
        The queues exist independently at each apiserver. The value
        must be positive.  Setting it to 1 effectively precludes
        shufflesharding and thus makes the distinguisher method of
        associated flow schemas irrelevant.  This field has a
        default value of 64.
        """
        self._properties["queues"] = value

    def __enter__(self) -> "QueuingConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourcePolicyRule(_kuber_definitions.Definition):
    """
    ResourcePolicyRule is a predicate that matches some resource
    requests, testing the request's verb and the target
    resource. A ResourcePolicyRule matches a resource request if
    and only if: (a) at least one member of verbs matches the
    request, (b) at least one member of apiGroups matches the
    request, (c) at least one member of resources matches the
    request, and (d) least one member of namespaces matches the
    request.
    """

    def __init__(
        self,
        api_groups: typing.List[str] = None,
        cluster_scope: bool = None,
        namespaces: typing.List[str] = None,
        resources: typing.List[str] = None,
        verbs: typing.List[str] = None,
    ):
        """Create ResourcePolicyRule instance."""
        super(ResourcePolicyRule, self).__init__(
            api_version="flowcontrol/v1beta1", kind="ResourcePolicyRule"
        )
        self._properties = {
            "apiGroups": api_groups if api_groups is not None else [],
            "clusterScope": cluster_scope if cluster_scope is not None else None,
            "namespaces": namespaces if namespaces is not None else [],
            "resources": resources if resources is not None else [],
            "verbs": verbs if verbs is not None else [],
        }
        self._types = {
            "apiGroups": (list, str),
            "clusterScope": (bool, None),
            "namespaces": (list, str),
            "resources": (list, str),
            "verbs": (list, str),
        }

    @property
    def api_groups(self) -> typing.List[str]:
        """
        `apiGroups` is a list of matching API groups and may not be
        empty. "*" matches all API groups and, if present, must be
        the only entry. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("apiGroups"),
        )

    @api_groups.setter
    def api_groups(self, value: typing.List[str]):
        """
        `apiGroups` is a list of matching API groups and may not be
        empty. "*" matches all API groups and, if present, must be
        the only entry. Required.
        """
        self._properties["apiGroups"] = value

    @property
    def cluster_scope(self) -> bool:
        """
        `clusterScope` indicates whether to match requests that do
        not specify a namespace (which happens either because the
        resource is not namespaced or the request targets all
        namespaces). If this field is omitted or false then the
        `namespaces` field must contain a non-empty list.
        """
        return typing.cast(
            bool,
            self._properties.get("clusterScope"),
        )

    @cluster_scope.setter
    def cluster_scope(self, value: bool):
        """
        `clusterScope` indicates whether to match requests that do
        not specify a namespace (which happens either because the
        resource is not namespaced or the request targets all
        namespaces). If this field is omitted or false then the
        `namespaces` field must contain a non-empty list.
        """
        self._properties["clusterScope"] = value

    @property
    def namespaces(self) -> typing.List[str]:
        """
        `namespaces` is a list of target namespaces that restricts
        matches.  A request that specifies a target namespace
        matches only if either (a) this list contains that target
        namespace or (b) this list contains "*".  Note that "*"
        matches any specified namespace but does not match a request
        that _does not specify_ a namespace (see the `clusterScope`
        field for that). This list may be empty, but only if
        `clusterScope` is true.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("namespaces"),
        )

    @namespaces.setter
    def namespaces(self, value: typing.List[str]):
        """
        `namespaces` is a list of target namespaces that restricts
        matches.  A request that specifies a target namespace
        matches only if either (a) this list contains that target
        namespace or (b) this list contains "*".  Note that "*"
        matches any specified namespace but does not match a request
        that _does not specify_ a namespace (see the `clusterScope`
        field for that). This list may be empty, but only if
        `clusterScope` is true.
        """
        self._properties["namespaces"] = value

    @property
    def resources(self) -> typing.List[str]:
        """
        `resources` is a list of matching resources (i.e., lowercase
        and plural) with, if desired, subresource.  For example, [
        "services", "nodes/status" ].  This list may not be empty.
        "*" matches all resources and, if present, must be the only
        entry. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("resources"),
        )

    @resources.setter
    def resources(self, value: typing.List[str]):
        """
        `resources` is a list of matching resources (i.e., lowercase
        and plural) with, if desired, subresource.  For example, [
        "services", "nodes/status" ].  This list may not be empty.
        "*" matches all resources and, if present, must be the only
        entry. Required.
        """
        self._properties["resources"] = value

    @property
    def verbs(self) -> typing.List[str]:
        """
        `verbs` is a list of matching verbs and may not be empty.
        "*" matches all verbs and, if present, must be the only
        entry. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("verbs"),
        )

    @verbs.setter
    def verbs(self, value: typing.List[str]):
        """
        `verbs` is a list of matching verbs and may not be empty.
        "*" matches all verbs and, if present, must be the only
        entry. Required.
        """
        self._properties["verbs"] = value

    def __enter__(self) -> "ResourcePolicyRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceAccountSubject(_kuber_definitions.Definition):
    """
    ServiceAccountSubject holds detailed information for
    service-account-kind subject.
    """

    def __init__(
        self,
        name: str = None,
        namespace: str = None,
    ):
        """Create ServiceAccountSubject instance."""
        super(ServiceAccountSubject, self).__init__(
            api_version="flowcontrol/v1beta1", kind="ServiceAccountSubject"
        )
        self._properties = {
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
        }
        self._types = {
            "name": (str, None),
            "namespace": (str, None),
        }

    @property
    def name(self) -> str:
        """
        `name` is the name of matching ServiceAccount objects, or
        "*" to match regardless of name. Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        `name` is the name of matching ServiceAccount objects, or
        "*" to match regardless of name. Required.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        `namespace` is the namespace of matching ServiceAccount
        objects. Required.
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        `namespace` is the namespace of matching ServiceAccount
        objects. Required.
        """
        self._properties["namespace"] = value

    def __enter__(self) -> "ServiceAccountSubject":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Subject(_kuber_definitions.Definition):
    """
    Subject matches the originator of a request, as identified
    by the request authentication system. There are three ways
    of matching an originator; by user, group, or service
    account.
    """

    def __init__(
        self,
        group: "GroupSubject" = None,
        kind: str = None,
        service_account: "ServiceAccountSubject" = None,
        user: "UserSubject" = None,
    ):
        """Create Subject instance."""
        super(Subject, self).__init__(api_version="flowcontrol/v1beta1", kind="Subject")
        self._properties = {
            "group": group if group is not None else GroupSubject(),
            "kind": kind if kind is not None else "",
            "serviceAccount": service_account
            if service_account is not None
            else ServiceAccountSubject(),
            "user": user if user is not None else UserSubject(),
        }
        self._types = {
            "group": (GroupSubject, None),
            "kind": (str, None),
            "serviceAccount": (ServiceAccountSubject, None),
            "user": (UserSubject, None),
        }

    @property
    def group(self) -> "GroupSubject":
        """"""
        return typing.cast(
            "GroupSubject",
            self._properties.get("group"),
        )

    @group.setter
    def group(self, value: typing.Union["GroupSubject", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                GroupSubject,
                GroupSubject().from_dict(value),
            )
        self._properties["group"] = value

    @property
    def kind(self) -> str:
        """
        Required
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Required
        """
        self._properties["kind"] = value

    @property
    def service_account(self) -> "ServiceAccountSubject":
        """"""
        return typing.cast(
            "ServiceAccountSubject",
            self._properties.get("serviceAccount"),
        )

    @service_account.setter
    def service_account(self, value: typing.Union["ServiceAccountSubject", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                ServiceAccountSubject,
                ServiceAccountSubject().from_dict(value),
            )
        self._properties["serviceAccount"] = value

    @property
    def user(self) -> "UserSubject":
        """"""
        return typing.cast(
            "UserSubject",
            self._properties.get("user"),
        )

    @user.setter
    def user(self, value: typing.Union["UserSubject", dict]):
        """"""
        if isinstance(value, dict):
            value = typing.cast(
                UserSubject,
                UserSubject().from_dict(value),
            )
        self._properties["user"] = value

    def __enter__(self) -> "Subject":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class UserSubject(_kuber_definitions.Definition):
    """
    UserSubject holds detailed information for user-kind
    subject.
    """

    def __init__(
        self,
        name: str = None,
    ):
        """Create UserSubject instance."""
        super(UserSubject, self).__init__(
            api_version="flowcontrol/v1beta1", kind="UserSubject"
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
        `name` is the username that matches, or "*" to match all
        usernames. Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        `name` is the username that matches, or "*" to match all
        usernames. Required.
        """
        self._properties["name"] = value

    def __enter__(self) -> "UserSubject":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
