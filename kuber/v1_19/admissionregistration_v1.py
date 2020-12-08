import typing

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_19.meta_v1 import LabelSelector
from kuber.v1_19.meta_v1 import ListMeta
from kuber.v1_19.meta_v1 import ObjectMeta


class MutatingWebhook(_kuber_definitions.Definition):
    """
    MutatingWebhook describes an admission webhook and the
    resources and operations it applies to.
    """

    def __init__(
        self,
        admission_review_versions: typing.List[str] = None,
        client_config: "WebhookClientConfig" = None,
        failure_policy: str = None,
        match_policy: str = None,
        name: str = None,
        namespace_selector: "LabelSelector" = None,
        object_selector: "LabelSelector" = None,
        reinvocation_policy: str = None,
        rules: typing.List["RuleWithOperations"] = None,
        side_effects: str = None,
        timeout_seconds: int = None,
    ):
        """Create MutatingWebhook instance."""
        super(MutatingWebhook, self).__init__(
            api_version="admissionregistration/v1", kind="MutatingWebhook"
        )
        self._properties = {
            "admissionReviewVersions": admission_review_versions
            if admission_review_versions is not None
            else [],
            "clientConfig": client_config
            if client_config is not None
            else WebhookClientConfig(),
            "failurePolicy": failure_policy if failure_policy is not None else "",
            "matchPolicy": match_policy if match_policy is not None else "",
            "name": name if name is not None else "",
            "namespaceSelector": namespace_selector
            if namespace_selector is not None
            else LabelSelector(),
            "objectSelector": object_selector
            if object_selector is not None
            else LabelSelector(),
            "reinvocationPolicy": reinvocation_policy
            if reinvocation_policy is not None
            else "",
            "rules": rules if rules is not None else [],
            "sideEffects": side_effects if side_effects is not None else "",
            "timeoutSeconds": timeout_seconds if timeout_seconds is not None else None,
        }
        self._types = {
            "admissionReviewVersions": (list, str),
            "clientConfig": (WebhookClientConfig, None),
            "failurePolicy": (str, None),
            "matchPolicy": (str, None),
            "name": (str, None),
            "namespaceSelector": (LabelSelector, None),
            "objectSelector": (LabelSelector, None),
            "reinvocationPolicy": (str, None),
            "rules": (list, RuleWithOperations),
            "sideEffects": (str, None),
            "timeoutSeconds": (int, None),
        }

    @property
    def admission_review_versions(self) -> typing.List[str]:
        """
        AdmissionReviewVersions is an ordered list of preferred
        `AdmissionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, validation will fail for this object. If a
        persisted webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail and be subject to the failure
        policy.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("admissionReviewVersions"),
        )

    @admission_review_versions.setter
    def admission_review_versions(self, value: typing.List[str]):
        """
        AdmissionReviewVersions is an ordered list of preferred
        `AdmissionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, validation will fail for this object. If a
        persisted webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail and be subject to the failure
        policy.
        """
        self._properties["admissionReviewVersions"] = value

    @property
    def client_config(self) -> "WebhookClientConfig":
        """
        ClientConfig defines how to communicate with the hook.
        Required
        """
        return typing.cast(
            "WebhookClientConfig",
            self._properties.get("clientConfig"),
        )

    @client_config.setter
    def client_config(self, value: typing.Union["WebhookClientConfig", dict]):
        """
        ClientConfig defines how to communicate with the hook.
        Required
        """
        if isinstance(value, dict):
            value = typing.cast(
                WebhookClientConfig,
                WebhookClientConfig().from_dict(value),
            )
        self._properties["clientConfig"] = value

    @property
    def failure_policy(self) -> str:
        """
        FailurePolicy defines how unrecognized errors from the
        admission endpoint are handled - allowed values are Ignore
        or Fail. Defaults to Fail.
        """
        return typing.cast(
            str,
            self._properties.get("failurePolicy"),
        )

    @failure_policy.setter
    def failure_policy(self, value: str):
        """
        FailurePolicy defines how unrecognized errors from the
        admission endpoint are handled - allowed values are Ignore
        or Fail. Defaults to Fail.
        """
        self._properties["failurePolicy"] = value

    @property
    def match_policy(self) -> str:
        """
        matchPolicy defines how the "rules" list is used to match
        incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the webhook.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the webhook.

        Defaults to "Equivalent"
        """
        return typing.cast(
            str,
            self._properties.get("matchPolicy"),
        )

    @match_policy.setter
    def match_policy(self, value: str):
        """
        matchPolicy defines how the "rules" list is used to match
        incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the webhook.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the webhook.

        Defaults to "Equivalent"
        """
        self._properties["matchPolicy"] = value

    @property
    def name(self) -> str:
        """
        The name of the admission webhook. Name should be fully
        qualified, e.g., imagepolicy.kubernetes.io, where
        "imagepolicy" is the name of the webhook, and kubernetes.io
        is the name of the organization. Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        The name of the admission webhook. Name should be fully
        qualified, e.g., imagepolicy.kubernetes.io, where
        "imagepolicy" is the name of the webhook, and kubernetes.io
        is the name of the organization. Required.
        """
        self._properties["name"] = value

    @property
    def namespace_selector(self) -> "LabelSelector":
        """
        NamespaceSelector decides whether to run the webhook on an
        object based on whether the namespace for that object
        matches the selector. If the object itself is a namespace,
        the matching is performed on object.metadata.labels. If the
        object is another cluster scoped resource, it never skips
        the webhook.

        For example, to run the webhook on any objects whose
        namespace is not associated with "runlevel" of "0" or "1";
        you will set the selector as follows: "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "runlevel",
              "operator": "NotIn",
              "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If instead you want to only run the webhook on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "environment",
              "operator": "In",
              "values": [
                "prod",
                "staging"
              ]
            }
          ]
        }

        See https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels/ for more examples of label selectors.

        Default to the empty LabelSelector, which matches
        everything.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("namespaceSelector"),
        )

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        NamespaceSelector decides whether to run the webhook on an
        object based on whether the namespace for that object
        matches the selector. If the object itself is a namespace,
        the matching is performed on object.metadata.labels. If the
        object is another cluster scoped resource, it never skips
        the webhook.

        For example, to run the webhook on any objects whose
        namespace is not associated with "runlevel" of "0" or "1";
        you will set the selector as follows: "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "runlevel",
              "operator": "NotIn",
              "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If instead you want to only run the webhook on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "environment",
              "operator": "In",
              "values": [
                "prod",
                "staging"
              ]
            }
          ]
        }

        See https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels/ for more examples of label selectors.

        Default to the empty LabelSelector, which matches
        everything.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["namespaceSelector"] = value

    @property
    def object_selector(self) -> "LabelSelector":
        """
        ObjectSelector decides whether to run the webhook based on
        if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the webhook, and is considered to match if
        either object matches the selector. A null object (oldObject
        in the case of create, or newObject in the case of delete)
        or an object that cannot have labels (like a
        DeploymentRollback or a PodProxyOptions object) is not
        considered to match. Use the object selector only if the
        webhook is opt-in, because end users may skip the admission
        webhook by setting the labels. Default to the empty
        LabelSelector, which matches everything.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("objectSelector"),
        )

    @object_selector.setter
    def object_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        ObjectSelector decides whether to run the webhook based on
        if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the webhook, and is considered to match if
        either object matches the selector. A null object (oldObject
        in the case of create, or newObject in the case of delete)
        or an object that cannot have labels (like a
        DeploymentRollback or a PodProxyOptions object) is not
        considered to match. Use the object selector only if the
        webhook is opt-in, because end users may skip the admission
        webhook by setting the labels. Default to the empty
        LabelSelector, which matches everything.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["objectSelector"] = value

    @property
    def reinvocation_policy(self) -> str:
        """
        reinvocationPolicy indicates whether this webhook should be
        called multiple times as part of a single admission
        evaluation. Allowed values are "Never" and "IfNeeded".

        Never: the webhook will not be called more than once in a
        single admission evaluation.

        IfNeeded: the webhook will be called at least one additional
        time as part of the admission evaluation if the object being
        admitted is modified by other admission plugins after the
        initial webhook call. Webhooks that specify this option
        *must* be idempotent, able to process objects they
        previously admitted. Note: * the number of additional
        invocations is not guaranteed to be exactly one. * if
        additional invocations result in further modifications to
        the object, webhooks are not guaranteed to be invoked again.
        * webhooks that use this option may be reordered to minimize
        the number of additional invocations. * to validate an
        object after all mutations are guaranteed complete, use a
        validating admission webhook instead.

        Defaults to "Never".
        """
        return typing.cast(
            str,
            self._properties.get("reinvocationPolicy"),
        )

    @reinvocation_policy.setter
    def reinvocation_policy(self, value: str):
        """
        reinvocationPolicy indicates whether this webhook should be
        called multiple times as part of a single admission
        evaluation. Allowed values are "Never" and "IfNeeded".

        Never: the webhook will not be called more than once in a
        single admission evaluation.

        IfNeeded: the webhook will be called at least one additional
        time as part of the admission evaluation if the object being
        admitted is modified by other admission plugins after the
        initial webhook call. Webhooks that specify this option
        *must* be idempotent, able to process objects they
        previously admitted. Note: * the number of additional
        invocations is not guaranteed to be exactly one. * if
        additional invocations result in further modifications to
        the object, webhooks are not guaranteed to be invoked again.
        * webhooks that use this option may be reordered to minimize
        the number of additional invocations. * to validate an
        object after all mutations are guaranteed complete, use a
        validating admission webhook instead.

        Defaults to "Never".
        """
        self._properties["reinvocationPolicy"] = value

    @property
    def rules(self) -> typing.List["RuleWithOperations"]:
        """
        Rules describes what operations on what
        resources/subresources the webhook cares about. The webhook
        cares about an operation if it matches _any_ Rule. However,
        in order to prevent ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks from putting the cluster in a
        state which cannot be recovered from without completely
        disabling the plugin, ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks are never called on admission
        requests for ValidatingWebhookConfiguration and
        MutatingWebhookConfiguration objects.
        """
        return typing.cast(
            typing.List["RuleWithOperations"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(
        self, value: typing.Union[typing.List["RuleWithOperations"], typing.List[dict]]
    ):
        """
        Rules describes what operations on what
        resources/subresources the webhook cares about. The webhook
        cares about an operation if it matches _any_ Rule. However,
        in order to prevent ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks from putting the cluster in a
        state which cannot be recovered from without completely
        disabling the plugin, ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks are never called on admission
        requests for ValidatingWebhookConfiguration and
        MutatingWebhookConfiguration objects.
        """
        cleaned: typing.List[RuleWithOperations] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    RuleWithOperations,
                    RuleWithOperations().from_dict(item),
                )
            cleaned.append(typing.cast(RuleWithOperations, item))
        self._properties["rules"] = cleaned

    @property
    def side_effects(self) -> str:
        """
        SideEffects states whether this webhook has side effects.
        Acceptable values are: None, NoneOnDryRun (webhooks created
        via v1beta1 may also specify Some or Unknown). Webhooks with
        side effects MUST implement a reconciliation system, since a
        request may be rejected by a future step in the admission
        change and the side effects therefore need to be undone.
        Requests with the dryRun attribute will be auto-rejected if
        they match a webhook with sideEffects == Unknown or Some.
        """
        return typing.cast(
            str,
            self._properties.get("sideEffects"),
        )

    @side_effects.setter
    def side_effects(self, value: str):
        """
        SideEffects states whether this webhook has side effects.
        Acceptable values are: None, NoneOnDryRun (webhooks created
        via v1beta1 may also specify Some or Unknown). Webhooks with
        side effects MUST implement a reconciliation system, since a
        request may be rejected by a future step in the admission
        change and the side effects therefore need to be undone.
        Requests with the dryRun attribute will be auto-rejected if
        they match a webhook with sideEffects == Unknown or Some.
        """
        self._properties["sideEffects"] = value

    @property
    def timeout_seconds(self) -> int:
        """
        TimeoutSeconds specifies the timeout for this webhook. After
        the timeout passes, the webhook call will be ignored or the
        API call will fail based on the failure policy. The timeout
        value must be between 1 and 30 seconds. Default to 10
        seconds.
        """
        return typing.cast(
            int,
            self._properties.get("timeoutSeconds"),
        )

    @timeout_seconds.setter
    def timeout_seconds(self, value: int):
        """
        TimeoutSeconds specifies the timeout for this webhook. After
        the timeout passes, the webhook call will be ignored or the
        API call will fail based on the failure policy. The timeout
        value must be between 1 and 30 seconds. Default to 10
        seconds.
        """
        self._properties["timeoutSeconds"] = value

    def __enter__(self) -> "MutatingWebhook":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingWebhookConfiguration(_kuber_definitions.Resource):
    """
    MutatingWebhookConfiguration describes the configuration of
    and admission webhook that accept or reject and may change
    the object.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        webhooks: typing.List["MutatingWebhook"] = None,
    ):
        """Create MutatingWebhookConfiguration instance."""
        super(MutatingWebhookConfiguration, self).__init__(
            api_version="admissionregistration/v1", kind="MutatingWebhookConfiguration"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "webhooks": webhooks if webhooks is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "webhooks": (list, MutatingWebhook),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def webhooks(self) -> typing.List["MutatingWebhook"]:
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        return typing.cast(
            typing.List["MutatingWebhook"],
            self._properties.get("webhooks"),
        )

    @webhooks.setter
    def webhooks(
        self, value: typing.Union[typing.List["MutatingWebhook"], typing.List[dict]]
    ):
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        cleaned: typing.List[MutatingWebhook] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MutatingWebhook,
                    MutatingWebhook().from_dict(item),
                )
            cleaned.append(typing.cast(MutatingWebhook, item))
        self._properties["webhooks"] = cleaned

    def create_resource(self, namespace: "str" = None):
        """
        Creates the MutatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_mutating_webhook_configuration",
            "create_mutating_webhook_configuration",
        ]

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
        Replaces the MutatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_mutating_webhook_configuration",
            "replace_mutating_webhook_configuration",
        ]

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
        Patches the MutatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_mutating_webhook_configuration",
            "patch_mutating_webhook_configuration",
        ]

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
        Reads the MutatingWebhookConfiguration from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_mutating_webhook_configuration",
            "read_mutating_webhook_configuration",
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
        Deletes the MutatingWebhookConfiguration from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_mutating_webhook_configuration",
            "delete_mutating_webhook_configuration",
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
    ) -> "client.AdmissionregistrationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1Api(**kwargs)

    def __enter__(self) -> "MutatingWebhookConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MutatingWebhookConfigurationList(_kuber_definitions.Collection):
    """
    MutatingWebhookConfigurationList is a list of
    MutatingWebhookConfiguration.
    """

    def __init__(
        self,
        items: typing.List["MutatingWebhookConfiguration"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create MutatingWebhookConfigurationList instance."""
        super(MutatingWebhookConfigurationList, self).__init__(
            api_version="admissionregistration/v1",
            kind="MutatingWebhookConfigurationList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, MutatingWebhookConfiguration),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["MutatingWebhookConfiguration"]:
        """
        List of MutatingWebhookConfiguration.
        """
        return typing.cast(
            typing.List["MutatingWebhookConfiguration"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["MutatingWebhookConfiguration"], typing.List[dict]
        ],
    ):
        """
        List of MutatingWebhookConfiguration.
        """
        cleaned: typing.List[MutatingWebhookConfiguration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MutatingWebhookConfiguration,
                    MutatingWebhookConfiguration().from_dict(item),
                )
            cleaned.append(typing.cast(MutatingWebhookConfiguration, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
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
        architecture/api-conventions.md#types-kinds
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
    ) -> "client.AdmissionregistrationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1Api(**kwargs)

    def __enter__(self) -> "MutatingWebhookConfigurationList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RuleWithOperations(_kuber_definitions.Definition):
    """
    RuleWithOperations is a tuple of Operations and Resources.
    It is recommended to make sure that all the tuple expansions
    are valid.
    """

    def __init__(
        self,
        api_groups: typing.List[str] = None,
        api_versions: typing.List[str] = None,
        operations: typing.List[str] = None,
        resources: typing.List[str] = None,
        scope: str = None,
    ):
        """Create RuleWithOperations instance."""
        super(RuleWithOperations, self).__init__(
            api_version="admissionregistration/v1", kind="RuleWithOperations"
        )
        self._properties = {
            "apiGroups": api_groups if api_groups is not None else [],
            "apiVersions": api_versions if api_versions is not None else [],
            "operations": operations if operations is not None else [],
            "resources": resources if resources is not None else [],
            "scope": scope if scope is not None else "",
        }
        self._types = {
            "apiGroups": (list, str),
            "apiVersions": (list, str),
            "operations": (list, str),
            "resources": (list, str),
            "scope": (str, None),
        }

    @property
    def api_groups(self) -> typing.List[str]:
        """
        APIGroups is the API groups the resources belong to. '*' is
        all groups. If '*' is present, the length of the slice must
        be one. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("apiGroups"),
        )

    @api_groups.setter
    def api_groups(self, value: typing.List[str]):
        """
        APIGroups is the API groups the resources belong to. '*' is
        all groups. If '*' is present, the length of the slice must
        be one. Required.
        """
        self._properties["apiGroups"] = value

    @property
    def api_versions(self) -> typing.List[str]:
        """
        APIVersions is the API versions the resources belong to. '*'
        is all versions. If '*' is present, the length of the slice
        must be one. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("apiVersions"),
        )

    @api_versions.setter
    def api_versions(self, value: typing.List[str]):
        """
        APIVersions is the API versions the resources belong to. '*'
        is all versions. If '*' is present, the length of the slice
        must be one. Required.
        """
        self._properties["apiVersions"] = value

    @property
    def operations(self) -> typing.List[str]:
        """
        Operations is the operations the admission hook cares about
        - CREATE, UPDATE, DELETE, CONNECT or * for all of those
        operations and any future admission operations that are
        added. If '*' is present, the length of the slice must be
        one. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("operations"),
        )

    @operations.setter
    def operations(self, value: typing.List[str]):
        """
        Operations is the operations the admission hook cares about
        - CREATE, UPDATE, DELETE, CONNECT or * for all of those
        operations and any future admission operations that are
        added. If '*' is present, the length of the slice must be
        one. Required.
        """
        self._properties["operations"] = value

    @property
    def resources(self) -> typing.List[str]:
        """
        Resources is a list of resources this rule applies to.

        For example: 'pods' means pods. 'pods/log' means the log
        subresource of pods. '*' means all resources, but not
        subresources. 'pods/*' means all subresources of pods.
        '*/scale' means all scale subresources. '*/*' means all
        resources and their subresources.

        If wildcard is present, the validation rule will ensure
        resources do not overlap with each other.

        Depending on the enclosing object, subresources might not be
        allowed. Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("resources"),
        )

    @resources.setter
    def resources(self, value: typing.List[str]):
        """
        Resources is a list of resources this rule applies to.

        For example: 'pods' means pods. 'pods/log' means the log
        subresource of pods. '*' means all resources, but not
        subresources. 'pods/*' means all subresources of pods.
        '*/scale' means all scale subresources. '*/*' means all
        resources and their subresources.

        If wildcard is present, the validation rule will ensure
        resources do not overlap with each other.

        Depending on the enclosing object, subresources might not be
        allowed. Required.
        """
        self._properties["resources"] = value

    @property
    def scope(self) -> str:
        """
        scope specifies the scope of this rule. Valid values are
        "Cluster", "Namespaced", and "*" "Cluster" means that only
        cluster-scoped resources will match this rule. Namespace API
        objects are cluster-scoped. "Namespaced" means that only
        namespaced resources will match this rule. "*" means that
        there are no scope restrictions. Subresources match the
        scope of their parent resource. Default is "*".
        """
        return typing.cast(
            str,
            self._properties.get("scope"),
        )

    @scope.setter
    def scope(self, value: str):
        """
        scope specifies the scope of this rule. Valid values are
        "Cluster", "Namespaced", and "*" "Cluster" means that only
        cluster-scoped resources will match this rule. Namespace API
        objects are cluster-scoped. "Namespaced" means that only
        namespaced resources will match this rule. "*" means that
        there are no scope restrictions. Subresources match the
        scope of their parent resource. Default is "*".
        """
        self._properties["scope"] = value

    def __enter__(self) -> "RuleWithOperations":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ServiceReference(_kuber_definitions.Definition):
    """
    ServiceReference holds a reference to Service.legacy.k8s.io
    """

    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        path: str = None,
        port: int = None,
    ):
        """Create ServiceReference instance."""
        super(ServiceReference, self).__init__(
            api_version="admissionregistration/v1", kind="ServiceReference"
        )
        self._properties = {
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "path": path if path is not None else "",
            "port": port if port is not None else None,
        }
        self._types = {
            "name": (str, None),
            "namespace": (str, None),
            "path": (str, None),
            "port": (int, None),
        }

    @property
    def name(self) -> str:
        """
        `name` is the name of the service. Required
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        `name` is the name of the service. Required
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        `namespace` is the namespace of the service. Required
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        `namespace` is the namespace of the service. Required
        """
        self._properties["namespace"] = value

    @property
    def path(self) -> str:
        """
        `path` is an optional URL path which will be sent in any
        request to this service.
        """
        return typing.cast(
            str,
            self._properties.get("path"),
        )

    @path.setter
    def path(self, value: str):
        """
        `path` is an optional URL path which will be sent in any
        request to this service.
        """
        self._properties["path"] = value

    @property
    def port(self) -> int:
        """
        If specified, the port on the service that hosting webhook.
        Default to 443 for backward compatibility. `port` should be
        a valid port number (1-65535, inclusive).
        """
        return typing.cast(
            int,
            self._properties.get("port"),
        )

    @port.setter
    def port(self, value: int):
        """
        If specified, the port on the service that hosting webhook.
        Default to 443 for backward compatibility. `port` should be
        a valid port number (1-65535, inclusive).
        """
        self._properties["port"] = value

    def __enter__(self) -> "ServiceReference":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingWebhook(_kuber_definitions.Definition):
    """
    ValidatingWebhook describes an admission webhook and the
    resources and operations it applies to.
    """

    def __init__(
        self,
        admission_review_versions: typing.List[str] = None,
        client_config: "WebhookClientConfig" = None,
        failure_policy: str = None,
        match_policy: str = None,
        name: str = None,
        namespace_selector: "LabelSelector" = None,
        object_selector: "LabelSelector" = None,
        rules: typing.List["RuleWithOperations"] = None,
        side_effects: str = None,
        timeout_seconds: int = None,
    ):
        """Create ValidatingWebhook instance."""
        super(ValidatingWebhook, self).__init__(
            api_version="admissionregistration/v1", kind="ValidatingWebhook"
        )
        self._properties = {
            "admissionReviewVersions": admission_review_versions
            if admission_review_versions is not None
            else [],
            "clientConfig": client_config
            if client_config is not None
            else WebhookClientConfig(),
            "failurePolicy": failure_policy if failure_policy is not None else "",
            "matchPolicy": match_policy if match_policy is not None else "",
            "name": name if name is not None else "",
            "namespaceSelector": namespace_selector
            if namespace_selector is not None
            else LabelSelector(),
            "objectSelector": object_selector
            if object_selector is not None
            else LabelSelector(),
            "rules": rules if rules is not None else [],
            "sideEffects": side_effects if side_effects is not None else "",
            "timeoutSeconds": timeout_seconds if timeout_seconds is not None else None,
        }
        self._types = {
            "admissionReviewVersions": (list, str),
            "clientConfig": (WebhookClientConfig, None),
            "failurePolicy": (str, None),
            "matchPolicy": (str, None),
            "name": (str, None),
            "namespaceSelector": (LabelSelector, None),
            "objectSelector": (LabelSelector, None),
            "rules": (list, RuleWithOperations),
            "sideEffects": (str, None),
            "timeoutSeconds": (int, None),
        }

    @property
    def admission_review_versions(self) -> typing.List[str]:
        """
        AdmissionReviewVersions is an ordered list of preferred
        `AdmissionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, validation will fail for this object. If a
        persisted webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail and be subject to the failure
        policy.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("admissionReviewVersions"),
        )

    @admission_review_versions.setter
    def admission_review_versions(self, value: typing.List[str]):
        """
        AdmissionReviewVersions is an ordered list of preferred
        `AdmissionReview` versions the Webhook expects. API server
        will try to use first version in the list which it supports.
        If none of the versions specified in this list supported by
        API server, validation will fail for this object. If a
        persisted webhook configuration specifies allowed versions
        and does not include any versions known to the API Server,
        calls to the webhook will fail and be subject to the failure
        policy.
        """
        self._properties["admissionReviewVersions"] = value

    @property
    def client_config(self) -> "WebhookClientConfig":
        """
        ClientConfig defines how to communicate with the hook.
        Required
        """
        return typing.cast(
            "WebhookClientConfig",
            self._properties.get("clientConfig"),
        )

    @client_config.setter
    def client_config(self, value: typing.Union["WebhookClientConfig", dict]):
        """
        ClientConfig defines how to communicate with the hook.
        Required
        """
        if isinstance(value, dict):
            value = typing.cast(
                WebhookClientConfig,
                WebhookClientConfig().from_dict(value),
            )
        self._properties["clientConfig"] = value

    @property
    def failure_policy(self) -> str:
        """
        FailurePolicy defines how unrecognized errors from the
        admission endpoint are handled - allowed values are Ignore
        or Fail. Defaults to Fail.
        """
        return typing.cast(
            str,
            self._properties.get("failurePolicy"),
        )

    @failure_policy.setter
    def failure_policy(self, value: str):
        """
        FailurePolicy defines how unrecognized errors from the
        admission endpoint are handled - allowed values are Ignore
        or Fail. Defaults to Fail.
        """
        self._properties["failurePolicy"] = value

    @property
    def match_policy(self) -> str:
        """
        matchPolicy defines how the "rules" list is used to match
        incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the webhook.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the webhook.

        Defaults to "Equivalent"
        """
        return typing.cast(
            str,
            self._properties.get("matchPolicy"),
        )

    @match_policy.setter
    def match_policy(self, value: str):
        """
        matchPolicy defines how the "rules" list is used to match
        incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the webhook.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the webhook.

        Defaults to "Equivalent"
        """
        self._properties["matchPolicy"] = value

    @property
    def name(self) -> str:
        """
        The name of the admission webhook. Name should be fully
        qualified, e.g., imagepolicy.kubernetes.io, where
        "imagepolicy" is the name of the webhook, and kubernetes.io
        is the name of the organization. Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        The name of the admission webhook. Name should be fully
        qualified, e.g., imagepolicy.kubernetes.io, where
        "imagepolicy" is the name of the webhook, and kubernetes.io
        is the name of the organization. Required.
        """
        self._properties["name"] = value

    @property
    def namespace_selector(self) -> "LabelSelector":
        """
        NamespaceSelector decides whether to run the webhook on an
        object based on whether the namespace for that object
        matches the selector. If the object itself is a namespace,
        the matching is performed on object.metadata.labels. If the
        object is another cluster scoped resource, it never skips
        the webhook.

        For example, to run the webhook on any objects whose
        namespace is not associated with "runlevel" of "0" or "1";
        you will set the selector as follows: "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "runlevel",
              "operator": "NotIn",
              "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If instead you want to only run the webhook on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "environment",
              "operator": "In",
              "values": [
                "prod",
                "staging"
              ]
            }
          ]
        }

        See https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels for more examples of label selectors.

        Default to the empty LabelSelector, which matches
        everything.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("namespaceSelector"),
        )

    @namespace_selector.setter
    def namespace_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        NamespaceSelector decides whether to run the webhook on an
        object based on whether the namespace for that object
        matches the selector. If the object itself is a namespace,
        the matching is performed on object.metadata.labels. If the
        object is another cluster scoped resource, it never skips
        the webhook.

        For example, to run the webhook on any objects whose
        namespace is not associated with "runlevel" of "0" or "1";
        you will set the selector as follows: "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "runlevel",
              "operator": "NotIn",
              "values": [
                "0",
                "1"
              ]
            }
          ]
        }

        If instead you want to only run the webhook on any objects
        whose namespace is associated with the "environment" of
        "prod" or "staging"; you will set the selector as follows:
        "namespaceSelector": {
          "matchExpressions": [
            {
              "key": "environment",
              "operator": "In",
              "values": [
                "prod",
                "staging"
              ]
            }
          ]
        }

        See https://kubernetes.io/docs/concepts/overview/working-
        with-objects/labels for more examples of label selectors.

        Default to the empty LabelSelector, which matches
        everything.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["namespaceSelector"] = value

    @property
    def object_selector(self) -> "LabelSelector":
        """
        ObjectSelector decides whether to run the webhook based on
        if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the webhook, and is considered to match if
        either object matches the selector. A null object (oldObject
        in the case of create, or newObject in the case of delete)
        or an object that cannot have labels (like a
        DeploymentRollback or a PodProxyOptions object) is not
        considered to match. Use the object selector only if the
        webhook is opt-in, because end users may skip the admission
        webhook by setting the labels. Default to the empty
        LabelSelector, which matches everything.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("objectSelector"),
        )

    @object_selector.setter
    def object_selector(self, value: typing.Union["LabelSelector", dict]):
        """
        ObjectSelector decides whether to run the webhook based on
        if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the webhook, and is considered to match if
        either object matches the selector. A null object (oldObject
        in the case of create, or newObject in the case of delete)
        or an object that cannot have labels (like a
        DeploymentRollback or a PodProxyOptions object) is not
        considered to match. Use the object selector only if the
        webhook is opt-in, because end users may skip the admission
        webhook by setting the labels. Default to the empty
        LabelSelector, which matches everything.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["objectSelector"] = value

    @property
    def rules(self) -> typing.List["RuleWithOperations"]:
        """
        Rules describes what operations on what
        resources/subresources the webhook cares about. The webhook
        cares about an operation if it matches _any_ Rule. However,
        in order to prevent ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks from putting the cluster in a
        state which cannot be recovered from without completely
        disabling the plugin, ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks are never called on admission
        requests for ValidatingWebhookConfiguration and
        MutatingWebhookConfiguration objects.
        """
        return typing.cast(
            typing.List["RuleWithOperations"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(
        self, value: typing.Union[typing.List["RuleWithOperations"], typing.List[dict]]
    ):
        """
        Rules describes what operations on what
        resources/subresources the webhook cares about. The webhook
        cares about an operation if it matches _any_ Rule. However,
        in order to prevent ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks from putting the cluster in a
        state which cannot be recovered from without completely
        disabling the plugin, ValidatingAdmissionWebhooks and
        MutatingAdmissionWebhooks are never called on admission
        requests for ValidatingWebhookConfiguration and
        MutatingWebhookConfiguration objects.
        """
        cleaned: typing.List[RuleWithOperations] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    RuleWithOperations,
                    RuleWithOperations().from_dict(item),
                )
            cleaned.append(typing.cast(RuleWithOperations, item))
        self._properties["rules"] = cleaned

    @property
    def side_effects(self) -> str:
        """
        SideEffects states whether this webhook has side effects.
        Acceptable values are: None, NoneOnDryRun (webhooks created
        via v1beta1 may also specify Some or Unknown). Webhooks with
        side effects MUST implement a reconciliation system, since a
        request may be rejected by a future step in the admission
        change and the side effects therefore need to be undone.
        Requests with the dryRun attribute will be auto-rejected if
        they match a webhook with sideEffects == Unknown or Some.
        """
        return typing.cast(
            str,
            self._properties.get("sideEffects"),
        )

    @side_effects.setter
    def side_effects(self, value: str):
        """
        SideEffects states whether this webhook has side effects.
        Acceptable values are: None, NoneOnDryRun (webhooks created
        via v1beta1 may also specify Some or Unknown). Webhooks with
        side effects MUST implement a reconciliation system, since a
        request may be rejected by a future step in the admission
        change and the side effects therefore need to be undone.
        Requests with the dryRun attribute will be auto-rejected if
        they match a webhook with sideEffects == Unknown or Some.
        """
        self._properties["sideEffects"] = value

    @property
    def timeout_seconds(self) -> int:
        """
        TimeoutSeconds specifies the timeout for this webhook. After
        the timeout passes, the webhook call will be ignored or the
        API call will fail based on the failure policy. The timeout
        value must be between 1 and 30 seconds. Default to 10
        seconds.
        """
        return typing.cast(
            int,
            self._properties.get("timeoutSeconds"),
        )

    @timeout_seconds.setter
    def timeout_seconds(self, value: int):
        """
        TimeoutSeconds specifies the timeout for this webhook. After
        the timeout passes, the webhook call will be ignored or the
        API call will fail based on the failure policy. The timeout
        value must be between 1 and 30 seconds. Default to 10
        seconds.
        """
        self._properties["timeoutSeconds"] = value

    def __enter__(self) -> "ValidatingWebhook":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingWebhookConfiguration(_kuber_definitions.Resource):
    """
    ValidatingWebhookConfiguration describes the configuration
    of and admission webhook that accept or reject and object
    without changing it.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        webhooks: typing.List["ValidatingWebhook"] = None,
    ):
        """Create ValidatingWebhookConfiguration instance."""
        super(ValidatingWebhookConfiguration, self).__init__(
            api_version="admissionregistration/v1",
            kind="ValidatingWebhookConfiguration",
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "webhooks": webhooks if webhooks is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "webhooks": (list, ValidatingWebhook),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        return typing.cast(
            "ObjectMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ObjectMeta", dict]):
        """
        Standard object metadata; More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#metadata.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ObjectMeta,
                ObjectMeta().from_dict(value),
            )
        self._properties["metadata"] = value

    @property
    def webhooks(self) -> typing.List["ValidatingWebhook"]:
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        return typing.cast(
            typing.List["ValidatingWebhook"],
            self._properties.get("webhooks"),
        )

    @webhooks.setter
    def webhooks(
        self, value: typing.Union[typing.List["ValidatingWebhook"], typing.List[dict]]
    ):
        """
        Webhooks is a list of webhooks and the affected resources
        and operations.
        """
        cleaned: typing.List[ValidatingWebhook] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ValidatingWebhook,
                    ValidatingWebhook().from_dict(item),
                )
            cleaned.append(typing.cast(ValidatingWebhook, item))
        self._properties["webhooks"] = cleaned

    def create_resource(self, namespace: "str" = None):
        """
        Creates the ValidatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_validating_webhook_configuration",
            "create_validating_webhook_configuration",
        ]

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
        Replaces the ValidatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_validating_webhook_configuration",
            "replace_validating_webhook_configuration",
        ]

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
        Patches the ValidatingWebhookConfiguration in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_validating_webhook_configuration",
            "patch_validating_webhook_configuration",
        ]

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
        Reads the ValidatingWebhookConfiguration from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_validating_webhook_configuration",
            "read_validating_webhook_configuration",
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
        Deletes the ValidatingWebhookConfiguration from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_validating_webhook_configuration",
            "delete_validating_webhook_configuration",
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
    ) -> "client.AdmissionregistrationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1Api(**kwargs)

    def __enter__(self) -> "ValidatingWebhookConfiguration":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingWebhookConfigurationList(_kuber_definitions.Collection):
    """
    ValidatingWebhookConfigurationList is a list of
    ValidatingWebhookConfiguration.
    """

    def __init__(
        self,
        items: typing.List["ValidatingWebhookConfiguration"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create ValidatingWebhookConfigurationList instance."""
        super(ValidatingWebhookConfigurationList, self).__init__(
            api_version="admissionregistration/v1",
            kind="ValidatingWebhookConfigurationList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ValidatingWebhookConfiguration),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ValidatingWebhookConfiguration"]:
        """
        List of ValidatingWebhookConfiguration.
        """
        return typing.cast(
            typing.List["ValidatingWebhookConfiguration"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["ValidatingWebhookConfiguration"], typing.List[dict]
        ],
    ):
        """
        List of ValidatingWebhookConfiguration.
        """
        cleaned: typing.List[ValidatingWebhookConfiguration] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ValidatingWebhookConfiguration,
                    ValidatingWebhookConfiguration().from_dict(item),
                )
            cleaned.append(typing.cast(ValidatingWebhookConfiguration, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#types-kinds
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
        architecture/api-conventions.md#types-kinds
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
    ) -> "client.AdmissionregistrationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1Api(**kwargs)

    def __enter__(self) -> "ValidatingWebhookConfigurationList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class WebhookClientConfig(_kuber_definitions.Definition):
    """
    WebhookClientConfig contains the information to make a TLS
    connection with the webhook
    """

    def __init__(
        self,
        ca_bundle: str = None,
        service: "ServiceReference" = None,
        url: str = None,
    ):
        """Create WebhookClientConfig instance."""
        super(WebhookClientConfig, self).__init__(
            api_version="admissionregistration/v1", kind="WebhookClientConfig"
        )
        self._properties = {
            "caBundle": ca_bundle if ca_bundle is not None else "",
            "service": service if service is not None else ServiceReference(),
            "url": url if url is not None else "",
        }
        self._types = {
            "caBundle": (str, None),
            "service": (ServiceReference, None),
            "url": (str, None),
        }

    @property
    def ca_bundle(self) -> str:
        """
        `caBundle` is a PEM encoded CA bundle which will be used to
        validate the webhook's server certificate. If unspecified,
        system trust roots on the apiserver are used.
        """
        return typing.cast(
            str,
            self._properties.get("caBundle"),
        )

    @ca_bundle.setter
    def ca_bundle(self, value: str):
        """
        `caBundle` is a PEM encoded CA bundle which will be used to
        validate the webhook's server certificate. If unspecified,
        system trust roots on the apiserver are used.
        """
        self._properties["caBundle"] = value

    @property
    def service(self) -> "ServiceReference":
        """
        `service` is a reference to the service for this webhook.
        Either `service` or `url` must be specified.

        If the webhook is running within the cluster, then you
        should use `service`.
        """
        return typing.cast(
            "ServiceReference",
            self._properties.get("service"),
        )

    @service.setter
    def service(self, value: typing.Union["ServiceReference", dict]):
        """
        `service` is a reference to the service for this webhook.
        Either `service` or `url` must be specified.

        If the webhook is running within the cluster, then you
        should use `service`.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ServiceReference,
                ServiceReference().from_dict(value),
            )
        self._properties["service"] = value

    @property
    def url(self) -> str:
        """
        `url` gives the location of the webhook, in standard URL
        form (`scheme://host:port/path`). Exactly one of `url` or
        `service` must be specified.

        The `host` should not refer to a service running in the
        cluster; use the `service` field instead. The host might be
        resolved via external DNS in some apiservers (e.g., `kube-
        apiserver` cannot resolve in-cluster DNS as that would be a
        layering violation). `host` may also be an IP address.

        Please note that using `localhost` or `127.0.0.1` as a
        `host` is risky unless you take great care to run this
        webhook on all hosts which run an apiserver which might need
        to make calls to this webhook. Such installs are likely to
        be non-portable, i.e., not easy to turn up in a new cluster.

        The scheme must be "https"; the URL must begin with
        "https://".

        A path is optional, and if present may be any string
        permissible in a URL. You may use the path to pass an
        arbitrary string to the webhook, for example, a cluster
        identifier.

        Attempting to use a user or basic auth e.g. "user:password@"
        is not allowed. Fragments ("#...") and query parameters
        ("?...") are not allowed, either.
        """
        return typing.cast(
            str,
            self._properties.get("url"),
        )

    @url.setter
    def url(self, value: str):
        """
        `url` gives the location of the webhook, in standard URL
        form (`scheme://host:port/path`). Exactly one of `url` or
        `service` must be specified.

        The `host` should not refer to a service running in the
        cluster; use the `service` field instead. The host might be
        resolved via external DNS in some apiservers (e.g., `kube-
        apiserver` cannot resolve in-cluster DNS as that would be a
        layering violation). `host` may also be an IP address.

        Please note that using `localhost` or `127.0.0.1` as a
        `host` is risky unless you take great care to run this
        webhook on all hosts which run an apiserver which might need
        to make calls to this webhook. Such installs are likely to
        be non-portable, i.e., not easy to turn up in a new cluster.

        The scheme must be "https"; the URL must begin with
        "https://".

        A path is optional, and if present may be any string
        permissible in a URL. You may use the path to pass an
        arbitrary string to the webhook, for example, a cluster
        identifier.

        Attempting to use a user or basic auth e.g. "user:password@"
        is not allowed. Fragments ("#...") and query parameters
        ("?...") are not allowed, either.
        """
        self._properties["url"] = value

    def __enter__(self) -> "WebhookClientConfig":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
