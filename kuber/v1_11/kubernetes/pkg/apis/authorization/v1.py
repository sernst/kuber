import typing


from kuber import definitions as _kuber_definitions


class LocalSubjectAccessReview(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.LocalSubjectAccessReview
    instead.
    """

    def __init__(
            self,
    ):
        """Create LocalSubjectAccessReview instance."""
        super(LocalSubjectAccessReview, self).__init__(
            api_version='authorization/v1',
            kind='LocalSubjectAccessReview'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'LocalSubjectAccessReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class NonResourceAttributes(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.NonResourceAttributes instead.
    """

    def __init__(
            self,
    ):
        """Create NonResourceAttributes instance."""
        super(NonResourceAttributes, self).__init__(
            api_version='authorization/v1',
            kind='NonResourceAttributes'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'NonResourceAttributes':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ResourceAttributes(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.ResourceAttributes instead.
    """

    def __init__(
            self,
    ):
        """Create ResourceAttributes instance."""
        super(ResourceAttributes, self).__init__(
            api_version='authorization/v1',
            kind='ResourceAttributes'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'ResourceAttributes':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SelfSubjectAccessReview(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.SelfSubjectAccessReview instead.
    """

    def __init__(
            self,
    ):
        """Create SelfSubjectAccessReview instance."""
        super(SelfSubjectAccessReview, self).__init__(
            api_version='authorization/v1',
            kind='SelfSubjectAccessReview'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'SelfSubjectAccessReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SelfSubjectAccessReviewSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.SelfSubjectAccessReviewSpec
    instead.
    """

    def __init__(
            self,
    ):
        """Create SelfSubjectAccessReviewSpec instance."""
        super(SelfSubjectAccessReviewSpec, self).__init__(
            api_version='authorization/v1',
            kind='SelfSubjectAccessReviewSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'SelfSubjectAccessReviewSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SubjectAccessReview(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.SubjectAccessReview instead.
    """

    def __init__(
            self,
    ):
        """Create SubjectAccessReview instance."""
        super(SubjectAccessReview, self).__init__(
            api_version='authorization/v1',
            kind='SubjectAccessReview'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'SubjectAccessReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SubjectAccessReviewSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.SubjectAccessReviewSpec instead.
    """

    def __init__(
            self,
    ):
        """Create SubjectAccessReviewSpec instance."""
        super(SubjectAccessReviewSpec, self).__init__(
            api_version='authorization/v1',
            kind='SubjectAccessReviewSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'SubjectAccessReviewSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class SubjectAccessReviewStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authorization.v1.SubjectAccessReviewStatus
    instead.
    """

    def __init__(
            self,
    ):
        """Create SubjectAccessReviewStatus instance."""
        super(SubjectAccessReviewStatus, self).__init__(
            api_version='authorization/v1',
            kind='SubjectAccessReviewStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'SubjectAccessReviewStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
