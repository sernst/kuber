import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class CronJob(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v2alpha1.CronJob
    instead.
    """

    def __init__(
            self,
    ):
        """Create CronJob instance."""
        super(CronJob, self).__init__(
            api_version='batch/v2alpha1',
            kind='CronJob'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CronJob':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CronJobList(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v2alpha1.CronJobList
    instead.
    """

    def __init__(
            self,
    ):
        """Create CronJobList instance."""
        super(CronJobList, self).__init__(
            api_version='batch/v2alpha1',
            kind='CronJobList'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CronJobList':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CronJobSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use io.k8s.api.batch.v2alpha1.CronJobSpec
    instead.
    """

    def __init__(
            self,
    ):
        """Create CronJobSpec instance."""
        super(CronJobSpec, self).__init__(
            api_version='batch/v2alpha1',
            kind='CronJobSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CronJobSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CronJobStatus(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.batch.v2alpha1.CronJobStatus instead.
    """

    def __init__(
            self,
    ):
        """Create CronJobStatus instance."""
        super(CronJobStatus, self).__init__(
            api_version='batch/v2alpha1',
            kind='CronJobStatus'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'CronJobStatus':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobTemplateSpec(_kuber_definitions.Definition):
    """
    Deprecated. Please use
    io.k8s.api.batch.v2alpha1.JobTemplateSpec instead.
    """

    def __init__(
            self,
    ):
        """Create JobTemplateSpec instance."""
        super(JobTemplateSpec, self).__init__(
            api_version='batch/v2alpha1',
            kind='JobTemplateSpec'
        )
        self._properties = {

        }
        self._types = {

        }

    def __enter__(self) -> 'JobTemplateSpec':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
