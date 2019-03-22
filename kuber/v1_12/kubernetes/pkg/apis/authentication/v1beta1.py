import typing


from kuber import definitions as _kuber_definitions


class TokenReview(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authentication.v1beta1.TokenReview instead.
    """

    def __init__(
            self,
    ):
        """Create TokenReview instance."""
        super(TokenReview, self).__init__(
            api_version='authentication/v1beta1',
            kind='TokenReview'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'TokenReview':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenReviewSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authentication.v1beta1.TokenReviewSpec instead.
    """

    def __init__(
            self,
    ):
        """Create TokenReviewSpec instance."""
        super(TokenReviewSpec, self).__init__(
            api_version='authentication/v1beta1',
            kind='TokenReviewSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'TokenReviewSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class TokenReviewStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authentication.v1beta1.TokenReviewStatus instead.
    """

    def __init__(
            self,
    ):
        """Create TokenReviewStatus instance."""
        super(TokenReviewStatus, self).__init__(
            api_version='authentication/v1beta1',
            kind='TokenReviewStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'TokenReviewStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class UserInfo(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.authentication.v1beta1.UserInfo instead.
    """

    def __init__(
            self,
    ):
        """Create UserInfo instance."""
        super(UserInfo, self).__init__(
            api_version='authentication/v1beta1',
            kind='UserInfo'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'UserInfo':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
