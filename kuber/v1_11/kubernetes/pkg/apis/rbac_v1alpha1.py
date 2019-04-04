import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class ClusterRole(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.rbac.v1alpha1.ClusterRole
    instead.
    """

    def __init__(
            self,
    ):
        """Create ClusterRole instance."""
        super(ClusterRole, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='ClusterRole'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ClusterRole':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterRoleBinding(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.rbac.v1alpha1.ClusterRoleBinding instead.
    """

    def __init__(
            self,
    ):
        """Create ClusterRoleBinding instance."""
        super(ClusterRoleBinding, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='ClusterRoleBinding'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ClusterRoleBinding':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterRoleBindingList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.rbac.v1alpha1.ClusterRoleBindingList instead.
    """

    def __init__(
            self,
    ):
        """Create ClusterRoleBindingList instance."""
        super(ClusterRoleBindingList, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='ClusterRoleBindingList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ClusterRoleBindingList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ClusterRoleList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.rbac.v1alpha1.ClusterRoleList instead.
    """

    def __init__(
            self,
    ):
        """Create ClusterRoleList instance."""
        super(ClusterRoleList, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='ClusterRoleList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ClusterRoleList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PolicyRule(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.rbac.v1alpha1.PolicyRule
    instead.
    """

    def __init__(
            self,
    ):
        """Create PolicyRule instance."""
        super(PolicyRule, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='PolicyRule'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'PolicyRule':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Role(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.rbac.v1alpha1.Role
    instead.
    """

    def __init__(
            self,
    ):
        """Create Role instance."""
        super(Role, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='Role'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Role':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleBinding(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.rbac.v1alpha1.RoleBinding
    instead.
    """

    def __init__(
            self,
    ):
        """Create RoleBinding instance."""
        super(RoleBinding, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='RoleBinding'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RoleBinding':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleBindingList(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.rbac.v1alpha1.RoleBindingList instead.
    """

    def __init__(
            self,
    ):
        """Create RoleBindingList instance."""
        super(RoleBindingList, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='RoleBindingList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RoleBindingList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleList(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.rbac.v1alpha1.RoleList
    instead.
    """

    def __init__(
            self,
    ):
        """Create RoleList instance."""
        super(RoleList, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='RoleList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RoleList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class RoleRef(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.rbac.v1alpha1.RoleRef
    instead.
    """

    def __init__(
            self,
    ):
        """Create RoleRef instance."""
        super(RoleRef, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='RoleRef'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'RoleRef':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Subject(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.rbac.v1alpha1.Subject
    instead.
    """

    def __init__(
            self,
    ):
        """Create Subject instance."""
        super(Subject, self).__init__(
            api_version='rbac.authorization.k8s.io/v1alpha1',
            kind='Subject'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Subject':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
