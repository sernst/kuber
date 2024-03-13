import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_30.meta_v1 import Condition  # noqa: F401
from kuber.v1_30.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_30.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_30.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_30.meta_v1 import Status  # noqa: F401
from kuber.v1_30.meta_v1 import StatusDetails  # noqa: F401


class AuditAnnotation(_kuber_definitions.Definition):
    """
    AuditAnnotation describes how to produce an audit annotation
    for an API request.
    """

    def __init__(
        self,
        key: typing.Optional[str] = None,
        value_expression: typing.Optional[str] = None,
    ):
        """Create AuditAnnotation instance."""
        super(AuditAnnotation, self).__init__(
            api_version="admissionregistration/v1beta1", kind="AuditAnnotation"
        )
        self._properties = {
            "key": key if key is not None else "",
            "valueExpression": value_expression if value_expression is not None else "",
        }
        self._types = {
            "key": (str, None),
            "valueExpression": (str, None),
        }

    @property
    def key(self) -> str:
        """
        key specifies the audit annotation key. The audit annotation
        keys of a ValidatingAdmissionPolicy must be unique. The key
        must be a qualified name ([A-Za-z0-9][-A-Za-z0-9_.]*) no
        more than 63 bytes in length.

        The key is combined with the resource name of the
        ValidatingAdmissionPolicy to construct an audit annotation
        key: "{ValidatingAdmissionPolicy name}/{key}".

        If an admission webhook uses the same resource name as this
        ValidatingAdmissionPolicy and the same audit annotation key,
        the annotation key will be identical. In this case, the
        first annotation written with the key will be included in
        the audit event and all subsequent annotations with the same
        key will be discarded.

        Required.
        """
        return typing.cast(
            str,
            self._properties.get("key"),
        )

    @key.setter
    def key(self, value: str):
        """
        key specifies the audit annotation key. The audit annotation
        keys of a ValidatingAdmissionPolicy must be unique. The key
        must be a qualified name ([A-Za-z0-9][-A-Za-z0-9_.]*) no
        more than 63 bytes in length.

        The key is combined with the resource name of the
        ValidatingAdmissionPolicy to construct an audit annotation
        key: "{ValidatingAdmissionPolicy name}/{key}".

        If an admission webhook uses the same resource name as this
        ValidatingAdmissionPolicy and the same audit annotation key,
        the annotation key will be identical. In this case, the
        first annotation written with the key will be included in
        the audit event and all subsequent annotations with the same
        key will be discarded.

        Required.
        """
        self._properties["key"] = value

    @property
    def value_expression(self) -> str:
        """
        valueExpression represents the expression which is evaluated
        by CEL to produce an audit annotation value. The expression
        must evaluate to either a string or null value. If the
        expression evaluates to a string, the audit annotation is
        included with the string value. If the expression evaluates
        to null or empty string the audit annotation will be
        omitted. The valueExpression may be no longer than 5kb in
        length. If the result of the valueExpression is more than
        10kb in length, it will be truncated to 10kb.

        If multiple ValidatingAdmissionPolicyBinding resources match
        an API request, then the valueExpression will be evaluated
        for each binding. All unique values produced by the
        valueExpressions will be joined together in a comma-
        separated list.

        Required.
        """
        return typing.cast(
            str,
            self._properties.get("valueExpression"),
        )

    @value_expression.setter
    def value_expression(self, value: str):
        """
        valueExpression represents the expression which is evaluated
        by CEL to produce an audit annotation value. The expression
        must evaluate to either a string or null value. If the
        expression evaluates to a string, the audit annotation is
        included with the string value. If the expression evaluates
        to null or empty string the audit annotation will be
        omitted. The valueExpression may be no longer than 5kb in
        length. If the result of the valueExpression is more than
        10kb in length, it will be truncated to 10kb.

        If multiple ValidatingAdmissionPolicyBinding resources match
        an API request, then the valueExpression will be evaluated
        for each binding. All unique values produced by the
        valueExpressions will be joined together in a comma-
        separated list.

        Required.
        """
        self._properties["valueExpression"] = value

    def __enter__(self) -> "AuditAnnotation":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ExpressionWarning(_kuber_definitions.Definition):
    """
    ExpressionWarning is a warning information that targets a
    specific expression.
    """

    def __init__(
        self,
        field_ref: typing.Optional[str] = None,
        warning: typing.Optional[str] = None,
    ):
        """Create ExpressionWarning instance."""
        super(ExpressionWarning, self).__init__(
            api_version="admissionregistration/v1beta1", kind="ExpressionWarning"
        )
        self._properties = {
            "fieldRef": field_ref if field_ref is not None else "",
            "warning": warning if warning is not None else "",
        }
        self._types = {
            "fieldRef": (str, None),
            "warning": (str, None),
        }

    @property
    def field_ref(self) -> str:
        """
        The path to the field that refers the expression. For
        example, the reference to the expression of the first item
        of validations is "spec.validations[0].expression"
        """
        return typing.cast(
            str,
            self._properties.get("fieldRef"),
        )

    @field_ref.setter
    def field_ref(self, value: str):
        """
        The path to the field that refers the expression. For
        example, the reference to the expression of the first item
        of validations is "spec.validations[0].expression"
        """
        self._properties["fieldRef"] = value

    @property
    def warning(self) -> str:
        """
        The content of type checking information in a human-readable
        form. Each line of the warning contains the type that the
        expression is checked against, followed by the type check
        error from the compiler.
        """
        return typing.cast(
            str,
            self._properties.get("warning"),
        )

    @warning.setter
    def warning(self, value: str):
        """
        The content of type checking information in a human-readable
        form. Each line of the warning contains the type that the
        expression is checked against, followed by the type check
        error from the compiler.
        """
        self._properties["warning"] = value

    def __enter__(self) -> "ExpressionWarning":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MatchCondition(_kuber_definitions.Definition):
    """
    MatchCondition represents a condition which must be
    fulfilled for a request to be sent to a webhook.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ):
        """Create MatchCondition instance."""
        super(MatchCondition, self).__init__(
            api_version="admissionregistration/v1beta1", kind="MatchCondition"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
            "name": name if name is not None else "",
        }
        self._types = {
            "expression": (str, None),
            "name": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        Expression represents the expression which will be evaluated
        by CEL. Must evaluate to bool. CEL expressions have access
        to the contents of the AdmissionRequest and Authorizer,
        organized into CEL variables:

        'object' - The object from the incoming request. The value
        is null for DELETE requests. 'oldObject' - The existing
        object. The value is null for CREATE requests. 'request' -
        Attributes of the admission
        request(/pkg/apis/admission/types.go#AdmissionRequest).
        'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.
        Documentation on CEL:
        https://kubernetes.io/docs/reference/using-api/cel/

        Required.
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        Expression represents the expression which will be evaluated
        by CEL. Must evaluate to bool. CEL expressions have access
        to the contents of the AdmissionRequest and Authorizer,
        organized into CEL variables:

        'object' - The object from the incoming request. The value
        is null for DELETE requests. 'oldObject' - The existing
        object. The value is null for CREATE requests. 'request' -
        Attributes of the admission
        request(/pkg/apis/admission/types.go#AdmissionRequest).
        'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.
        Documentation on CEL:
        https://kubernetes.io/docs/reference/using-api/cel/

        Required.
        """
        self._properties["expression"] = value

    @property
    def name(self) -> str:
        """
        Name is an identifier for this match condition, used for
        strategic merging of MatchConditions, as well as providing
        an identifier for logging purposes. A good name should be
        descriptive of the associated expression. Name must be a
        qualified name consisting of alphanumeric characters, '-',
        '_' or '.', and must start and end with an alphanumeric
        character (e.g. 'MyName',  or 'my.name',  or '123-abc',
        regex used for validation is
        '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an optional
        DNS subdomain prefix and '/' (e.g. 'example.com/MyName')

        Required.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is an identifier for this match condition, used for
        strategic merging of MatchConditions, as well as providing
        an identifier for logging purposes. A good name should be
        descriptive of the associated expression. Name must be a
        qualified name consisting of alphanumeric characters, '-',
        '_' or '.', and must start and end with an alphanumeric
        character (e.g. 'MyName',  or 'my.name',  or '123-abc',
        regex used for validation is
        '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an optional
        DNS subdomain prefix and '/' (e.g. 'example.com/MyName')

        Required.
        """
        self._properties["name"] = value

    def __enter__(self) -> "MatchCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MatchResources(_kuber_definitions.Definition):
    """
    MatchResources decides whether to run the admission control
    policy on an object based on whether it meets the match
    criteria. The exclude rules take precedence over include
    rules (if a resource matches both, it is excluded)
    """

    def __init__(
        self,
        exclude_resource_rules: typing.Optional[
            typing.List["NamedRuleWithOperations"]
        ] = None,
        match_policy: typing.Optional[str] = None,
        namespace_selector: typing.Optional["LabelSelector"] = None,
        object_selector: typing.Optional["LabelSelector"] = None,
        resource_rules: typing.Optional[typing.List["NamedRuleWithOperations"]] = None,
    ):
        """Create MatchResources instance."""
        super(MatchResources, self).__init__(
            api_version="admissionregistration/v1beta1", kind="MatchResources"
        )
        self._properties = {
            "excludeResourceRules": (
                exclude_resource_rules if exclude_resource_rules is not None else []
            ),
            "matchPolicy": match_policy if match_policy is not None else "",
            "namespaceSelector": (
                namespace_selector
                if namespace_selector is not None
                else LabelSelector()
            ),
            "objectSelector": (
                object_selector if object_selector is not None else LabelSelector()
            ),
            "resourceRules": resource_rules if resource_rules is not None else [],
        }
        self._types = {
            "excludeResourceRules": (list, NamedRuleWithOperations),
            "matchPolicy": (str, None),
            "namespaceSelector": (LabelSelector, None),
            "objectSelector": (LabelSelector, None),
            "resourceRules": (list, NamedRuleWithOperations),
        }

    @property
    def exclude_resource_rules(self) -> typing.List["NamedRuleWithOperations"]:
        """
        ExcludeResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy should
        not care about. The exclude rules take precedence over
        include rules (if a resource matches both, it is excluded)
        """
        return typing.cast(
            typing.List["NamedRuleWithOperations"],
            self._properties.get("excludeResourceRules"),
        )

    @exclude_resource_rules.setter
    def exclude_resource_rules(
        self,
        value: typing.Union[typing.List["NamedRuleWithOperations"], typing.List[dict]],
    ):
        """
        ExcludeResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy should
        not care about. The exclude rules take precedence over
        include rules (if a resource matches both, it is excluded)
        """
        cleaned: typing.List[NamedRuleWithOperations] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NamedRuleWithOperations,
                    NamedRuleWithOperations().from_dict(item),
                )
            cleaned.append(typing.cast(NamedRuleWithOperations, item))
        self._properties["excludeResourceRules"] = cleaned

    @property
    def match_policy(self) -> str:
        """
        matchPolicy defines how the "MatchResources" list is used to
        match incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the ValidatingAdmissionPolicy.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the ValidatingAdmissionPolicy.

        Defaults to "Equivalent"
        """
        return typing.cast(
            str,
            self._properties.get("matchPolicy"),
        )

    @match_policy.setter
    def match_policy(self, value: str):
        """
        matchPolicy defines how the "MatchResources" list is used to
        match incoming requests. Allowed values are "Exact" or
        "Equivalent".

        - Exact: match a request only if it exactly matches a
        specified rule. For example, if deployments can be modified
        via apps/v1, apps/v1beta1, and extensions/v1beta1, but
        "rules" only included `apiGroups:["apps"],
        apiVersions:["v1"], resources: ["deployments"]`, a request
        to apps/v1beta1 or extensions/v1beta1 would not be sent to
        the ValidatingAdmissionPolicy.

        - Equivalent: match a request if modifies a resource listed
        in rules, even via another API group or version. For
        example, if deployments can be modified via apps/v1,
        apps/v1beta1, and extensions/v1beta1, and "rules" only
        included `apiGroups:["apps"], apiVersions:["v1"], resources:
        ["deployments"]`, a request to apps/v1beta1 or
        extensions/v1beta1 would be converted to apps/v1 and sent to
        the ValidatingAdmissionPolicy.

        Defaults to "Equivalent"
        """
        self._properties["matchPolicy"] = value

    @property
    def namespace_selector(self) -> "LabelSelector":
        """
        NamespaceSelector decides whether to run the admission
        control policy on an object based on whether the namespace
        for that object matches the selector. If the object itself
        is a namespace, the matching is performed on
        object.metadata.labels. If the object is another cluster
        scoped resource, it never skips the policy.

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

        If instead you want to only run the policy on any objects
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
        NamespaceSelector decides whether to run the admission
        control policy on an object based on whether the namespace
        for that object matches the selector. If the object itself
        is a namespace, the matching is performed on
        object.metadata.labels. If the object is another cluster
        scoped resource, it never skips the policy.

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

        If instead you want to only run the policy on any objects
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
        ObjectSelector decides whether to run the validation based
        on if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the cel validation, and is considered to
        match if either object matches the selector. A null object
        (oldObject in the case of create, or newObject in the case
        of delete) or an object that cannot have labels (like a
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
        ObjectSelector decides whether to run the validation based
        on if the object has matching labels. objectSelector is
        evaluated against both the oldObject and newObject that
        would be sent to the cel validation, and is considered to
        match if either object matches the selector. A null object
        (oldObject in the case of create, or newObject in the case
        of delete) or an object that cannot have labels (like a
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
    def resource_rules(self) -> typing.List["NamedRuleWithOperations"]:
        """
        ResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy
        matches. The policy cares about an operation if it matches
        _any_ Rule.
        """
        return typing.cast(
            typing.List["NamedRuleWithOperations"],
            self._properties.get("resourceRules"),
        )

    @resource_rules.setter
    def resource_rules(
        self,
        value: typing.Union[typing.List["NamedRuleWithOperations"], typing.List[dict]],
    ):
        """
        ResourceRules describes what operations on what
        resources/subresources the ValidatingAdmissionPolicy
        matches. The policy cares about an operation if it matches
        _any_ Rule.
        """
        cleaned: typing.List[NamedRuleWithOperations] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    NamedRuleWithOperations,
                    NamedRuleWithOperations().from_dict(item),
                )
            cleaned.append(typing.cast(NamedRuleWithOperations, item))
        self._properties["resourceRules"] = cleaned

    def __enter__(self) -> "MatchResources":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NamedRuleWithOperations(_kuber_definitions.Definition):
    """
    NamedRuleWithOperations is a tuple of Operations and
    Resources with ResourceNames.
    """

    def __init__(
        self,
        api_groups: typing.Optional[typing.List[str]] = None,
        api_versions: typing.Optional[typing.List[str]] = None,
        operations: typing.Optional[typing.List[str]] = None,
        resource_names: typing.Optional[typing.List[str]] = None,
        resources: typing.Optional[typing.List[str]] = None,
        scope: typing.Optional[str] = None,
    ):
        """Create NamedRuleWithOperations instance."""
        super(NamedRuleWithOperations, self).__init__(
            api_version="admissionregistration/v1beta1", kind="NamedRuleWithOperations"
        )
        self._properties = {
            "apiGroups": api_groups if api_groups is not None else [],
            "apiVersions": api_versions if api_versions is not None else [],
            "operations": operations if operations is not None else [],
            "resourceNames": resource_names if resource_names is not None else [],
            "resources": resources if resources is not None else [],
            "scope": scope if scope is not None else "",
        }
        self._types = {
            "apiGroups": (list, str),
            "apiVersions": (list, str),
            "operations": (list, str),
            "resourceNames": (list, str),
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
    def resource_names(self) -> typing.List[str]:
        """
        ResourceNames is an optional white list of names that the
        rule applies to.  An empty set means that everything is
        allowed.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("resourceNames"),
        )

    @resource_names.setter
    def resource_names(self, value: typing.List[str]):
        """
        ResourceNames is an optional white list of names that the
        rule applies to.  An empty set means that everything is
        allowed.
        """
        self._properties["resourceNames"] = value

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

    def __enter__(self) -> "NamedRuleWithOperations":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ParamKind(_kuber_definitions.Definition):
    """
    ParamKind is a tuple of Group Kind and Version.
    """

    def __init__(
        self,
        api_version: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
    ):
        """Create ParamKind instance."""
        super(ParamKind, self).__init__(
            api_version="admissionregistration/v1beta1", kind="ParamKind"
        )
        self._properties = {
            "apiVersion": api_version if api_version is not None else "",
            "kind": kind if kind is not None else "",
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
        }

    @property
    def api_version(self) -> str:
        """
        APIVersion is the API group version the resources belong to.
        In format of "group/version". Required.
        """
        return typing.cast(
            str,
            self._properties.get("apiVersion"),
        )

    @api_version.setter
    def api_version(self, value: str):
        """
        APIVersion is the API group version the resources belong to.
        In format of "group/version". Required.
        """
        self._properties["apiVersion"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the API kind the resources belong to. Required.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the API kind the resources belong to. Required.
        """
        self._properties["kind"] = value

    def __enter__(self) -> "ParamKind":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ParamRef(_kuber_definitions.Definition):
    """
    ParamRef describes how to locate the params to be used as
    input to expressions of rules applied by a policy binding.
    """

    def __init__(
        self,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
        parameter_not_found_action: typing.Optional[str] = None,
        selector: typing.Optional["LabelSelector"] = None,
    ):
        """Create ParamRef instance."""
        super(ParamRef, self).__init__(
            api_version="admissionregistration/v1beta1", kind="ParamRef"
        )
        self._properties = {
            "name": name if name is not None else "",
            "namespace": namespace if namespace is not None else "",
            "parameterNotFoundAction": (
                parameter_not_found_action
                if parameter_not_found_action is not None
                else ""
            ),
            "selector": selector if selector is not None else LabelSelector(),
        }
        self._types = {
            "name": (str, None),
            "namespace": (str, None),
            "parameterNotFoundAction": (str, None),
            "selector": (LabelSelector, None),
        }

    @property
    def name(self) -> str:
        """
        name is the name of the resource being referenced.

        One of `name` or `selector` must be set, but `name` and
        `selector` are mutually exclusive properties. If one is set,
        the other must be unset.

        A single parameter used for all admission requests can be
        configured by setting the `name` field, leaving `selector`
        blank, and setting namespace if `paramKind` is namespace-
        scoped.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        name is the name of the resource being referenced.

        One of `name` or `selector` must be set, but `name` and
        `selector` are mutually exclusive properties. If one is set,
        the other must be unset.

        A single parameter used for all admission requests can be
        configured by setting the `name` field, leaving `selector`
        blank, and setting namespace if `paramKind` is namespace-
        scoped.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        namespace is the namespace of the referenced resource.
        Allows limiting the search for params to a specific
        namespace. Applies to both `name` and `selector` fields.

        A per-namespace parameter may be used by specifying a
        namespace-scoped `paramKind` in the policy and leaving this
        field empty.

        - If `paramKind` is cluster-scoped, this field MUST be
        unset. Setting this field results in a configuration error.

        - If `paramKind` is namespace-scoped, the namespace of the
        object being evaluated for admission will be used when this
        field is left unset. Take care that if this is left empty
        the binding must not match any cluster-scoped resources,
        which will result in an error.
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        namespace is the namespace of the referenced resource.
        Allows limiting the search for params to a specific
        namespace. Applies to both `name` and `selector` fields.

        A per-namespace parameter may be used by specifying a
        namespace-scoped `paramKind` in the policy and leaving this
        field empty.

        - If `paramKind` is cluster-scoped, this field MUST be
        unset. Setting this field results in a configuration error.

        - If `paramKind` is namespace-scoped, the namespace of the
        object being evaluated for admission will be used when this
        field is left unset. Take care that if this is left empty
        the binding must not match any cluster-scoped resources,
        which will result in an error.
        """
        self._properties["namespace"] = value

    @property
    def parameter_not_found_action(self) -> str:
        """
        `parameterNotFoundAction` controls the behavior of the
        binding when the resource exists, and name or selector is
        valid, but there are no parameters matched by the binding.
        If the value is set to `Allow`, then no matched parameters
        will be treated as successful validation by the binding. If
        set to `Deny`, then no matched parameters will be subject to
        the `failurePolicy` of the policy.

        Allowed values are `Allow` or `Deny`

        Required
        """
        return typing.cast(
            str,
            self._properties.get("parameterNotFoundAction"),
        )

    @parameter_not_found_action.setter
    def parameter_not_found_action(self, value: str):
        """
        `parameterNotFoundAction` controls the behavior of the
        binding when the resource exists, and name or selector is
        valid, but there are no parameters matched by the binding.
        If the value is set to `Allow`, then no matched parameters
        will be treated as successful validation by the binding. If
        set to `Deny`, then no matched parameters will be subject to
        the `failurePolicy` of the policy.

        Allowed values are `Allow` or `Deny`

        Required
        """
        self._properties["parameterNotFoundAction"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        selector can be used to match multiple param objects based
        on their labels. Supply selector: {} to match all resources
        of the ParamKind.

        If multiple params are found, they are all evaluated with
        the policy expressions and the results are ANDed together.

        One of `name` or `selector` must be set, but `name` and
        `selector` are mutually exclusive properties. If one is set,
        the other must be unset.
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        selector can be used to match multiple param objects based
        on their labels. Supply selector: {} to match all resources
        of the ParamKind.

        If multiple params are found, they are all evaluated with
        the policy expressions and the results are ANDed together.

        One of `name` or `selector` must be set, but `name` and
        `selector` are mutually exclusive properties. If one is set,
        the other must be unset.
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    def __enter__(self) -> "ParamRef":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TypeChecking(_kuber_definitions.Definition):
    """
    TypeChecking contains results of type checking the
    expressions in the ValidatingAdmissionPolicy
    """

    def __init__(
        self,
        expression_warnings: typing.Optional[typing.List["ExpressionWarning"]] = None,
    ):
        """Create TypeChecking instance."""
        super(TypeChecking, self).__init__(
            api_version="admissionregistration/v1beta1", kind="TypeChecking"
        )
        self._properties = {
            "expressionWarnings": (
                expression_warnings if expression_warnings is not None else []
            ),
        }
        self._types = {
            "expressionWarnings": (list, ExpressionWarning),
        }

    @property
    def expression_warnings(self) -> typing.List["ExpressionWarning"]:
        """
        The type checking warnings for each expression.
        """
        return typing.cast(
            typing.List["ExpressionWarning"],
            self._properties.get("expressionWarnings"),
        )

    @expression_warnings.setter
    def expression_warnings(
        self, value: typing.Union[typing.List["ExpressionWarning"], typing.List[dict]]
    ):
        """
        The type checking warnings for each expression.
        """
        cleaned: typing.List[ExpressionWarning] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ExpressionWarning,
                    ExpressionWarning().from_dict(item),
                )
            cleaned.append(typing.cast(ExpressionWarning, item))
        self._properties["expressionWarnings"] = cleaned

    def __enter__(self) -> "TypeChecking":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicy(_kuber_definitions.Resource):
    """
    ValidatingAdmissionPolicy describes the definition of an
    admission validation policy that accepts or rejects an
    object without changing it.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ValidatingAdmissionPolicySpec"] = None,
        status: typing.Optional["ValidatingAdmissionPolicyStatus"] = None,
    ):
        """Create ValidatingAdmissionPolicy instance."""
        super(ValidatingAdmissionPolicy, self).__init__(
            api_version="admissionregistration/v1beta1",
            kind="ValidatingAdmissionPolicy",
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else ValidatingAdmissionPolicySpec(),
            "status": (
                status if status is not None else ValidatingAdmissionPolicyStatus()
            ),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ValidatingAdmissionPolicySpec, None),
            "status": (ValidatingAdmissionPolicyStatus, None),
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
    def spec(self) -> "ValidatingAdmissionPolicySpec":
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicy.
        """
        return typing.cast(
            "ValidatingAdmissionPolicySpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ValidatingAdmissionPolicySpec", dict]):
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicy.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ValidatingAdmissionPolicySpec,
                ValidatingAdmissionPolicySpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "ValidatingAdmissionPolicyStatus":
        """
        The status of the ValidatingAdmissionPolicy, including
        warnings that are useful to determine if the policy behaves
        in the expected way. Populated by the system. Read-only.
        """
        return typing.cast(
            "ValidatingAdmissionPolicyStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["ValidatingAdmissionPolicyStatus", dict]):
        """
        The status of the ValidatingAdmissionPolicy, including
        warnings that are useful to determine if the policy behaves
        in the expected way. Populated by the system. Read-only.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ValidatingAdmissionPolicyStatus,
                ValidatingAdmissionPolicyStatus().from_dict(value),
            )
        self._properties["status"] = value

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ValidatingAdmissionPolicyStatus":
        """
        Creates the ValidatingAdmissionPolicy in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = [
            "create_namespaced_validating_admission_policy",
            "create_validating_admission_policy",
        ]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = ValidatingAdmissionPolicyStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ValidatingAdmissionPolicyStatus":
        """
        Replaces the ValidatingAdmissionPolicy in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "replace_namespaced_validating_admission_policy",
            "replace_validating_admission_policy",
        ]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ValidatingAdmissionPolicyStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "ValidatingAdmissionPolicyStatus":
        """
        Patches the ValidatingAdmissionPolicy in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = [
            "patch_namespaced_validating_admission_policy",
            "patch_validating_admission_policy",
        ]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = ValidatingAdmissionPolicyStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "ValidatingAdmissionPolicyStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_validating_admission_policy",
            "read_validating_admission_policy",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = ValidatingAdmissionPolicyStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the ValidatingAdmissionPolicy from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_validating_admission_policy",
            "read_validating_admission_policy",
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
        Deletes the ValidatingAdmissionPolicy from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_validating_admission_policy",
            "delete_validating_admission_policy",
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
    ) -> "client.AdmissionregistrationV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyBinding(_kuber_definitions.Resource):
    """
    ValidatingAdmissionPolicyBinding binds the
    ValidatingAdmissionPolicy with paramerized resources.
    ValidatingAdmissionPolicyBinding and parameter CRDs together
    define how cluster administrators configure policies for
    clusters.

    For a given admission request, each binding will cause its
    policy to be evaluated N times, where N is 1 for
    policies/bindings that don't use params, otherwise N is the
    number of parameters selected by the binding.

    The CEL expressions of a policy must have a computed CEL
    cost below the maximum CEL budget. Each evaluation of the
    policy is given an independent CEL cost budget.
    Adding/removing policies, bindings, or params can not affect
    whether a given (policy, binding, param) combination is
    within its own CEL budget.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["ValidatingAdmissionPolicyBindingSpec"] = None,
    ):
        """Create ValidatingAdmissionPolicyBinding instance."""
        super(ValidatingAdmissionPolicyBinding, self).__init__(
            api_version="admissionregistration/v1beta1",
            kind="ValidatingAdmissionPolicyBinding",
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": (
                spec if spec is not None else ValidatingAdmissionPolicyBindingSpec()
            ),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (ValidatingAdmissionPolicyBindingSpec, None),
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
    def spec(self) -> "ValidatingAdmissionPolicyBindingSpec":
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicyBinding.
        """
        return typing.cast(
            "ValidatingAdmissionPolicyBindingSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["ValidatingAdmissionPolicyBindingSpec", dict]):
        """
        Specification of the desired behavior of the
        ValidatingAdmissionPolicyBinding.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ValidatingAdmissionPolicyBindingSpec,
                ValidatingAdmissionPolicyBindingSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ValidatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_validating_admission_policy_binding",
            "create_validating_admission_policy_binding",
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
        Replaces the ValidatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_validating_admission_policy_binding",
            "replace_validating_admission_policy_binding",
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
        Patches the ValidatingAdmissionPolicyBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "patch_namespaced_validating_admission_policy_binding",
            "patch_validating_admission_policy_binding",
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
        Reads the ValidatingAdmissionPolicyBinding from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_validating_admission_policy_binding",
            "read_validating_admission_policy_binding",
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
        Deletes the ValidatingAdmissionPolicyBinding from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_validating_admission_policy_binding",
            "delete_validating_admission_policy_binding",
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
    ) -> "client.AdmissionregistrationV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicyBinding":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyBindingList(_kuber_definitions.Collection):
    """
    ValidatingAdmissionPolicyBindingList is a list of
    ValidatingAdmissionPolicyBinding.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ValidatingAdmissionPolicyBinding"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ValidatingAdmissionPolicyBindingList instance."""
        super(ValidatingAdmissionPolicyBindingList, self).__init__(
            api_version="admissionregistration/v1beta1",
            kind="ValidatingAdmissionPolicyBindingList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ValidatingAdmissionPolicyBinding),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ValidatingAdmissionPolicyBinding"]:
        """
        List of PolicyBinding.
        """
        return typing.cast(
            typing.List["ValidatingAdmissionPolicyBinding"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["ValidatingAdmissionPolicyBinding"], typing.List[dict]
        ],
    ):
        """
        List of PolicyBinding.
        """
        cleaned: typing.List[ValidatingAdmissionPolicyBinding] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ValidatingAdmissionPolicyBinding,
                    ValidatingAdmissionPolicyBinding().from_dict(item),
                )
            cleaned.append(typing.cast(ValidatingAdmissionPolicyBinding, item))
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.AdmissionregistrationV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicyBindingList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyBindingSpec(_kuber_definitions.Definition):
    """
    ValidatingAdmissionPolicyBindingSpec is the specification of
    the ValidatingAdmissionPolicyBinding.
    """

    def __init__(
        self,
        match_resources: typing.Optional["MatchResources"] = None,
        param_ref: typing.Optional["ParamRef"] = None,
        policy_name: typing.Optional[str] = None,
        validation_actions: typing.Optional[typing.List[str]] = None,
    ):
        """Create ValidatingAdmissionPolicyBindingSpec instance."""
        super(ValidatingAdmissionPolicyBindingSpec, self).__init__(
            api_version="admissionregistration/v1beta1",
            kind="ValidatingAdmissionPolicyBindingSpec",
        )
        self._properties = {
            "matchResources": (
                match_resources if match_resources is not None else MatchResources()
            ),
            "paramRef": param_ref if param_ref is not None else ParamRef(),
            "policyName": policy_name if policy_name is not None else "",
            "validationActions": (
                validation_actions if validation_actions is not None else []
            ),
        }
        self._types = {
            "matchResources": (MatchResources, None),
            "paramRef": (ParamRef, None),
            "policyName": (str, None),
            "validationActions": (list, str),
        }

    @property
    def match_resources(self) -> "MatchResources":
        """
        MatchResources declares what resources match this binding
        and will be validated by it. Note that this is intersected
        with the policy's matchConstraints, so only requests that
        are matched by the policy can be selected by this. If this
        is unset, all resources matched by the policy are validated
        by this binding When resourceRules is unset, it does not
        constrain resource matching. If a resource is matched by the
        other fields of this object, it will be validated. Note that
        this is differs from ValidatingAdmissionPolicy
        matchConstraints, where resourceRules are required.
        """
        return typing.cast(
            "MatchResources",
            self._properties.get("matchResources"),
        )

    @match_resources.setter
    def match_resources(self, value: typing.Union["MatchResources", dict]):
        """
        MatchResources declares what resources match this binding
        and will be validated by it. Note that this is intersected
        with the policy's matchConstraints, so only requests that
        are matched by the policy can be selected by this. If this
        is unset, all resources matched by the policy are validated
        by this binding When resourceRules is unset, it does not
        constrain resource matching. If a resource is matched by the
        other fields of this object, it will be validated. Note that
        this is differs from ValidatingAdmissionPolicy
        matchConstraints, where resourceRules are required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MatchResources,
                MatchResources().from_dict(value),
            )
        self._properties["matchResources"] = value

    @property
    def param_ref(self) -> "ParamRef":
        """
        paramRef specifies the parameter resource used to configure
        the admission control policy. It should point to a resource
        of the type specified in ParamKind of the bound
        ValidatingAdmissionPolicy. If the policy specifies a
        ParamKind and the resource referred to by ParamRef does not
        exist, this binding is considered mis-configured and the
        FailurePolicy of the ValidatingAdmissionPolicy applied. If
        the policy does not specify a ParamKind then this field is
        ignored, and the rules are evaluated without a param.
        """
        return typing.cast(
            "ParamRef",
            self._properties.get("paramRef"),
        )

    @param_ref.setter
    def param_ref(self, value: typing.Union["ParamRef", dict]):
        """
        paramRef specifies the parameter resource used to configure
        the admission control policy. It should point to a resource
        of the type specified in ParamKind of the bound
        ValidatingAdmissionPolicy. If the policy specifies a
        ParamKind and the resource referred to by ParamRef does not
        exist, this binding is considered mis-configured and the
        FailurePolicy of the ValidatingAdmissionPolicy applied. If
        the policy does not specify a ParamKind then this field is
        ignored, and the rules are evaluated without a param.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ParamRef,
                ParamRef().from_dict(value),
            )
        self._properties["paramRef"] = value

    @property
    def policy_name(self) -> str:
        """
        PolicyName references a ValidatingAdmissionPolicy name which
        the ValidatingAdmissionPolicyBinding binds to. If the
        referenced resource does not exist, this binding is
        considered invalid and will be ignored Required.
        """
        return typing.cast(
            str,
            self._properties.get("policyName"),
        )

    @policy_name.setter
    def policy_name(self, value: str):
        """
        PolicyName references a ValidatingAdmissionPolicy name which
        the ValidatingAdmissionPolicyBinding binds to. If the
        referenced resource does not exist, this binding is
        considered invalid and will be ignored Required.
        """
        self._properties["policyName"] = value

    @property
    def validation_actions(self) -> typing.List[str]:
        """
        validationActions declares how Validations of the referenced
        ValidatingAdmissionPolicy are enforced. If a validation
        evaluates to false it is always enforced according to these
        actions.

        Failures defined by the ValidatingAdmissionPolicy's
        FailurePolicy are enforced according to these actions only
        if the FailurePolicy is set to Fail, otherwise the failures
        are ignored. This includes compilation errors, runtime
        errors and misconfigurations of the policy.

        validationActions is declared as a set of action values.
        Order does not matter. validationActions may not contain
        duplicates of the same action.

        The supported actions values are:

        "Deny" specifies that a validation failure results in a
        denied request.

        "Warn" specifies that a validation failure is reported to
        the request client in HTTP Warning headers, with a warning
        code of 299. Warnings can be sent both for allowed or denied
        admission responses.

        "Audit" specifies that a validation failure is included in
        the published audit event for the request. The audit event
        will contain a
        `validation.policy.admission.k8s.io/validation_failure`
        audit annotation with a value containing the details of the
        validation failures, formatted as a JSON list of objects,
        each with the following fields: - message: The validation
        failure message string - policy: The resource name of the
        ValidatingAdmissionPolicy - binding: The resource name of
        the ValidatingAdmissionPolicyBinding - expressionIndex: The
        index of the failed validations in the
        ValidatingAdmissionPolicy - validationActions: The
        enforcement actions enacted for the validation failure
        Example audit annotation:
        `"validation.policy.admission.k8s.io/validation_failure":
        "[{"message": "Invalid value", {"policy":
        "policy.example.com", {"binding":
        "policybinding.example.com", {"expressionIndex": "1",
        {"validationActions": ["Audit"]}]"`

        Clients should expect to handle additional values by
        ignoring any values not recognized.

        "Deny" and "Warn" may not be used together since this
        combination needlessly duplicates the validation failure
        both in the API response body and the HTTP warning headers.

        Required.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("validationActions"),
        )

    @validation_actions.setter
    def validation_actions(self, value: typing.List[str]):
        """
        validationActions declares how Validations of the referenced
        ValidatingAdmissionPolicy are enforced. If a validation
        evaluates to false it is always enforced according to these
        actions.

        Failures defined by the ValidatingAdmissionPolicy's
        FailurePolicy are enforced according to these actions only
        if the FailurePolicy is set to Fail, otherwise the failures
        are ignored. This includes compilation errors, runtime
        errors and misconfigurations of the policy.

        validationActions is declared as a set of action values.
        Order does not matter. validationActions may not contain
        duplicates of the same action.

        The supported actions values are:

        "Deny" specifies that a validation failure results in a
        denied request.

        "Warn" specifies that a validation failure is reported to
        the request client in HTTP Warning headers, with a warning
        code of 299. Warnings can be sent both for allowed or denied
        admission responses.

        "Audit" specifies that a validation failure is included in
        the published audit event for the request. The audit event
        will contain a
        `validation.policy.admission.k8s.io/validation_failure`
        audit annotation with a value containing the details of the
        validation failures, formatted as a JSON list of objects,
        each with the following fields: - message: The validation
        failure message string - policy: The resource name of the
        ValidatingAdmissionPolicy - binding: The resource name of
        the ValidatingAdmissionPolicyBinding - expressionIndex: The
        index of the failed validations in the
        ValidatingAdmissionPolicy - validationActions: The
        enforcement actions enacted for the validation failure
        Example audit annotation:
        `"validation.policy.admission.k8s.io/validation_failure":
        "[{"message": "Invalid value", {"policy":
        "policy.example.com", {"binding":
        "policybinding.example.com", {"expressionIndex": "1",
        {"validationActions": ["Audit"]}]"`

        Clients should expect to handle additional values by
        ignoring any values not recognized.

        "Deny" and "Warn" may not be used together since this
        combination needlessly duplicates the validation failure
        both in the API response body and the HTTP warning headers.

        Required.
        """
        self._properties["validationActions"] = value

    def __enter__(self) -> "ValidatingAdmissionPolicyBindingSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyList(_kuber_definitions.Collection):
    """
    ValidatingAdmissionPolicyList is a list of
    ValidatingAdmissionPolicy.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ValidatingAdmissionPolicy"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ValidatingAdmissionPolicyList instance."""
        super(ValidatingAdmissionPolicyList, self).__init__(
            api_version="admissionregistration/v1beta1",
            kind="ValidatingAdmissionPolicyList",
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ValidatingAdmissionPolicy),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ValidatingAdmissionPolicy"]:
        """
        List of ValidatingAdmissionPolicy.
        """
        return typing.cast(
            typing.List["ValidatingAdmissionPolicy"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self,
        value: typing.Union[
            typing.List["ValidatingAdmissionPolicy"], typing.List[dict]
        ],
    ):
        """
        List of ValidatingAdmissionPolicy.
        """
        cleaned: typing.List[ValidatingAdmissionPolicy] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ValidatingAdmissionPolicy,
                    ValidatingAdmissionPolicy().from_dict(item),
                )
            cleaned.append(typing.cast(ValidatingAdmissionPolicy, item))
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.AdmissionregistrationV1beta1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.AdmissionregistrationV1beta1Api(**kwargs)

    def __enter__(self) -> "ValidatingAdmissionPolicyList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicySpec(_kuber_definitions.Definition):
    """
    ValidatingAdmissionPolicySpec is the specification of the
    desired behavior of the AdmissionPolicy.
    """

    def __init__(
        self,
        audit_annotations: typing.Optional[typing.List["AuditAnnotation"]] = None,
        failure_policy: typing.Optional[str] = None,
        match_conditions: typing.Optional[typing.List["MatchCondition"]] = None,
        match_constraints: typing.Optional["MatchResources"] = None,
        param_kind: typing.Optional["ParamKind"] = None,
        validations: typing.Optional[typing.List["Validation"]] = None,
        variables: typing.Optional[typing.List["Variable"]] = None,
    ):
        """Create ValidatingAdmissionPolicySpec instance."""
        super(ValidatingAdmissionPolicySpec, self).__init__(
            api_version="admissionregistration/v1beta1",
            kind="ValidatingAdmissionPolicySpec",
        )
        self._properties = {
            "auditAnnotations": (
                audit_annotations if audit_annotations is not None else []
            ),
            "failurePolicy": failure_policy if failure_policy is not None else "",
            "matchConditions": match_conditions if match_conditions is not None else [],
            "matchConstraints": (
                match_constraints if match_constraints is not None else MatchResources()
            ),
            "paramKind": param_kind if param_kind is not None else ParamKind(),
            "validations": validations if validations is not None else [],
            "variables": variables if variables is not None else [],
        }
        self._types = {
            "auditAnnotations": (list, AuditAnnotation),
            "failurePolicy": (str, None),
            "matchConditions": (list, MatchCondition),
            "matchConstraints": (MatchResources, None),
            "paramKind": (ParamKind, None),
            "validations": (list, Validation),
            "variables": (list, Variable),
        }

    @property
    def audit_annotations(self) -> typing.List["AuditAnnotation"]:
        """
        auditAnnotations contains CEL expressions which are used to
        produce audit annotations for the audit event of the API
        request. validations and auditAnnotations may not both be
        empty; a least one of validations or auditAnnotations is
        required.
        """
        return typing.cast(
            typing.List["AuditAnnotation"],
            self._properties.get("auditAnnotations"),
        )

    @audit_annotations.setter
    def audit_annotations(
        self, value: typing.Union[typing.List["AuditAnnotation"], typing.List[dict]]
    ):
        """
        auditAnnotations contains CEL expressions which are used to
        produce audit annotations for the audit event of the API
        request. validations and auditAnnotations may not both be
        empty; a least one of validations or auditAnnotations is
        required.
        """
        cleaned: typing.List[AuditAnnotation] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    AuditAnnotation,
                    AuditAnnotation().from_dict(item),
                )
            cleaned.append(typing.cast(AuditAnnotation, item))
        self._properties["auditAnnotations"] = cleaned

    @property
    def failure_policy(self) -> str:
        """
        failurePolicy defines how to handle failures for the
        admission policy. Failures can occur from CEL expression
        parse errors, type check errors, runtime errors and invalid
        or mis-configured policy definitions or bindings.

        A policy is invalid if spec.paramKind refers to a non-
        existent Kind. A binding is invalid if spec.paramRef.name
        refers to a non-existent resource.

        failurePolicy does not define how validations that evaluate
        to false are handled.

        When failurePolicy is set to Fail,
        ValidatingAdmissionPolicyBinding validationActions define
        how failures are enforced.

        Allowed values are Ignore or Fail. Defaults to Fail.
        """
        return typing.cast(
            str,
            self._properties.get("failurePolicy"),
        )

    @failure_policy.setter
    def failure_policy(self, value: str):
        """
        failurePolicy defines how to handle failures for the
        admission policy. Failures can occur from CEL expression
        parse errors, type check errors, runtime errors and invalid
        or mis-configured policy definitions or bindings.

        A policy is invalid if spec.paramKind refers to a non-
        existent Kind. A binding is invalid if spec.paramRef.name
        refers to a non-existent resource.

        failurePolicy does not define how validations that evaluate
        to false are handled.

        When failurePolicy is set to Fail,
        ValidatingAdmissionPolicyBinding validationActions define
        how failures are enforced.

        Allowed values are Ignore or Fail. Defaults to Fail.
        """
        self._properties["failurePolicy"] = value

    @property
    def match_conditions(self) -> typing.List["MatchCondition"]:
        """
        MatchConditions is a list of conditions that must be met for
        a request to be validated. Match conditions filter requests
        that have already been matched by the rules,
        namespaceSelector, and objectSelector. An empty list of
        matchConditions matches all requests. There are a maximum of
        64 match conditions allowed.

        If a parameter object is provided, it can be accessed via
        the `params` handle in the same manner as validation
        expressions.

        The exact matching logic is (in order):
          1. If ANY matchCondition evaluates to FALSE, the policy is
        skipped.
          2. If ALL matchConditions evaluate to TRUE, the policy is
        evaluated.
          3. If any matchCondition evaluates to an error (but none
        are FALSE):
             - If failurePolicy=Fail, reject the request
             - If failurePolicy=Ignore, the policy is skipped
        """
        return typing.cast(
            typing.List["MatchCondition"],
            self._properties.get("matchConditions"),
        )

    @match_conditions.setter
    def match_conditions(
        self, value: typing.Union[typing.List["MatchCondition"], typing.List[dict]]
    ):
        """
        MatchConditions is a list of conditions that must be met for
        a request to be validated. Match conditions filter requests
        that have already been matched by the rules,
        namespaceSelector, and objectSelector. An empty list of
        matchConditions matches all requests. There are a maximum of
        64 match conditions allowed.

        If a parameter object is provided, it can be accessed via
        the `params` handle in the same manner as validation
        expressions.

        The exact matching logic is (in order):
          1. If ANY matchCondition evaluates to FALSE, the policy is
        skipped.
          2. If ALL matchConditions evaluate to TRUE, the policy is
        evaluated.
          3. If any matchCondition evaluates to an error (but none
        are FALSE):
             - If failurePolicy=Fail, reject the request
             - If failurePolicy=Ignore, the policy is skipped
        """
        cleaned: typing.List[MatchCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    MatchCondition,
                    MatchCondition().from_dict(item),
                )
            cleaned.append(typing.cast(MatchCondition, item))
        self._properties["matchConditions"] = cleaned

    @property
    def match_constraints(self) -> "MatchResources":
        """
        MatchConstraints specifies what resources this policy is
        designed to validate. The AdmissionPolicy cares about a
        request if it matches _all_ Constraints. However, in order
        to prevent clusters from being put into an unstable state
        that cannot be recovered from via the API
        ValidatingAdmissionPolicy cannot match
        ValidatingAdmissionPolicy and
        ValidatingAdmissionPolicyBinding. Required.
        """
        return typing.cast(
            "MatchResources",
            self._properties.get("matchConstraints"),
        )

    @match_constraints.setter
    def match_constraints(self, value: typing.Union["MatchResources", dict]):
        """
        MatchConstraints specifies what resources this policy is
        designed to validate. The AdmissionPolicy cares about a
        request if it matches _all_ Constraints. However, in order
        to prevent clusters from being put into an unstable state
        that cannot be recovered from via the API
        ValidatingAdmissionPolicy cannot match
        ValidatingAdmissionPolicy and
        ValidatingAdmissionPolicyBinding. Required.
        """
        if isinstance(value, dict):
            value = typing.cast(
                MatchResources,
                MatchResources().from_dict(value),
            )
        self._properties["matchConstraints"] = value

    @property
    def param_kind(self) -> "ParamKind":
        """
        ParamKind specifies the kind of resources used to
        parameterize this policy. If absent, there are no parameters
        for this policy and the param CEL variable will not be
        provided to validation expressions. If ParamKind refers to a
        non-existent kind, this policy definition is mis-configured
        and the FailurePolicy is applied. If paramKind is specified
        but paramRef is unset in ValidatingAdmissionPolicyBinding,
        the params variable will be null.
        """
        return typing.cast(
            "ParamKind",
            self._properties.get("paramKind"),
        )

    @param_kind.setter
    def param_kind(self, value: typing.Union["ParamKind", dict]):
        """
        ParamKind specifies the kind of resources used to
        parameterize this policy. If absent, there are no parameters
        for this policy and the param CEL variable will not be
        provided to validation expressions. If ParamKind refers to a
        non-existent kind, this policy definition is mis-configured
        and the FailurePolicy is applied. If paramKind is specified
        but paramRef is unset in ValidatingAdmissionPolicyBinding,
        the params variable will be null.
        """
        if isinstance(value, dict):
            value = typing.cast(
                ParamKind,
                ParamKind().from_dict(value),
            )
        self._properties["paramKind"] = value

    @property
    def validations(self) -> typing.List["Validation"]:
        """
        Validations contain CEL expressions which is used to apply
        the validation. Validations and AuditAnnotations may not
        both be empty; a minimum of one Validations or
        AuditAnnotations is required.
        """
        return typing.cast(
            typing.List["Validation"],
            self._properties.get("validations"),
        )

    @validations.setter
    def validations(
        self, value: typing.Union[typing.List["Validation"], typing.List[dict]]
    ):
        """
        Validations contain CEL expressions which is used to apply
        the validation. Validations and AuditAnnotations may not
        both be empty; a minimum of one Validations or
        AuditAnnotations is required.
        """
        cleaned: typing.List[Validation] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Validation,
                    Validation().from_dict(item),
                )
            cleaned.append(typing.cast(Validation, item))
        self._properties["validations"] = cleaned

    @property
    def variables(self) -> typing.List["Variable"]:
        """
        Variables contain definitions of variables that can be used
        in composition of other expressions. Each variable is
        defined as a named CEL expression. The variables defined
        here will be available under `variables` in other
        expressions of the policy except MatchConditions because
        MatchConditions are evaluated before the rest of the policy.

        The expression of a variable can refer to other variables
        defined earlier in the list but not those after. Thus,
        Variables must be sorted by the order of first appearance
        and acyclic.
        """
        return typing.cast(
            typing.List["Variable"],
            self._properties.get("variables"),
        )

    @variables.setter
    def variables(
        self, value: typing.Union[typing.List["Variable"], typing.List[dict]]
    ):
        """
        Variables contain definitions of variables that can be used
        in composition of other expressions. Each variable is
        defined as a named CEL expression. The variables defined
        here will be available under `variables` in other
        expressions of the policy except MatchConditions because
        MatchConditions are evaluated before the rest of the policy.

        The expression of a variable can refer to other variables
        defined earlier in the list but not those after. Thus,
        Variables must be sorted by the order of first appearance
        and acyclic.
        """
        cleaned: typing.List[Variable] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Variable,
                    Variable().from_dict(item),
                )
            cleaned.append(typing.cast(Variable, item))
        self._properties["variables"] = cleaned

    def __enter__(self) -> "ValidatingAdmissionPolicySpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ValidatingAdmissionPolicyStatus(_kuber_definitions.Definition):
    """
    ValidatingAdmissionPolicyStatus represents the status of an
    admission validation policy.
    """

    def __init__(
        self,
        conditions: typing.Optional[typing.List["Condition"]] = None,
        observed_generation: typing.Optional[int] = None,
        type_checking: typing.Optional["TypeChecking"] = None,
    ):
        """Create ValidatingAdmissionPolicyStatus instance."""
        super(ValidatingAdmissionPolicyStatus, self).__init__(
            api_version="admissionregistration/v1beta1",
            kind="ValidatingAdmissionPolicyStatus",
        )
        self._properties = {
            "conditions": conditions if conditions is not None else [],
            "observedGeneration": (
                observed_generation if observed_generation is not None else None
            ),
            "typeChecking": (
                type_checking if type_checking is not None else TypeChecking()
            ),
        }
        self._types = {
            "conditions": (list, Condition),
            "observedGeneration": (int, None),
            "typeChecking": (TypeChecking, None),
        }

    @property
    def conditions(self) -> typing.List["Condition"]:
        """
        The conditions represent the latest available observations
        of a policy's current state.
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
        The conditions represent the latest available observations
        of a policy's current state.
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
    def observed_generation(self) -> int:
        """
        The generation observed by the controller.
        """
        return typing.cast(
            int,
            self._properties.get("observedGeneration"),
        )

    @observed_generation.setter
    def observed_generation(self, value: int):
        """
        The generation observed by the controller.
        """
        self._properties["observedGeneration"] = value

    @property
    def type_checking(self) -> "TypeChecking":
        """
        The results of type checking for each expression. Presence
        of this field indicates the completion of the type checking.
        """
        return typing.cast(
            "TypeChecking",
            self._properties.get("typeChecking"),
        )

    @type_checking.setter
    def type_checking(self, value: typing.Union["TypeChecking", dict]):
        """
        The results of type checking for each expression. Presence
        of this field indicates the completion of the type checking.
        """
        if isinstance(value, dict):
            value = typing.cast(
                TypeChecking,
                TypeChecking().from_dict(value),
            )
        self._properties["typeChecking"] = value

    def __enter__(self) -> "ValidatingAdmissionPolicyStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Validation(_kuber_definitions.Definition):
    """
    Validation specifies the CEL expression which is used to
    apply the validation.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        message_expression: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
    ):
        """Create Validation instance."""
        super(Validation, self).__init__(
            api_version="admissionregistration/v1beta1", kind="Validation"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
            "message": message if message is not None else "",
            "messageExpression": (
                message_expression if message_expression is not None else ""
            ),
            "reason": reason if reason is not None else "",
        }
        self._types = {
            "expression": (str, None),
            "message": (str, None),
            "messageExpression": (str, None),
            "reason": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        Expression represents the expression which will be evaluated
        by CEL. ref: https://github.com/google/cel-spec CEL
        expressions have access to the contents of the API
        request/response, organized into CEL variables as well as
        some other useful variables:

        - 'object' - The object from the incoming request. The value
        is null for DELETE requests. - 'oldObject' - The existing
        object. The value is null for CREATE requests. - 'request' -
        Attributes of the API request([ref](/pkg/apis/admission/type
        s.go#AdmissionRequest)). - 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind. - 'namespaceObject'
        - The namespace object that the incoming object belongs to.
        The value is null for cluster-scoped resources. -
        'variables' - Map of composited variables, from its name to
        its lazily evaluated value.
          For example, a variable named 'foo' can be accessed as
        'variables.foo'.
        - 'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        - 'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.

        The `apiVersion`, `kind`, `metadata.name` and
        `metadata.generateName` are always accessible from the root
        of the object. No other metadata properties are accessible.

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property
        names are escaped according to the following rules when
        accessed in the expression: - '__' escapes to
        '__underscores__' - '.' escapes to '__dot__' - '-' escapes
        to '__dash__' - '/' escapes to '__slash__' - Property names
        that exactly match a CEL RESERVED keyword escape to
        '__{keyword}__'. The keywords are:
                  "true", "false", "null", "in", "as", "break", "const",
        "continue", "else", "for", "function", "if",
                  "import", "let", "loop", "package", "namespace",
        "return".
        Examples:
          - Expression accessing a property named "namespace":
        {"Expression": "object.__namespace__ > 0"}
          - Expression accessing a property named "x-prop":
        {"Expression": "object.x__dash__prop > 0"}
          - Expression accessing a property named "redact__d":
        {"Expression": "object.redact__underscores__d > 0"}

        Equality on arrays with list type of 'set' or 'map' ignores
        element order, i.e. [1, 2] == [2, 1]. Concatenation on
        arrays with x-kubernetes-list-type use the semantics of the
        list type:
          - 'set': `X + Y` performs a union where the array
        positions of all elements in `X` are preserved and
            non-intersecting elements in `Y` are appended, retaining
        their partial order.
          - 'map': `X + Y` performs a merge where the array
        positions of all keys in `X` are preserved but the values
            are overwritten by values in `Y` when the key sets of
        `X` and `Y` intersect. Elements in `Y` with
            non-intersecting keys are appended, retaining their
        partial order.
        Required.
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        Expression represents the expression which will be evaluated
        by CEL. ref: https://github.com/google/cel-spec CEL
        expressions have access to the contents of the API
        request/response, organized into CEL variables as well as
        some other useful variables:

        - 'object' - The object from the incoming request. The value
        is null for DELETE requests. - 'oldObject' - The existing
        object. The value is null for CREATE requests. - 'request' -
        Attributes of the API request([ref](/pkg/apis/admission/type
        s.go#AdmissionRequest)). - 'params' - Parameter resource
        referred to by the policy binding being evaluated. Only
        populated if the policy has a ParamKind. - 'namespaceObject'
        - The namespace object that the incoming object belongs to.
        The value is null for cluster-scoped resources. -
        'variables' - Map of composited variables, from its name to
        its lazily evaluated value.
          For example, a variable named 'foo' can be accessed as
        'variables.foo'.
        - 'authorizer' - A CEL Authorizer. May be used to perform
        authorization checks for the principal (user or service
        account) of the request.
          See
        https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
        - 'authorizer.requestResource' - A CEL ResourceCheck
        constructed from the 'authorizer' and configured with the
          request resource.

        The `apiVersion`, `kind`, `metadata.name` and
        `metadata.generateName` are always accessible from the root
        of the object. No other metadata properties are accessible.

        Only property names of the form `[a-zA-
        Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property
        names are escaped according to the following rules when
        accessed in the expression: - '__' escapes to
        '__underscores__' - '.' escapes to '__dot__' - '-' escapes
        to '__dash__' - '/' escapes to '__slash__' - Property names
        that exactly match a CEL RESERVED keyword escape to
        '__{keyword}__'. The keywords are:
                  "true", "false", "null", "in", "as", "break", "const",
        "continue", "else", "for", "function", "if",
                  "import", "let", "loop", "package", "namespace",
        "return".
        Examples:
          - Expression accessing a property named "namespace":
        {"Expression": "object.__namespace__ > 0"}
          - Expression accessing a property named "x-prop":
        {"Expression": "object.x__dash__prop > 0"}
          - Expression accessing a property named "redact__d":
        {"Expression": "object.redact__underscores__d > 0"}

        Equality on arrays with list type of 'set' or 'map' ignores
        element order, i.e. [1, 2] == [2, 1]. Concatenation on
        arrays with x-kubernetes-list-type use the semantics of the
        list type:
          - 'set': `X + Y` performs a union where the array
        positions of all elements in `X` are preserved and
            non-intersecting elements in `Y` are appended, retaining
        their partial order.
          - 'map': `X + Y` performs a merge where the array
        positions of all keys in `X` are preserved but the values
            are overwritten by values in `Y` when the key sets of
        `X` and `Y` intersect. Elements in `Y` with
            non-intersecting keys are appended, retaining their
        partial order.
        Required.
        """
        self._properties["expression"] = value

    @property
    def message(self) -> str:
        """
        Message represents the message displayed when validation
        fails. The message is required if the Expression contains
        line breaks. The message must not contain line breaks. If
        unset, the message is "failed rule: {Rule}". e.g. "must be a
        URL with the host matching spec.host" If the Expression
        contains line breaks. Message is required. The message must
        not contain line breaks. If unset, the message is "failed
        Expression: {Expression}".
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        Message represents the message displayed when validation
        fails. The message is required if the Expression contains
        line breaks. The message must not contain line breaks. If
        unset, the message is "failed rule: {Rule}". e.g. "must be a
        URL with the host matching spec.host" If the Expression
        contains line breaks. Message is required. The message must
        not contain line breaks. If unset, the message is "failed
        Expression: {Expression}".
        """
        self._properties["message"] = value

    @property
    def message_expression(self) -> str:
        """
        messageExpression declares a CEL expression that evaluates
        to the validation failure message that is returned when this
        rule fails. Since messageExpression is used as a failure
        message, it must evaluate to a string. If both message and
        messageExpression are present on a validation, then
        messageExpression will be used if validation fails. If
        messageExpression results in a runtime error, the runtime
        error is logged, and the validation failure message is
        produced as if the messageExpression field were unset. If
        messageExpression evaluates to an empty string, a string
        with only spaces, or a string that contains line breaks,
        then the validation failure message will also be produced as
        if the messageExpression field were unset, and the fact that
        messageExpression produced an empty string/string with only
        spaces/string with line breaks will be logged.
        messageExpression has access to all the same variables as
        the `expression` except for 'authorizer' and
        'authorizer.requestResource'. Example: "object.x must be
        less than max ("+string(params.max)+")"
        """
        return typing.cast(
            str,
            self._properties.get("messageExpression"),
        )

    @message_expression.setter
    def message_expression(self, value: str):
        """
        messageExpression declares a CEL expression that evaluates
        to the validation failure message that is returned when this
        rule fails. Since messageExpression is used as a failure
        message, it must evaluate to a string. If both message and
        messageExpression are present on a validation, then
        messageExpression will be used if validation fails. If
        messageExpression results in a runtime error, the runtime
        error is logged, and the validation failure message is
        produced as if the messageExpression field were unset. If
        messageExpression evaluates to an empty string, a string
        with only spaces, or a string that contains line breaks,
        then the validation failure message will also be produced as
        if the messageExpression field were unset, and the fact that
        messageExpression produced an empty string/string with only
        spaces/string with line breaks will be logged.
        messageExpression has access to all the same variables as
        the `expression` except for 'authorizer' and
        'authorizer.requestResource'. Example: "object.x must be
        less than max ("+string(params.max)+")"
        """
        self._properties["messageExpression"] = value

    @property
    def reason(self) -> str:
        """
        Reason represents a machine-readable description of why this
        validation failed. If this is the first validation in the
        list to fail, this reason, as well as the corresponding HTTP
        response code, are used in the HTTP response to the client.
        The currently supported reasons are: "Unauthorized",
        "Forbidden", "Invalid", "RequestEntityTooLarge". If not set,
        StatusReasonInvalid is used in the response to the client.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        Reason represents a machine-readable description of why this
        validation failed. If this is the first validation in the
        list to fail, this reason, as well as the corresponding HTTP
        response code, are used in the HTTP response to the client.
        The currently supported reasons are: "Unauthorized",
        "Forbidden", "Invalid", "RequestEntityTooLarge". If not set,
        StatusReasonInvalid is used in the response to the client.
        """
        self._properties["reason"] = value

    def __enter__(self) -> "Validation":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Variable(_kuber_definitions.Definition):
    """
    Variable is the definition of a variable that is used for
    composition. A variable is defined as a named expression.
    """

    def __init__(
        self,
        expression: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ):
        """Create Variable instance."""
        super(Variable, self).__init__(
            api_version="admissionregistration/v1beta1", kind="Variable"
        )
        self._properties = {
            "expression": expression if expression is not None else "",
            "name": name if name is not None else "",
        }
        self._types = {
            "expression": (str, None),
            "name": (str, None),
        }

    @property
    def expression(self) -> str:
        """
        Expression is the expression that will be evaluated as the
        value of the variable. The CEL expression has access to the
        same identifiers as the CEL expressions in Validation.
        """
        return typing.cast(
            str,
            self._properties.get("expression"),
        )

    @expression.setter
    def expression(self, value: str):
        """
        Expression is the expression that will be evaluated as the
        value of the variable. The CEL expression has access to the
        same identifiers as the CEL expressions in Validation.
        """
        self._properties["expression"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of the variable. The name must be a valid
        CEL identifier and unique among all variables. The variable
        can be accessed in other expressions through `variables` For
        example, if name is "foo", the variable will be available as
        `variables.foo`
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of the variable. The name must be a valid
        CEL identifier and unique among all variables. The variable
        can be accessed in other expressions through `variables` For
        example, if name is "foo", the variable will be available as
        `variables.foo`
        """
        self._properties["name"] = value

    def __enter__(self) -> "Variable":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
