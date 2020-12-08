import typing
import datetime as _datetime

from kubernetes import client
from kuber import kube_api as _kube_api

from kuber import definitions as _kuber_definitions
from kuber.v1_21.core_v1 import Container
from kuber.v1_21.core_v1 import ContainerPort
from kuber.v1_21.core_v1 import EnvFromSource
from kuber.v1_21.core_v1 import EnvVar
from kuber.v1_21.batch_v1 import JobSpec
from kuber.v1_21.core_v1 import Lifecycle
from kuber.v1_21.meta_v1 import ListMeta
from kuber.v1_21.meta_v1 import ObjectMeta
from kuber.v1_21.core_v1 import ObjectReference
from kuber.v1_21.core_v1 import Probe
from kuber.v1_21.core_v1 import ResourceRequirements
from kuber.v1_21.core_v1 import SecurityContext
from kuber.v1_21.meta_v1 import Status
from kuber.v1_21.meta_v1 import StatusDetails
from kuber.v1_21.core_v1 import VolumeDevice
from kuber.v1_21.core_v1 import VolumeMount


class CronJob(_kuber_definitions.Resource):
    """
    CronJob represents the configuration of a single cron job.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "CronJobSpec" = None,
        status: "CronJobStatus" = None,
    ):
        """Create CronJob instance."""
        super(CronJob, self).__init__(api_version="batch/v2alpha1", kind="CronJob")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else CronJobSpec(),
            "status": status if status is not None else CronJobStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (CronJobSpec, None),
            "status": (CronJobStatus, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata. More info:
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
        Standard object's metadata. More info:
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
    def spec(self) -> "CronJobSpec":
        """
        Specification of the desired behavior of a cron job,
        including the schedule. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "CronJobSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["CronJobSpec", dict]):
        """
        Specification of the desired behavior of a cron job,
        including the schedule. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                CronJobSpec,
                CronJobSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "CronJobStatus":
        """
        Current status of a cron job. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "CronJobStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["CronJobStatus", dict]):
        """
        Current status of a cron job. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                CronJobStatus,
                CronJobStatus().from_dict(value),
            )
        self._properties["status"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "CronJob":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.spec.job_template.spec.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next(
            (
                c
                for c in self.spec.job_template.spec.template.spec.containers
                if c.name == name
            ),
            None,
        )

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.spec.job_template.spec.template.spec.containers

    def create_resource(self, namespace: "str" = None) -> "CronJobStatus":
        """
        Creates the CronJob in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_cron_job", "create_cron_job"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = CronJobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: "str" = None) -> "CronJobStatus":
        """
        Replaces the CronJob in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_cron_job", "replace_cron_job"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CronJobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: "str" = None) -> "CronJobStatus":
        """
        Patches the CronJob in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_cron_job", "patch_cron_job"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = CronJobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(self, namespace: "str" = None) -> "CronJobStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = ["read_namespaced_cron_job", "read_cron_job"]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = CronJobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: str = None):
        """
        Reads the CronJob from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_cron_job",
            "read_cron_job",
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
        Deletes the CronJob from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_cron_job",
            "delete_cron_job",
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
    ) -> "client.BatchV2alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.BatchV2alpha1Api(**kwargs)

    def __enter__(self) -> "CronJob":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CronJobList(_kuber_definitions.Collection):
    """
    CronJobList is a collection of cron jobs.
    """

    def __init__(
        self,
        items: typing.List["CronJob"] = None,
        metadata: "ListMeta" = None,
    ):
        """Create CronJobList instance."""
        super(CronJobList, self).__init__(
            api_version="batch/v2alpha1", kind="CronJobList"
        )
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, CronJob),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["CronJob"]:
        """
        items is the list of CronJobs.
        """
        return typing.cast(
            typing.List["CronJob"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["CronJob"], typing.List[dict]]):
        """
        items is the list of CronJobs.
        """
        cleaned: typing.List[CronJob] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    CronJob,
                    CronJob().from_dict(item),
                )
            cleaned.append(typing.cast(CronJob, item))
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
    ) -> "client.BatchV2alpha1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.BatchV2alpha1Api(**kwargs)

    def __enter__(self) -> "CronJobList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CronJobSpec(_kuber_definitions.Definition):
    """
    CronJobSpec describes how the job execution will look like
    and when it will actually run.
    """

    def __init__(
        self,
        concurrency_policy: str = None,
        failed_jobs_history_limit: int = None,
        job_template: "JobTemplateSpec" = None,
        schedule: str = None,
        starting_deadline_seconds: int = None,
        successful_jobs_history_limit: int = None,
        suspend: bool = None,
    ):
        """Create CronJobSpec instance."""
        super(CronJobSpec, self).__init__(
            api_version="batch/v2alpha1", kind="CronJobSpec"
        )
        self._properties = {
            "concurrencyPolicy": concurrency_policy
            if concurrency_policy is not None
            else "",
            "failedJobsHistoryLimit": failed_jobs_history_limit
            if failed_jobs_history_limit is not None
            else None,
            "jobTemplate": job_template
            if job_template is not None
            else JobTemplateSpec(),
            "schedule": schedule if schedule is not None else "",
            "startingDeadlineSeconds": starting_deadline_seconds
            if starting_deadline_seconds is not None
            else None,
            "successfulJobsHistoryLimit": successful_jobs_history_limit
            if successful_jobs_history_limit is not None
            else None,
            "suspend": suspend if suspend is not None else None,
        }
        self._types = {
            "concurrencyPolicy": (str, None),
            "failedJobsHistoryLimit": (int, None),
            "jobTemplate": (JobTemplateSpec, None),
            "schedule": (str, None),
            "startingDeadlineSeconds": (int, None),
            "successfulJobsHistoryLimit": (int, None),
            "suspend": (bool, None),
        }

    @property
    def concurrency_policy(self) -> str:
        """
        Specifies how to treat concurrent executions of a Job. Valid
        values are: - "Allow" (default): allows CronJobs to run
        concurrently; - "Forbid": forbids concurrent runs, skipping
        next run if previous run hasn't finished yet; - "Replace":
        cancels currently running job and replaces it with a new one
        """
        return typing.cast(
            str,
            self._properties.get("concurrencyPolicy"),
        )

    @concurrency_policy.setter
    def concurrency_policy(self, value: str):
        """
        Specifies how to treat concurrent executions of a Job. Valid
        values are: - "Allow" (default): allows CronJobs to run
        concurrently; - "Forbid": forbids concurrent runs, skipping
        next run if previous run hasn't finished yet; - "Replace":
        cancels currently running job and replaces it with a new one
        """
        self._properties["concurrencyPolicy"] = value

    @property
    def failed_jobs_history_limit(self) -> int:
        """
        The number of failed finished jobs to retain. This is a
        pointer to distinguish between explicit zero and not
        specified.
        """
        return typing.cast(
            int,
            self._properties.get("failedJobsHistoryLimit"),
        )

    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, value: int):
        """
        The number of failed finished jobs to retain. This is a
        pointer to distinguish between explicit zero and not
        specified.
        """
        self._properties["failedJobsHistoryLimit"] = value

    @property
    def job_template(self) -> "JobTemplateSpec":
        """
        Specifies the job that will be created when executing a
        CronJob.
        """
        return typing.cast(
            "JobTemplateSpec",
            self._properties.get("jobTemplate"),
        )

    @job_template.setter
    def job_template(self, value: typing.Union["JobTemplateSpec", dict]):
        """
        Specifies the job that will be created when executing a
        CronJob.
        """
        if isinstance(value, dict):
            value = typing.cast(
                JobTemplateSpec,
                JobTemplateSpec().from_dict(value),
            )
        self._properties["jobTemplate"] = value

    @property
    def schedule(self) -> str:
        """
        The schedule in Cron format, see
        https://en.wikipedia.org/wiki/Cron.
        """
        return typing.cast(
            str,
            self._properties.get("schedule"),
        )

    @schedule.setter
    def schedule(self, value: str):
        """
        The schedule in Cron format, see
        https://en.wikipedia.org/wiki/Cron.
        """
        self._properties["schedule"] = value

    @property
    def starting_deadline_seconds(self) -> int:
        """
        Optional deadline in seconds for starting the job if it
        misses scheduled time for any reason.  Missed jobs
        executions will be counted as failed ones.
        """
        return typing.cast(
            int,
            self._properties.get("startingDeadlineSeconds"),
        )

    @starting_deadline_seconds.setter
    def starting_deadline_seconds(self, value: int):
        """
        Optional deadline in seconds for starting the job if it
        misses scheduled time for any reason.  Missed jobs
        executions will be counted as failed ones.
        """
        self._properties["startingDeadlineSeconds"] = value

    @property
    def successful_jobs_history_limit(self) -> int:
        """
        The number of successful finished jobs to retain. This is a
        pointer to distinguish between explicit zero and not
        specified.
        """
        return typing.cast(
            int,
            self._properties.get("successfulJobsHistoryLimit"),
        )

    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, value: int):
        """
        The number of successful finished jobs to retain. This is a
        pointer to distinguish between explicit zero and not
        specified.
        """
        self._properties["successfulJobsHistoryLimit"] = value

    @property
    def suspend(self) -> bool:
        """
        This flag tells the controller to suspend subsequent
        executions, it does not apply to already started executions.
        Defaults to false.
        """
        return typing.cast(
            bool,
            self._properties.get("suspend"),
        )

    @suspend.setter
    def suspend(self, value: bool):
        """
        This flag tells the controller to suspend subsequent
        executions, it does not apply to already started executions.
        Defaults to false.
        """
        self._properties["suspend"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "CronJobSpec":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.job_template.spec.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next(
            (
                c
                for c in self.job_template.spec.template.spec.containers
                if c.name == name
            ),
            None,
        )

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.job_template.spec.template.spec.containers

    def __enter__(self) -> "CronJobSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class CronJobStatus(_kuber_definitions.Definition):
    """
    CronJobStatus represents the current state of a cron job.
    """

    def __init__(
        self,
        active: typing.List["ObjectReference"] = None,
        last_schedule_time: str = None,
    ):
        """Create CronJobStatus instance."""
        super(CronJobStatus, self).__init__(
            api_version="batch/v2alpha1", kind="CronJobStatus"
        )
        self._properties = {
            "active": active if active is not None else [],
            "lastScheduleTime": last_schedule_time
            if last_schedule_time is not None
            else None,
        }
        self._types = {
            "active": (list, ObjectReference),
            "lastScheduleTime": (str, None),
        }

    @property
    def active(self) -> typing.List["ObjectReference"]:
        """
        A list of pointers to currently running jobs.
        """
        return typing.cast(
            typing.List["ObjectReference"],
            self._properties.get("active"),
        )

    @active.setter
    def active(
        self, value: typing.Union[typing.List["ObjectReference"], typing.List[dict]]
    ):
        """
        A list of pointers to currently running jobs.
        """
        cleaned: typing.List[ObjectReference] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    ObjectReference,
                    ObjectReference().from_dict(item),
                )
            cleaned.append(typing.cast(ObjectReference, item))
        self._properties["active"] = cleaned

    @property
    def last_schedule_time(self) -> str:
        """
        Information when was the last time the job was successfully
        scheduled.
        """
        return typing.cast(
            str,
            self._properties.get("lastScheduleTime"),
        )

    @last_schedule_time.setter
    def last_schedule_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Information when was the last time the job was successfully
        scheduled.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastScheduleTime"] = value

    def __enter__(self) -> "CronJobStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobTemplateSpec(_kuber_definitions.Definition):
    """
    JobTemplateSpec describes the data a Job should have when
    created from a template
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "JobSpec" = None,
    ):
        """Create JobTemplateSpec instance."""
        super(JobTemplateSpec, self).__init__(
            api_version="batch/v2alpha1", kind="JobTemplateSpec"
        )
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else JobSpec(),
        }
        self._types = {
            "metadata": (ObjectMeta, None),
            "spec": (JobSpec, None),
        }

    @property
    def metadata(self) -> "ObjectMeta":
        """
        Standard object's metadata of the jobs created from this
        template. More info:
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
        Standard object's metadata of the jobs created from this
        template. More info:
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
    def spec(self) -> "JobSpec":
        """
        Specification of the desired behavior of the job. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "JobSpec",
            self._properties.get("spec"),
        )

    @spec.setter
    def spec(self, value: typing.Union["JobSpec", dict]):
        """
        Specification of the desired behavior of the job. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                JobSpec,
                JobSpec().from_dict(value),
            )
        self._properties["spec"] = value

    def append_container(
        self,
        args: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        command: typing.Union[
            typing.List[str],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env: typing.Union[
            typing.List["EnvVar"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        env_from: typing.Union[
            typing.List["EnvFromSource"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        image_pull_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        lifecycle: typing.Union[
            "Lifecycle",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        liveness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        name: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        ports: typing.Union[
            typing.List["ContainerPort"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        readiness_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        security_context: typing.Union[
            "SecurityContext",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        startup_probe: typing.Union[
            "Probe",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        stdin_once: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_path: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        termination_message_policy: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        tty: typing.Union[
            bool,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_devices: typing.Union[
            typing.List["VolumeDevice"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        volume_mounts: typing.Union[
            typing.List["VolumeMount"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        working_dir: typing.Union[
            str,
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
    ) -> "JobTemplateSpec":
        """Adds a container object within the specified resource."""
        values: typing.Dict[str, typing.Any] = {
            "args": args,
            "command": command,
            "env": env,
            "env_from": env_from,
            "image": image,
            "image_pull_policy": image_pull_policy,
            "lifecycle": lifecycle,
            "liveness_probe": liveness_probe,
            "name": name,
            "ports": ports,
            "readiness_probe": readiness_probe,
            "resources": resources,
            "security_context": security_context,
            "startup_probe": startup_probe,
            "stdin": stdin,
            "stdin_once": stdin_once,
            "termination_message_path": termination_message_path,
            "termination_message_policy": termination_message_policy,
            "tty": tty,
            "volume_devices": volume_devices,
            "volume_mounts": volume_mounts,
            "working_dir": working_dir,
        }
        self.spec.template.spec.containers.append(
            Container(
                **{
                    k: v
                    for k, v in values.items()
                    if v != _kuber_definitions.UNCHANGED_VALUE
                }
            )
        )
        return self

    def get_container(self, name: str) -> typing.Optional["Container"]:
        """
        Fetch a container definition within this resource by name if such a
        container definition exists. Return None if no container definition
        by that name exists.
        """
        return next(
            (c for c in self.spec.template.spec.containers if c.name == name), None
        )

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.spec.template.spec.containers

    def __enter__(self) -> "JobTemplateSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
