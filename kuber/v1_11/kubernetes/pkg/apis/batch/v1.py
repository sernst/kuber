import typing


from kuber import definitions as _kuber_definitions


class Job(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v1.Job instead.
    """

    def __init__(
            self,
    ):
        """Create Job instance."""
        super(Job, self).__init__(
            api_version='batch/v1',
            kind='Job'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'Job':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobCondition(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v1.JobCondition
    instead.
    """

    def __init__(
            self,
    ):
        """Create JobCondition instance."""
        super(JobCondition, self).__init__(
            api_version='batch/v1',
            kind='JobCondition'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'JobCondition':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobList(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v1.JobList instead.
    """

    def __init__(
            self,
    ):
        """Create JobList instance."""
        super(JobList, self).__init__(
            api_version='batch/v1',
            kind='JobList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'JobList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v1.JobSpec instead.
    """

    def __init__(
            self,
    ):
        """Create JobSpec instance."""
        super(JobSpec, self).__init__(
            api_version='batch/v1',
            kind='JobSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'JobSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v1.JobStatus
    instead.
    """

    def __init__(
            self,
    ):
        """Create JobStatus instance."""
        super(JobStatus, self).__init__(
            api_version='batch/v1',
            kind='JobStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'JobStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
