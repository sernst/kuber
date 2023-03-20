import typing  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.latest.meta_v1 import LabelSelector  # noqa: F401
from kuber.latest.meta_v1 import ListMeta  # noqa: F401
from kuber.latest.meta_v1 import ObjectMeta  # noqa: F401


class AggregationRule(_kuber_definitions.Definition):
    """
    AggregationRule describes how to locate ClusterRoles to
    aggregate into the ClusterRole
    """

    def __init__(
        self,
        cluster_role_selectors: typing.Optional[typing.List["LabelSelector"]] = None,
    ):
        """Create AggregationRule instance."""
        super(AggregationRule, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="AggregationRule"
        )
        self._properties = {
            "clusterRoleSelectors": cluster_role_selectors
            if cluster_role_selectors is not None
            else [],
        }
        self._types = {
            "clusterRoleSelectors": (list, LabelSelector),
        }

    @property
    def cluster_role_selectors(self) -> typing.List["LabelSelector"]:
        """
        ClusterRoleSelectors holds a list of selectors which will be
        used to find ClusterRoles and create the rules. If any of
        the selectors match, then the ClusterRole's permissions will
        be added
        """
        return typing.cast(
            typing.List["LabelSelector"],
            self._properties.get("clusterRoleSelectors"),
        )

    @cluster_role_selectors.setter
    def cluster_role_selectors(
        self, value: typing.Union[typing.List["LabelSelector"], typing.List[dict]]
    ):
        """
        ClusterRoleSelectors holds a list of selectors which will be
        used to find ClusterRoles and create the rules. If any of
        the selectors match, then the ClusterRole's permissions will
        be added
        """
        cleaned: typing.List[LabelSelector] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    LabelSelector,
                    LabelSelector().from_dict(item),
                )
            cleaned.append(typing.cast(LabelSelector, item))
        self._properties["clusterRoleSelectors"] = cleaned

    def __enter__(self) -> "AggregationRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterRole(_kuber_definitions.Resource):
    """
    ClusterRole is a cluster level, logical grouping of
    PolicyRules that can be referenced as a unit by a
    RoleBinding or ClusterRoleBinding.
    """

    def __init__(
        self,
        aggregation_rule: typing.Optional["AggregationRule"] = None,
        metadata: typing.Optional["ObjectMeta"] = None,
        rules: typing.Optional[typing.List["PolicyRule"]] = None,
    ):
        """Create ClusterRole instance."""
        super(ClusterRole, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="ClusterRole"
        )
        self._properties = {
            "aggregationRule": aggregation_rule
            if aggregation_rule is not None
            else AggregationRule(),
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "rules": rules if rules is not None else [],
        }
        self._types = {
            "aggregationRule": (AggregationRule, None),
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "rules": (list, PolicyRule),
        }

    @property
    def aggregation_rule(self) -> "AggregationRule":
        """
        AggregationRule is an optional field that describes how to
        build the Rules for this ClusterRole. If AggregationRule is
        set, then the Rules are controller managed and direct
        changes to Rules will be stomped by the controller.
        """
        return typing.cast(
            "AggregationRule",
            self._properties.get("aggregationRule"),
        )

    @aggregation_rule.setter
    def aggregation_rule(self, value: typing.Union["AggregationRule", dict]):
        """
        AggregationRule is an optional field that describes how to
        build the Rules for this ClusterRole. If AggregationRule is
        set, then the Rules are controller managed and direct
        changes to Rules will be stomped by the controller.
        """
        if isinstance(value, dict):
            value = typing.cast(
                AggregationRule,
                AggregationRule().from_dict(value),
            )
        self._properties["aggregationRule"] = value

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
    def rules(self) -> typing.List["PolicyRule"]:
        """
        Rules holds all the PolicyRules for this ClusterRole
        """
        return typing.cast(
            typing.List["PolicyRule"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(self, value: typing.Union[typing.List["PolicyRule"], typing.List[dict]]):
        """
        Rules holds all the PolicyRules for this ClusterRole
        """
        cleaned: typing.List[PolicyRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PolicyRule,
                    PolicyRule().from_dict(item),
                )
            cleaned.append(typing.cast(PolicyRule, item))
        self._properties["rules"] = cleaned

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ClusterRole in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_cluster_role", "create_cluster_role"]

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
        Replaces the ClusterRole in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_cluster_role", "replace_cluster_role"]

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
        Patches the ClusterRole in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_cluster_role", "patch_cluster_role"]

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
        Reads the ClusterRole from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_cluster_role",
            "read_cluster_role",
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
        Deletes the ClusterRole from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_cluster_role",
            "delete_cluster_role",
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "ClusterRole":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterRoleBinding(_kuber_definitions.Resource):
    """
    ClusterRoleBinding references a ClusterRole, but not contain
    it.  It can reference a ClusterRole in the global namespace,
    and adds who information via Subject.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        role_ref: typing.Optional["RoleRef"] = None,
        subjects: typing.Optional[typing.List["Subject"]] = None,
    ):
        """Create ClusterRoleBinding instance."""
        super(ClusterRoleBinding, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="ClusterRoleBinding"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "roleRef": role_ref if role_ref is not None else RoleRef(),
            "subjects": subjects if subjects is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "roleRef": (RoleRef, None),
            "subjects": (list, Subject),
        }

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
    def role_ref(self) -> "RoleRef":
        """
        RoleRef can only reference a ClusterRole in the global
        namespace. If the RoleRef cannot be resolved, the Authorizer
        must return an error.
        """
        return typing.cast(
            "RoleRef",
            self._properties.get("roleRef"),
        )

    @role_ref.setter
    def role_ref(self, value: typing.Union["RoleRef", dict]):
        """
        RoleRef can only reference a ClusterRole in the global
        namespace. If the RoleRef cannot be resolved, the Authorizer
        must return an error.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RoleRef,
                RoleRef().from_dict(value),
            )
        self._properties["roleRef"] = value

    @property
    def subjects(self) -> typing.List["Subject"]:
        """
        Subjects holds references to the objects the role applies
        to.
        """
        return typing.cast(
            typing.List["Subject"],
            self._properties.get("subjects"),
        )

    @subjects.setter
    def subjects(self, value: typing.Union[typing.List["Subject"], typing.List[dict]]):
        """
        Subjects holds references to the objects the role applies
        to.
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

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the ClusterRoleBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "create_namespaced_cluster_role_binding",
            "create_cluster_role_binding",
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
        Replaces the ClusterRoleBinding in the currently
        configured Kubernetes cluster.
        """
        names = [
            "replace_namespaced_cluster_role_binding",
            "replace_cluster_role_binding",
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
        Patches the ClusterRoleBinding in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_cluster_role_binding", "patch_cluster_role_binding"]

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
        Reads the ClusterRoleBinding from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_cluster_role_binding",
            "read_cluster_role_binding",
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
        Deletes the ClusterRoleBinding from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_cluster_role_binding",
            "delete_cluster_role_binding",
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "ClusterRoleBinding":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterRoleBindingList(_kuber_definitions.Collection):
    """
    ClusterRoleBindingList is a collection of
    ClusterRoleBindings
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ClusterRoleBinding"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ClusterRoleBindingList instance."""
        super(ClusterRoleBindingList, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="ClusterRoleBindingList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ClusterRoleBinding),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ClusterRoleBinding"]:
        """
        Items is a list of ClusterRoleBindings
        """
        return typing.cast(
            typing.List["ClusterRoleBinding"],
            self._properties.get("items"),
        )

    @items.setter
    def items(
        self, value: typing.Union[typing.List["ClusterRoleBinding"], typing.List[dict]]
    ):
        """
        Items is a list of ClusterRoleBindings
        """
        cleaned: typing.List[ClusterRoleBinding] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ClusterRoleBinding,
                    ClusterRoleBinding().from_dict(item),
                )
            cleaned.append(typing.cast(ClusterRoleBinding, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard object's metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard object's metadata.
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "ClusterRoleBindingList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterRoleList(_kuber_definitions.Collection):
    """
    ClusterRoleList is a collection of ClusterRoles
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["ClusterRole"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create ClusterRoleList instance."""
        super(ClusterRoleList, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="ClusterRoleList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, ClusterRole),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["ClusterRole"]:
        """
        Items is a list of ClusterRoles
        """
        return typing.cast(
            typing.List["ClusterRole"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["ClusterRole"], typing.List[dict]]):
        """
        Items is a list of ClusterRoles
        """
        cleaned: typing.List[ClusterRole] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ClusterRole,
                    ClusterRole().from_dict(item),
                )
            cleaned.append(typing.cast(ClusterRole, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard object's metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard object's metadata.
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "ClusterRoleList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PolicyRule(_kuber_definitions.Definition):
    """
    PolicyRule holds information that describes a policy rule,
    but does not contain information about who the rule applies
    to or which namespace the rule applies to.
    """

    def __init__(
        self,
        api_groups: typing.Optional[typing.List[str]] = None,
        non_resource_urls: typing.Optional[typing.List[str]] = None,
        resource_names: typing.Optional[typing.List[str]] = None,
        resources: typing.Optional[typing.List[str]] = None,
        verbs: typing.Optional[typing.List[str]] = None,
    ):
        """Create PolicyRule instance."""
        super(PolicyRule, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="PolicyRule"
        )
        self._properties = {
            "apiGroups": api_groups if api_groups is not None else [],
            "nonResourceURLs": non_resource_urls
            if non_resource_urls is not None
            else [],
            "resourceNames": resource_names if resource_names is not None else [],
            "resources": resources if resources is not None else [],
            "verbs": verbs if verbs is not None else [],
        }
        self._types = {
            "apiGroups": (list, str),
            "nonResourceURLs": (list, str),
            "resourceNames": (list, str),
            "resources": (list, str),
            "verbs": (list, str),
        }

    @property
    def api_groups(self) -> typing.List[str]:
        """
        APIGroups is the name of the APIGroup that contains the
        resources.  If multiple API groups are specified, any action
        requested against one of the enumerated resources in any API
        group will be allowed. "" represents the core API group and
        "*" represents all API groups.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("apiGroups"),
        )

    @api_groups.setter
    def api_groups(self, value: typing.List[str]):
        """
        APIGroups is the name of the APIGroup that contains the
        resources.  If multiple API groups are specified, any action
        requested against one of the enumerated resources in any API
        group will be allowed. "" represents the core API group and
        "*" represents all API groups.
        """
        self._properties["apiGroups"] = value

    @property
    def non_resource_urls(self) -> typing.List[str]:
        """
        NonResourceURLs is a set of partial urls that a user should
        have access to.  *s are allowed, but only as the full, final
        step in the path Since non-resource URLs are not namespaced,
        this field is only applicable for ClusterRoles referenced
        from a ClusterRoleBinding. Rules can either apply to API
        resources (such as "pods" or "secrets") or non-resource URL
        paths (such as "/api"),  but not both.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("nonResourceURLs"),
        )

    @non_resource_urls.setter
    def non_resource_urls(self, value: typing.List[str]):
        """
        NonResourceURLs is a set of partial urls that a user should
        have access to.  *s are allowed, but only as the full, final
        step in the path Since non-resource URLs are not namespaced,
        this field is only applicable for ClusterRoles referenced
        from a ClusterRoleBinding. Rules can either apply to API
        resources (such as "pods" or "secrets") or non-resource URL
        paths (such as "/api"),  but not both.
        """
        self._properties["nonResourceURLs"] = value

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
        Resources is a list of resources this rule applies to. '*'
        represents all resources.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("resources"),
        )

    @resources.setter
    def resources(self, value: typing.List[str]):
        """
        Resources is a list of resources this rule applies to. '*'
        represents all resources.
        """
        self._properties["resources"] = value

    @property
    def verbs(self) -> typing.List[str]:
        """
        Verbs is a list of Verbs that apply to ALL the ResourceKinds
        contained in this rule. '*' represents all verbs.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("verbs"),
        )

    @verbs.setter
    def verbs(self, value: typing.List[str]):
        """
        Verbs is a list of Verbs that apply to ALL the ResourceKinds
        contained in this rule. '*' represents all verbs.
        """
        self._properties["verbs"] = value

    def __enter__(self) -> "PolicyRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Role(_kuber_definitions.Resource):
    """
    Role is a namespaced, logical grouping of PolicyRules that
    can be referenced as a unit by a RoleBinding.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        rules: typing.Optional[typing.List["PolicyRule"]] = None,
    ):
        """Create Role instance."""
        super(Role, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="Role"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "rules": rules if rules is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "rules": (list, PolicyRule),
        }

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
    def rules(self) -> typing.List["PolicyRule"]:
        """
        Rules holds all the PolicyRules for this Role
        """
        return typing.cast(
            typing.List["PolicyRule"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(self, value: typing.Union[typing.List["PolicyRule"], typing.List[dict]]):
        """
        Rules holds all the PolicyRules for this Role
        """
        cleaned: typing.List[PolicyRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PolicyRule,
                    PolicyRule().from_dict(item),
                )
            cleaned.append(typing.cast(PolicyRule, item))
        self._properties["rules"] = cleaned

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the Role in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_role", "create_role"]

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
        Replaces the Role in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_role", "replace_role"]

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
        Patches the Role in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_role", "patch_role"]

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
        Reads the Role from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_role",
            "read_role",
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
        Deletes the Role from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_role",
            "delete_role",
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "Role":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleBinding(_kuber_definitions.Resource):
    """
    RoleBinding references a role, but does not contain it.  It
    can reference a Role in the same namespace or a ClusterRole
    in the global namespace. It adds who information via
    Subjects and namespace information by which namespace it
    exists in.  RoleBindings in a given namespace only have
    effect in that namespace.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        role_ref: typing.Optional["RoleRef"] = None,
        subjects: typing.Optional[typing.List["Subject"]] = None,
    ):
        """Create RoleBinding instance."""
        super(RoleBinding, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="RoleBinding"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "roleRef": role_ref if role_ref is not None else RoleRef(),
            "subjects": subjects if subjects is not None else [],
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "roleRef": (RoleRef, None),
            "subjects": (list, Subject),
        }

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
    def role_ref(self) -> "RoleRef":
        """
        RoleRef can reference a Role in the current namespace or a
        ClusterRole in the global namespace. If the RoleRef cannot
        be resolved, the Authorizer must return an error.
        """
        return typing.cast(
            "RoleRef",
            self._properties.get("roleRef"),
        )

    @role_ref.setter
    def role_ref(self, value: typing.Union["RoleRef", dict]):
        """
        RoleRef can reference a Role in the current namespace or a
        ClusterRole in the global namespace. If the RoleRef cannot
        be resolved, the Authorizer must return an error.
        """
        if isinstance(value, dict):
            value = typing.cast(
                RoleRef,
                RoleRef().from_dict(value),
            )
        self._properties["roleRef"] = value

    @property
    def subjects(self) -> typing.List["Subject"]:
        """
        Subjects holds references to the objects the role applies
        to.
        """
        return typing.cast(
            typing.List["Subject"],
            self._properties.get("subjects"),
        )

    @subjects.setter
    def subjects(self, value: typing.Union[typing.List["Subject"], typing.List[dict]]):
        """
        Subjects holds references to the objects the role applies
        to.
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

    def create_resource(self, namespace: typing.Optional["str"] = None):
        """
        Creates the RoleBinding in the currently
        configured Kubernetes cluster.
        """
        names = ["create_namespaced_role_binding", "create_role_binding"]

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
        Replaces the RoleBinding in the currently
        configured Kubernetes cluster.
        """
        names = ["replace_namespaced_role_binding", "replace_role_binding"]

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
        Patches the RoleBinding in the currently
        configured Kubernetes cluster.
        """
        names = ["patch_namespaced_role_binding", "patch_role_binding"]

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
        Reads the RoleBinding from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_role_binding",
            "read_role_binding",
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
        Deletes the RoleBinding from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_role_binding",
            "delete_role_binding",
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "RoleBinding":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleBindingList(_kuber_definitions.Collection):
    """
    RoleBindingList is a collection of RoleBindings
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["RoleBinding"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create RoleBindingList instance."""
        super(RoleBindingList, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="RoleBindingList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, RoleBinding),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["RoleBinding"]:
        """
        Items is a list of RoleBindings
        """
        return typing.cast(
            typing.List["RoleBinding"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["RoleBinding"], typing.List[dict]]):
        """
        Items is a list of RoleBindings
        """
        cleaned: typing.List[RoleBinding] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    RoleBinding,
                    RoleBinding().from_dict(item),
                )
            cleaned.append(typing.cast(RoleBinding, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard object's metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard object's metadata.
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "RoleBindingList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleList(_kuber_definitions.Collection):
    """
    RoleList is a collection of Roles
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["Role"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create RoleList instance."""
        super(RoleList, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="RoleList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, Role),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["Role"]:
        """
        Items is a list of Roles
        """
        return typing.cast(
            typing.List["Role"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["Role"], typing.List[dict]]):
        """
        Items is a list of Roles
        """
        cleaned: typing.List[Role] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Role,
                    Role().from_dict(item),
                )
            cleaned.append(typing.cast(Role, item))
        self._properties["items"] = cleaned

    @property
    def metadata(self) -> "ListMeta":
        """
        Standard object's metadata.
        """
        return typing.cast(
            "ListMeta",
            self._properties.get("metadata"),
        )

    @metadata.setter
    def metadata(self, value: typing.Union["ListMeta", dict]):
        """
        Standard object's metadata.
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
    ) -> "client.RbacAuthorizationV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.RbacAuthorizationV1Api(**kwargs)

    def __enter__(self) -> "RoleList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleRef(_kuber_definitions.Definition):
    """
    RoleRef contains information that points to the role being
    used
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
    ):
        """Create RoleRef instance."""
        super(RoleRef, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="RoleRef"
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
        APIGroup is the group for the resource being referenced
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup is the group for the resource being referenced
        """
        self._properties["apiGroup"] = value

    @property
    def kind(self) -> str:
        """
        Kind is the type of resource being referenced
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind is the type of resource being referenced
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name is the name of resource being referenced
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name is the name of resource being referenced
        """
        self._properties["name"] = value

    def __enter__(self) -> "RoleRef":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Subject(_kuber_definitions.Definition):
    """
    Subject contains a reference to the object or user
    identities a role binding applies to.  This can either hold
    a direct API object reference, or a value for non-objects
    such as user and group names.
    """

    def __init__(
        self,
        api_group: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        namespace: typing.Optional[str] = None,
    ):
        """Create Subject instance."""
        super(Subject, self).__init__(
            api_version="rbac.authorization.k8s.io/v1", kind="Subject"
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
        APIGroup holds the API group of the referenced subject.
        Defaults to "" for ServiceAccount subjects. Defaults to
        "rbac.authorization.k8s.io" for User and Group subjects.
        """
        return typing.cast(
            str,
            self._properties.get("apiGroup"),
        )

    @api_group.setter
    def api_group(self, value: str):
        """
        APIGroup holds the API group of the referenced subject.
        Defaults to "" for ServiceAccount subjects. Defaults to
        "rbac.authorization.k8s.io" for User and Group subjects.
        """
        self._properties["apiGroup"] = value

    @property
    def kind(self) -> str:
        """
        Kind of object being referenced. Values defined by this API
        group are "User", "Group", and "ServiceAccount". If the
        Authorizer does not recognized the kind value, the
        Authorizer should report an error.
        """
        return typing.cast(
            str,
            self._properties.get("kind"),
        )

    @kind.setter
    def kind(self, value: str):
        """
        Kind of object being referenced. Values defined by this API
        group are "User", "Group", and "ServiceAccount". If the
        Authorizer does not recognized the kind value, the
        Authorizer should report an error.
        """
        self._properties["kind"] = value

    @property
    def name(self) -> str:
        """
        Name of the object being referenced.
        """
        return typing.cast(
            str,
            self._properties.get("name"),
        )

    @name.setter
    def name(self, value: str):
        """
        Name of the object being referenced.
        """
        self._properties["name"] = value

    @property
    def namespace(self) -> str:
        """
        Namespace of the referenced object.  If the object kind is
        non-namespace, such as "User" or "Group", and this value is
        not empty the Authorizer should report an error.
        """
        return typing.cast(
            str,
            self._properties.get("namespace"),
        )

    @namespace.setter
    def namespace(self, value: str):
        """
        Namespace of the referenced object.  If the object kind is
        non-namespace, such as "User" or "Group", and this value is
        not empty the Authorizer should report an error.
        """
        self._properties["namespace"] = value

    def __enter__(self) -> "Subject":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
