import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_28.core_v1 import Container  # noqa: F401
from kuber.v1_28.core_v1 import ContainerPort  # noqa: F401
from kuber.v1_28.core_v1 import ContainerResizePolicy  # noqa: F401
from kuber.v1_28.core_v1 import EnvFromSource  # noqa: F401
from kuber.v1_28.core_v1 import EnvVar  # noqa: F401
from kuber.v1_28.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_28.core_v1 import Lifecycle  # noqa: F401
from kuber.v1_28.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_28.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_28.core_v1 import ObjectReference  # noqa: F401
from kuber.v1_28.core_v1 import PodTemplateSpec  # noqa: F401
from kuber.v1_28.core_v1 import Probe  # noqa: F401
from kuber.v1_28.core_v1 import ResourceRequirements  # noqa: F401
from kuber.v1_28.core_v1 import SecurityContext  # noqa: F401
from kuber.v1_28.meta_v1 import Status  # noqa: F401
from kuber.v1_28.meta_v1 import StatusDetails  # noqa: F401
from kuber.v1_28.core_v1 import VolumeDevice  # noqa: F401
from kuber.v1_28.core_v1 import VolumeMount  # noqa: F401


class CronJob(_kuber_definitions.Resource):
    """
    CronJob represents the configuration of a single cron job.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["CronJobSpec"] = None,
        status: typing.Optional["CronJobStatus"] = None,
    ):
        """Create CronJob instance."""
        super(CronJob, self).__init__(api_version="batch/v1", kind="CronJob")
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
        resize_policy: typing.Union[
            typing.List["ContainerResizePolicy"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        restart_policy: typing.Union[
            str,
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
            "resize_policy": resize_policy,
            "resources": resources,
            "restart_policy": restart_policy,
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

    def create_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "CronJobStatus":
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

    def replace_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "CronJobStatus":
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

    def patch_resource(
        self, namespace: typing.Optional["str"] = None
    ) -> "CronJobStatus":
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

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "CronJobStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_cron_job",
            "read_cron_job",
        ]

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

    def read_resource(self, namespace: typing.Optional[str] = None):
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
        namespace: typing.Optional[str] = None,
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.BatchV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.BatchV1Api(**kwargs)

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
        items: typing.Optional[typing.List["CronJob"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create CronJobList instance."""
        super(CronJobList, self).__init__(api_version="batch/v1", kind="CronJobList")
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.BatchV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.BatchV1Api(**kwargs)

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
        concurrency_policy: typing.Optional[str] = None,
        failed_jobs_history_limit: typing.Optional[int] = None,
        job_template: typing.Optional["JobTemplateSpec"] = None,
        schedule: typing.Optional[str] = None,
        starting_deadline_seconds: typing.Optional[int] = None,
        successful_jobs_history_limit: typing.Optional[int] = None,
        suspend: typing.Optional[bool] = None,
        time_zone: typing.Optional[str] = None,
    ):
        """Create CronJobSpec instance."""
        super(CronJobSpec, self).__init__(api_version="batch/v1", kind="CronJobSpec")
        self._properties = {
            "concurrencyPolicy": (
                concurrency_policy if concurrency_policy is not None else ""
            ),
            "failedJobsHistoryLimit": (
                failed_jobs_history_limit
                if failed_jobs_history_limit is not None
                else None
            ),
            "jobTemplate": (
                job_template if job_template is not None else JobTemplateSpec()
            ),
            "schedule": schedule if schedule is not None else "",
            "startingDeadlineSeconds": (
                starting_deadline_seconds
                if starting_deadline_seconds is not None
                else None
            ),
            "successfulJobsHistoryLimit": (
                successful_jobs_history_limit
                if successful_jobs_history_limit is not None
                else None
            ),
            "suspend": suspend if suspend is not None else None,
            "timeZone": time_zone if time_zone is not None else "",
        }
        self._types = {
            "concurrencyPolicy": (str, None),
            "failedJobsHistoryLimit": (int, None),
            "jobTemplate": (JobTemplateSpec, None),
            "schedule": (str, None),
            "startingDeadlineSeconds": (int, None),
            "successfulJobsHistoryLimit": (int, None),
            "suspend": (bool, None),
            "timeZone": (str, None),
        }

    @property
    def concurrency_policy(self) -> str:
        """
        Specifies how to treat concurrent executions of a Job. Valid
        values are:

        - "Allow" (default): allows CronJobs to run concurrently; -
        "Forbid": forbids concurrent runs, skipping next run if
        previous run hasn't finished yet; - "Replace": cancels
        currently running job and replaces it with a new one
        """
        return typing.cast(
            str,
            self._properties.get("concurrencyPolicy"),
        )

    @concurrency_policy.setter
    def concurrency_policy(self, value: str):
        """
        Specifies how to treat concurrent executions of a Job. Valid
        values are:

        - "Allow" (default): allows CronJobs to run concurrently; -
        "Forbid": forbids concurrent runs, skipping next run if
        previous run hasn't finished yet; - "Replace": cancels
        currently running job and replaces it with a new one
        """
        self._properties["concurrencyPolicy"] = value

    @property
    def failed_jobs_history_limit(self) -> int:
        """
        The number of failed finished jobs to retain. Value must be
        non-negative integer. Defaults to 1.
        """
        return typing.cast(
            int,
            self._properties.get("failedJobsHistoryLimit"),
        )

    @failed_jobs_history_limit.setter
    def failed_jobs_history_limit(self, value: int):
        """
        The number of failed finished jobs to retain. Value must be
        non-negative integer. Defaults to 1.
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
        The number of successful finished jobs to retain. Value must
        be non-negative integer. Defaults to 3.
        """
        return typing.cast(
            int,
            self._properties.get("successfulJobsHistoryLimit"),
        )

    @successful_jobs_history_limit.setter
    def successful_jobs_history_limit(self, value: int):
        """
        The number of successful finished jobs to retain. Value must
        be non-negative integer. Defaults to 3.
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

    @property
    def time_zone(self) -> str:
        """
        The time zone name for the given schedule, see https://en.wi
        kipedia.org/wiki/List_of_tz_database_time_zones. If not
        specified, this will default to the time zone of the kube-
        controller-manager process. The set of valid time zone names
        and the time zone offset is loaded from the system-wide time
        zone database by the API server during CronJob validation
        and the controller manager during execution. If no system-
        wide time zone database can be found a bundled version of
        the database is used instead. If the time zone name becomes
        invalid during the lifetime of a CronJob or due to a change
        in host configuration, the controller will stop creating new
        new Jobs and will create a system event with the reason
        UnknownTimeZone. More information can be found in https://ku
        bernetes.io/docs/concepts/workloads/controllers/cron-
        jobs/#time-zones
        """
        return typing.cast(
            str,
            self._properties.get("timeZone"),
        )

    @time_zone.setter
    def time_zone(self, value: str):
        """
        The time zone name for the given schedule, see https://en.wi
        kipedia.org/wiki/List_of_tz_database_time_zones. If not
        specified, this will default to the time zone of the kube-
        controller-manager process. The set of valid time zone names
        and the time zone offset is loaded from the system-wide time
        zone database by the API server during CronJob validation
        and the controller manager during execution. If no system-
        wide time zone database can be found a bundled version of
        the database is used instead. If the time zone name becomes
        invalid during the lifetime of a CronJob or due to a change
        in host configuration, the controller will stop creating new
        new Jobs and will create a system event with the reason
        UnknownTimeZone. More information can be found in https://ku
        bernetes.io/docs/concepts/workloads/controllers/cron-
        jobs/#time-zones
        """
        self._properties["timeZone"] = value

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
        resize_policy: typing.Union[
            typing.List["ContainerResizePolicy"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        restart_policy: typing.Union[
            str,
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
            "resize_policy": resize_policy,
            "resources": resources,
            "restart_policy": restart_policy,
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
        active: typing.Optional[typing.List["ObjectReference"]] = None,
        last_schedule_time: typing.Optional[str] = None,
        last_successful_time: typing.Optional[str] = None,
    ):
        """Create CronJobStatus instance."""
        super(CronJobStatus, self).__init__(
            api_version="batch/v1", kind="CronJobStatus"
        )
        self._properties = {
            "active": active if active is not None else [],
            "lastScheduleTime": (
                last_schedule_time if last_schedule_time is not None else None
            ),
            "lastSuccessfulTime": (
                last_successful_time if last_successful_time is not None else None
            ),
        }
        self._types = {
            "active": (list, ObjectReference),
            "lastScheduleTime": (str, None),
            "lastSuccessfulTime": (str, None),
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

    @property
    def last_successful_time(self) -> str:
        """
        Information when was the last time the job successfully
        completed.
        """
        return typing.cast(
            str,
            self._properties.get("lastSuccessfulTime"),
        )

    @last_successful_time.setter
    def last_successful_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Information when was the last time the job successfully
        completed.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastSuccessfulTime"] = value

    def __enter__(self) -> "CronJobStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Job(_kuber_definitions.Resource):
    """
    Job represents the configuration of a single job.
    """

    def __init__(
        self,
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["JobSpec"] = None,
        status: typing.Optional["JobStatus"] = None,
    ):
        """Create Job instance."""
        super(Job, self).__init__(api_version="batch/v1", kind="Job")
        self._properties = {
            "metadata": metadata if metadata is not None else ObjectMeta(),
            "spec": spec if spec is not None else JobSpec(),
            "status": status if status is not None else JobStatus(),
        }
        self._types = {
            "apiVersion": (str, None),
            "kind": (str, None),
            "metadata": (ObjectMeta, None),
            "spec": (JobSpec, None),
            "status": (JobStatus, None),
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
    def spec(self) -> "JobSpec":
        """
        Specification of the desired behavior of a job. More info:
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
        Specification of the desired behavior of a job. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                JobSpec,
                JobSpec().from_dict(value),
            )
        self._properties["spec"] = value

    @property
    def status(self) -> "JobStatus":
        """
        Current status of a job. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        return typing.cast(
            "JobStatus",
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: typing.Union["JobStatus", dict]):
        """
        Current status of a job. More info:
        https://git.k8s.io/community/contributors/devel/sig-
        architecture/api-conventions.md#spec-and-status
        """
        if isinstance(value, dict):
            value = typing.cast(
                JobStatus,
                JobStatus().from_dict(value),
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
        resize_policy: typing.Union[
            typing.List["ContainerResizePolicy"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        restart_policy: typing.Union[
            str,
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
    ) -> "Job":
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
            "resize_policy": resize_policy,
            "resources": resources,
            "restart_policy": restart_policy,
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

    def create_resource(self, namespace: typing.Optional["str"] = None) -> "JobStatus":
        """
        Creates the Job in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the create is complete.
        """
        names = ["create_namespaced_job", "create_job"]

        response = _kube_api.execute(
            action="create",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict()},
        )

        output = JobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def replace_resource(self, namespace: typing.Optional["str"] = None) -> "JobStatus":
        """
        Replaces the Job in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["replace_namespaced_job", "replace_job"]

        response = _kube_api.execute(
            action="replace",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = JobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def patch_resource(self, namespace: typing.Optional["str"] = None) -> "JobStatus":
        """
        Patches the Job in the currently
        configured Kubernetes cluster and returns the status information
        returned by the Kubernetes API after the replace is complete.
        """
        names = ["patch_namespaced_job", "patch_job"]

        response = _kube_api.execute(
            action="patch",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"body": self.to_dict(), "name": self.metadata.name},
        )

        output = JobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def get_resource_status(
        self, namespace: typing.Optional["str"] = None
    ) -> "JobStatus":
        """
        Returns status information about the given resource within the cluster.
        """
        names = [
            "read_namespaced_job",
            "read_job",
        ]

        response = _kube_api.execute(
            action="read",
            resource=self,
            names=names,
            namespace=namespace,
            api_client=None,
            api_args={"name": self.metadata.name},
        )

        output = JobStatus()
        if response is not None:
            output.from_dict(_kube_api.to_kuber_dict(response.status))
        return output

    def read_resource(self, namespace: typing.Optional[str] = None):
        """
        Reads the Job from the currently configured
        Kubernetes cluster and returns the low-level definition object.
        """
        names = [
            "read_namespaced_job",
            "read_job",
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
        Deletes the Job from the currently configured
        Kubernetes cluster.
        """
        names = [
            "delete_namespaced_job",
            "delete_job",
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
    ) -> "client.BatchV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.BatchV1Api(**kwargs)

    def __enter__(self) -> "Job":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobCondition(_kuber_definitions.Definition):
    """
    JobCondition describes current state of a job.
    """

    def __init__(
        self,
        last_probe_time: typing.Optional[str] = None,
        last_transition_time: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create JobCondition instance."""
        super(JobCondition, self).__init__(api_version="batch/v1", kind="JobCondition")
        self._properties = {
            "lastProbeTime": last_probe_time if last_probe_time is not None else None,
            "lastTransitionTime": (
                last_transition_time if last_transition_time is not None else None
            ),
            "message": message if message is not None else "",
            "reason": reason if reason is not None else "",
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "lastProbeTime": (str, None),
            "lastTransitionTime": (str, None),
            "message": (str, None),
            "reason": (str, None),
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def last_probe_time(self) -> str:
        """
        Last time the condition was checked.
        """
        return typing.cast(
            str,
            self._properties.get("lastProbeTime"),
        )

    @last_probe_time.setter
    def last_probe_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Last time the condition was checked.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastProbeTime"] = value

    @property
    def last_transition_time(self) -> str:
        """
        Last time the condition transit from one status to another.
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
        Last time the condition transit from one status to another.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["lastTransitionTime"] = value

    @property
    def message(self) -> str:
        """
        Human readable message indicating details about last
        transition.
        """
        return typing.cast(
            str,
            self._properties.get("message"),
        )

    @message.setter
    def message(self, value: str):
        """
        Human readable message indicating details about last
        transition.
        """
        self._properties["message"] = value

    @property
    def reason(self) -> str:
        """
        (brief) reason for the condition's last transition.
        """
        return typing.cast(
            str,
            self._properties.get("reason"),
        )

    @reason.setter
    def reason(self, value: str):
        """
        (brief) reason for the condition's last transition.
        """
        self._properties["reason"] = value

    @property
    def status(self) -> str:
        """
        Status of the condition, one of True, False, Unknown.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Status of the condition, one of True, False, Unknown.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        Type of job condition, Complete or Failed.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Type of job condition, Complete or Failed.
        """
        self._properties["type"] = value

    def __enter__(self) -> "JobCondition":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobList(_kuber_definitions.Collection):
    """
    JobList is a collection of jobs.
    """

    def __init__(
        self,
        items: typing.Optional[typing.List["Job"]] = None,
        metadata: typing.Optional["ListMeta"] = None,
    ):
        """Create JobList instance."""
        super(JobList, self).__init__(api_version="batch/v1", kind="JobList")
        self._properties = {
            "items": items if items is not None else [],
            "metadata": metadata if metadata is not None else ListMeta(),
        }
        self._types = {
            "apiVersion": (str, None),
            "items": (list, Job),
            "kind": (str, None),
            "metadata": (ListMeta, None),
        }

    @property
    def items(self) -> typing.List["Job"]:
        """
        items is the list of Jobs.
        """
        return typing.cast(
            typing.List["Job"],
            self._properties.get("items"),
        )

    @items.setter
    def items(self, value: typing.Union[typing.List["Job"], typing.List[dict]]):
        """
        items is the list of Jobs.
        """
        cleaned: typing.List[Job] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    Job,
                    Job().from_dict(item),
                )
            cleaned.append(typing.cast(Job, item))
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
        api_client: typing.Optional[client.ApiClient] = None, **kwargs
    ) -> "client.BatchV1Api":
        """
        Returns an instance of the kubernetes API client associated with
        this object.
        """
        if api_client:
            kwargs["apl_client"] = api_client
        return client.BatchV1Api(**kwargs)

    def __enter__(self) -> "JobList":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobSpec(_kuber_definitions.Definition):
    """
    JobSpec describes how the job execution will look like.
    """

    def __init__(
        self,
        active_deadline_seconds: typing.Optional[int] = None,
        backoff_limit: typing.Optional[int] = None,
        backoff_limit_per_index: typing.Optional[int] = None,
        completion_mode: typing.Optional[str] = None,
        completions: typing.Optional[int] = None,
        manual_selector: typing.Optional[bool] = None,
        max_failed_indexes: typing.Optional[int] = None,
        parallelism: typing.Optional[int] = None,
        pod_failure_policy: typing.Optional["PodFailurePolicy"] = None,
        pod_replacement_policy: typing.Optional[str] = None,
        selector: typing.Optional["LabelSelector"] = None,
        suspend: typing.Optional[bool] = None,
        template: typing.Optional["PodTemplateSpec"] = None,
        ttl_seconds_after_finished: typing.Optional[int] = None,
    ):
        """Create JobSpec instance."""
        super(JobSpec, self).__init__(api_version="batch/v1", kind="JobSpec")
        self._properties = {
            "activeDeadlineSeconds": (
                active_deadline_seconds if active_deadline_seconds is not None else None
            ),
            "backoffLimit": backoff_limit if backoff_limit is not None else None,
            "backoffLimitPerIndex": (
                backoff_limit_per_index if backoff_limit_per_index is not None else None
            ),
            "completionMode": completion_mode if completion_mode is not None else "",
            "completions": completions if completions is not None else None,
            "manualSelector": manual_selector if manual_selector is not None else None,
            "maxFailedIndexes": (
                max_failed_indexes if max_failed_indexes is not None else None
            ),
            "parallelism": parallelism if parallelism is not None else None,
            "podFailurePolicy": (
                pod_failure_policy
                if pod_failure_policy is not None
                else PodFailurePolicy()
            ),
            "podReplacementPolicy": (
                pod_replacement_policy if pod_replacement_policy is not None else ""
            ),
            "selector": selector if selector is not None else LabelSelector(),
            "suspend": suspend if suspend is not None else None,
            "template": template if template is not None else PodTemplateSpec(),
            "ttlSecondsAfterFinished": (
                ttl_seconds_after_finished
                if ttl_seconds_after_finished is not None
                else None
            ),
        }
        self._types = {
            "activeDeadlineSeconds": (int, None),
            "backoffLimit": (int, None),
            "backoffLimitPerIndex": (int, None),
            "completionMode": (str, None),
            "completions": (int, None),
            "manualSelector": (bool, None),
            "maxFailedIndexes": (int, None),
            "parallelism": (int, None),
            "podFailurePolicy": (PodFailurePolicy, None),
            "podReplacementPolicy": (str, None),
            "selector": (LabelSelector, None),
            "suspend": (bool, None),
            "template": (PodTemplateSpec, None),
            "ttlSecondsAfterFinished": (int, None),
        }

    @property
    def active_deadline_seconds(self) -> int:
        """
        Specifies the duration in seconds relative to the startTime
        that the job may be continuously active before the system
        tries to terminate it; value must be positive integer. If a
        Job is suspended (at creation or through an update), this
        timer will effectively be stopped and reset when the Job is
        resumed again.
        """
        return typing.cast(
            int,
            self._properties.get("activeDeadlineSeconds"),
        )

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, value: int):
        """
        Specifies the duration in seconds relative to the startTime
        that the job may be continuously active before the system
        tries to terminate it; value must be positive integer. If a
        Job is suspended (at creation or through an update), this
        timer will effectively be stopped and reset when the Job is
        resumed again.
        """
        self._properties["activeDeadlineSeconds"] = value

    @property
    def backoff_limit(self) -> int:
        """
        Specifies the number of retries before marking this job
        failed. Defaults to 6
        """
        return typing.cast(
            int,
            self._properties.get("backoffLimit"),
        )

    @backoff_limit.setter
    def backoff_limit(self, value: int):
        """
        Specifies the number of retries before marking this job
        failed. Defaults to 6
        """
        self._properties["backoffLimit"] = value

    @property
    def backoff_limit_per_index(self) -> int:
        """
        Specifies the limit for the number of retries within an
        index before marking this index as failed. When enabled the
        number of failures per index is kept in the pod's
        batch.kubernetes.io/job-index-failure-count annotation. It
        can only be set when Job's completionMode=Indexed, and the
        Pod's restart policy is Never. The field is immutable. This
        field is alpha-level. It can be used when the
        `JobBackoffLimitPerIndex` feature gate is enabled (disabled
        by default).
        """
        return typing.cast(
            int,
            self._properties.get("backoffLimitPerIndex"),
        )

    @backoff_limit_per_index.setter
    def backoff_limit_per_index(self, value: int):
        """
        Specifies the limit for the number of retries within an
        index before marking this index as failed. When enabled the
        number of failures per index is kept in the pod's
        batch.kubernetes.io/job-index-failure-count annotation. It
        can only be set when Job's completionMode=Indexed, and the
        Pod's restart policy is Never. The field is immutable. This
        field is alpha-level. It can be used when the
        `JobBackoffLimitPerIndex` feature gate is enabled (disabled
        by default).
        """
        self._properties["backoffLimitPerIndex"] = value

    @property
    def completion_mode(self) -> str:
        """
        completionMode specifies how Pod completions are tracked. It
        can be `NonIndexed` (default) or `Indexed`.

        `NonIndexed` means that the Job is considered complete when
        there have been .spec.completions successfully completed
        Pods. Each Pod completion is homologous to each other.

        `Indexed` means that the Pods of a Job get an associated
        completion index from 0 to (.spec.completions - 1),
        available in the annotation batch.kubernetes.io/job-
        completion-index. The Job is considered complete when there
        is one successfully completed Pod for each index. When value
        is `Indexed`, .spec.completions must be specified and
        `.spec.parallelism` must be less than or equal to 10^5. In
        addition, The Pod name takes the form `$(job-
        name)-$(index)-$(random-string)`, the Pod hostname takes the
        form `$(job-name)-$(index)`.

        More completion modes can be added in the future. If the Job
        controller observes a mode that it doesn't recognize, which
        is possible during upgrades due to version skew, the
        controller skips updates for the Job.
        """
        return typing.cast(
            str,
            self._properties.get("completionMode"),
        )

    @completion_mode.setter
    def completion_mode(self, value: str):
        """
        completionMode specifies how Pod completions are tracked. It
        can be `NonIndexed` (default) or `Indexed`.

        `NonIndexed` means that the Job is considered complete when
        there have been .spec.completions successfully completed
        Pods. Each Pod completion is homologous to each other.

        `Indexed` means that the Pods of a Job get an associated
        completion index from 0 to (.spec.completions - 1),
        available in the annotation batch.kubernetes.io/job-
        completion-index. The Job is considered complete when there
        is one successfully completed Pod for each index. When value
        is `Indexed`, .spec.completions must be specified and
        `.spec.parallelism` must be less than or equal to 10^5. In
        addition, The Pod name takes the form `$(job-
        name)-$(index)-$(random-string)`, the Pod hostname takes the
        form `$(job-name)-$(index)`.

        More completion modes can be added in the future. If the Job
        controller observes a mode that it doesn't recognize, which
        is possible during upgrades due to version skew, the
        controller skips updates for the Job.
        """
        self._properties["completionMode"] = value

    @property
    def completions(self) -> int:
        """
        Specifies the desired number of successfully finished pods
        the job should be run with.  Setting to null means that the
        success of any pod signals the success of all pods, and
        allows parallelism to have any positive value.  Setting to 1
        means that parallelism is limited to 1 and the success of
        that pod signals the success of the job. More info: https://
        kubernetes.io/docs/concepts/workloads/controllers/jobs-run-
        to-completion/
        """
        return typing.cast(
            int,
            self._properties.get("completions"),
        )

    @completions.setter
    def completions(self, value: int):
        """
        Specifies the desired number of successfully finished pods
        the job should be run with.  Setting to null means that the
        success of any pod signals the success of all pods, and
        allows parallelism to have any positive value.  Setting to 1
        means that parallelism is limited to 1 and the success of
        that pod signals the success of the job. More info: https://
        kubernetes.io/docs/concepts/workloads/controllers/jobs-run-
        to-completion/
        """
        self._properties["completions"] = value

    @property
    def manual_selector(self) -> bool:
        """
        manualSelector controls generation of pod labels and pod
        selectors. Leave `manualSelector` unset unless you are
        certain what you are doing. When false or unset, the system
        pick labels unique to this job and appends those labels to
        the pod template.  When true, the user is responsible for
        picking unique labels and specifying the selector.  Failure
        to pick a unique label may cause this and other jobs to not
        function correctly.  However, You may see
        `manualSelector=true` in jobs that were created with the old
        `extensions/v1beta1` API. More info: https://kubernetes.io/d
        ocs/concepts/workloads/controllers/jobs-run-to-
        completion/#specifying-your-own-pod-selector
        """
        return typing.cast(
            bool,
            self._properties.get("manualSelector"),
        )

    @manual_selector.setter
    def manual_selector(self, value: bool):
        """
        manualSelector controls generation of pod labels and pod
        selectors. Leave `manualSelector` unset unless you are
        certain what you are doing. When false or unset, the system
        pick labels unique to this job and appends those labels to
        the pod template.  When true, the user is responsible for
        picking unique labels and specifying the selector.  Failure
        to pick a unique label may cause this and other jobs to not
        function correctly.  However, You may see
        `manualSelector=true` in jobs that were created with the old
        `extensions/v1beta1` API. More info: https://kubernetes.io/d
        ocs/concepts/workloads/controllers/jobs-run-to-
        completion/#specifying-your-own-pod-selector
        """
        self._properties["manualSelector"] = value

    @property
    def max_failed_indexes(self) -> int:
        """
        Specifies the maximal number of failed indexes before
        marking the Job as failed, when backoffLimitPerIndex is set.
        Once the number of failed indexes exceeds this number the
        entire Job is marked as Failed and its execution is
        terminated. When left as null the job continues execution of
        all of its indexes and is marked with the `Complete` Job
        condition. It can only be specified when
        backoffLimitPerIndex is set. It can be null or up to
        completions. It is required and must be less than or equal
        to 10^4 when is completions greater than 10^5. This field is
        alpha-level. It can be used when the
        `JobBackoffLimitPerIndex` feature gate is enabled (disabled
        by default).
        """
        return typing.cast(
            int,
            self._properties.get("maxFailedIndexes"),
        )

    @max_failed_indexes.setter
    def max_failed_indexes(self, value: int):
        """
        Specifies the maximal number of failed indexes before
        marking the Job as failed, when backoffLimitPerIndex is set.
        Once the number of failed indexes exceeds this number the
        entire Job is marked as Failed and its execution is
        terminated. When left as null the job continues execution of
        all of its indexes and is marked with the `Complete` Job
        condition. It can only be specified when
        backoffLimitPerIndex is set. It can be null or up to
        completions. It is required and must be less than or equal
        to 10^4 when is completions greater than 10^5. This field is
        alpha-level. It can be used when the
        `JobBackoffLimitPerIndex` feature gate is enabled (disabled
        by default).
        """
        self._properties["maxFailedIndexes"] = value

    @property
    def parallelism(self) -> int:
        """
        Specifies the maximum desired number of pods the job should
        run at any given time. The actual number of pods running in
        steady state will be less than this number when
        ((.spec.completions - .status.successful) <
        .spec.parallelism), i.e. when the work left to do is less
        than max parallelism. More info: https://kubernetes.io/docs/
        concepts/workloads/controllers/jobs-run-to-completion/
        """
        return typing.cast(
            int,
            self._properties.get("parallelism"),
        )

    @parallelism.setter
    def parallelism(self, value: int):
        """
        Specifies the maximum desired number of pods the job should
        run at any given time. The actual number of pods running in
        steady state will be less than this number when
        ((.spec.completions - .status.successful) <
        .spec.parallelism), i.e. when the work left to do is less
        than max parallelism. More info: https://kubernetes.io/docs/
        concepts/workloads/controllers/jobs-run-to-completion/
        """
        self._properties["parallelism"] = value

    @property
    def pod_failure_policy(self) -> "PodFailurePolicy":
        """
        Specifies the policy of handling failed pods. In particular,
        it allows to specify the set of actions and conditions which
        need to be satisfied to take the associated action. If
        empty, the default behaviour applies - the counter of failed
        pods, represented by the jobs's .status.failed field, is
        incremented and it is checked against the backoffLimit. This
        field cannot be used in combination with
        restartPolicy=OnFailure.

        This field is beta-level. It can be used when the
        `JobPodFailurePolicy` feature gate is enabled (enabled by
        default).
        """
        return typing.cast(
            "PodFailurePolicy",
            self._properties.get("podFailurePolicy"),
        )

    @pod_failure_policy.setter
    def pod_failure_policy(self, value: typing.Union["PodFailurePolicy", dict]):
        """
        Specifies the policy of handling failed pods. In particular,
        it allows to specify the set of actions and conditions which
        need to be satisfied to take the associated action. If
        empty, the default behaviour applies - the counter of failed
        pods, represented by the jobs's .status.failed field, is
        incremented and it is checked against the backoffLimit. This
        field cannot be used in combination with
        restartPolicy=OnFailure.

        This field is beta-level. It can be used when the
        `JobPodFailurePolicy` feature gate is enabled (enabled by
        default).
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodFailurePolicy,
                PodFailurePolicy().from_dict(value),
            )
        self._properties["podFailurePolicy"] = value

    @property
    def pod_replacement_policy(self) -> str:
        """
        podReplacementPolicy specifies when to create replacement
        Pods. Possible values are: - TerminatingOrFailed means that
        we recreate pods
          when they are terminating (has a
        metadata.deletionTimestamp) or failed.
        - Failed means to wait until a previously created Pod is
        fully terminated (has phase
          Failed or Succeeded) before creating a replacement Pod.

        When using podFailurePolicy, Failed is the the only allowed
        value. TerminatingOrFailed and Failed are allowed values
        when podFailurePolicy is not in use. This is an alpha field.
        Enable JobPodReplacementPolicy to be able to use this field.
        """
        return typing.cast(
            str,
            self._properties.get("podReplacementPolicy"),
        )

    @pod_replacement_policy.setter
    def pod_replacement_policy(self, value: str):
        """
        podReplacementPolicy specifies when to create replacement
        Pods. Possible values are: - TerminatingOrFailed means that
        we recreate pods
          when they are terminating (has a
        metadata.deletionTimestamp) or failed.
        - Failed means to wait until a previously created Pod is
        fully terminated (has phase
          Failed or Succeeded) before creating a replacement Pod.

        When using podFailurePolicy, Failed is the the only allowed
        value. TerminatingOrFailed and Failed are allowed values
        when podFailurePolicy is not in use. This is an alpha field.
        Enable JobPodReplacementPolicy to be able to use this field.
        """
        self._properties["podReplacementPolicy"] = value

    @property
    def selector(self) -> "LabelSelector":
        """
        A label query over pods that should match the pod count.
        Normally, the system sets this field for you. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        return typing.cast(
            "LabelSelector",
            self._properties.get("selector"),
        )

    @selector.setter
    def selector(self, value: typing.Union["LabelSelector", dict]):
        """
        A label query over pods that should match the pod count.
        Normally, the system sets this field for you. More info:
        https://kubernetes.io/docs/concepts/overview/working-with-
        objects/labels/#label-selectors
        """
        if isinstance(value, dict):
            value = typing.cast(
                LabelSelector,
                LabelSelector().from_dict(value),
            )
        self._properties["selector"] = value

    @property
    def suspend(self) -> bool:
        """
        suspend specifies whether the Job controller should create
        Pods or not. If a Job is created with suspend set to true,
        no Pods are created by the Job controller. If a Job is
        suspended after creation (i.e. the flag goes from false to
        true), the Job controller will delete all active Pods
        associated with this Job. Users must design their workload
        to gracefully handle this. Suspending a Job will reset the
        StartTime field of the Job, effectively resetting the
        ActiveDeadlineSeconds timer too. Defaults to false.
        """
        return typing.cast(
            bool,
            self._properties.get("suspend"),
        )

    @suspend.setter
    def suspend(self, value: bool):
        """
        suspend specifies whether the Job controller should create
        Pods or not. If a Job is created with suspend set to true,
        no Pods are created by the Job controller. If a Job is
        suspended after creation (i.e. the flag goes from false to
        true), the Job controller will delete all active Pods
        associated with this Job. Users must design their workload
        to gracefully handle this. Suspending a Job will reset the
        StartTime field of the Job, effectively resetting the
        ActiveDeadlineSeconds timer too. Defaults to false.
        """
        self._properties["suspend"] = value

    @property
    def template(self) -> "PodTemplateSpec":
        """
        Describes the pod that will be created when executing a job.
        The only allowed template.spec.restartPolicy values are
        "Never" or "OnFailure". More info: https://kubernetes.io/doc
        s/concepts/workloads/controllers/jobs-run-to-completion/
        """
        return typing.cast(
            "PodTemplateSpec",
            self._properties.get("template"),
        )

    @template.setter
    def template(self, value: typing.Union["PodTemplateSpec", dict]):
        """
        Describes the pod that will be created when executing a job.
        The only allowed template.spec.restartPolicy values are
        "Never" or "OnFailure". More info: https://kubernetes.io/doc
        s/concepts/workloads/controllers/jobs-run-to-completion/
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodTemplateSpec,
                PodTemplateSpec().from_dict(value),
            )
        self._properties["template"] = value

    @property
    def ttl_seconds_after_finished(self) -> int:
        """
        ttlSecondsAfterFinished limits the lifetime of a Job that
        has finished execution (either Complete or Failed). If this
        field is set, ttlSecondsAfterFinished after the Job
        finishes, it is eligible to be automatically deleted. When
        the Job is being deleted, its lifecycle guarantees (e.g.
        finalizers) will be honored. If this field is unset, the Job
        won't be automatically deleted. If this field is set to
        zero, the Job becomes eligible to be deleted immediately
        after it finishes.
        """
        return typing.cast(
            int,
            self._properties.get("ttlSecondsAfterFinished"),
        )

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, value: int):
        """
        ttlSecondsAfterFinished limits the lifetime of a Job that
        has finished execution (either Complete or Failed). If this
        field is set, ttlSecondsAfterFinished after the Job
        finishes, it is eligible to be automatically deleted. When
        the Job is being deleted, its lifecycle guarantees (e.g.
        finalizers) will be honored. If this field is unset, the Job
        won't be automatically deleted. If this field is set to
        zero, the Job becomes eligible to be deleted immediately
        after it finishes.
        """
        self._properties["ttlSecondsAfterFinished"] = value

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
        resize_policy: typing.Union[
            typing.List["ContainerResizePolicy"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        restart_policy: typing.Union[
            str,
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
    ) -> "JobSpec":
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
            "resize_policy": resize_policy,
            "resources": resources,
            "restart_policy": restart_policy,
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
        self.template.spec.containers.append(
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
        return next((c for c in self.template.spec.containers if c.name == name), None)

    def get_containers(self) -> typing.List["Container"]:
        """
        Returns the list of containers stored in this resource if any such
        containers exist.
        """
        return self.template.spec.containers

    def __enter__(self) -> "JobSpec":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class JobStatus(_kuber_definitions.Definition):
    """
    JobStatus represents the current state of a Job.
    """

    def __init__(
        self,
        active: typing.Optional[int] = None,
        completed_indexes: typing.Optional[str] = None,
        completion_time: typing.Optional[str] = None,
        conditions: typing.Optional[typing.List["JobCondition"]] = None,
        failed: typing.Optional[int] = None,
        failed_indexes: typing.Optional[str] = None,
        ready: typing.Optional[int] = None,
        start_time: typing.Optional[str] = None,
        succeeded: typing.Optional[int] = None,
        terminating: typing.Optional[int] = None,
        uncounted_terminated_pods: typing.Optional["UncountedTerminatedPods"] = None,
    ):
        """Create JobStatus instance."""
        super(JobStatus, self).__init__(api_version="batch/v1", kind="JobStatus")
        self._properties = {
            "active": active if active is not None else None,
            "completedIndexes": (
                completed_indexes if completed_indexes is not None else ""
            ),
            "completionTime": completion_time if completion_time is not None else None,
            "conditions": conditions if conditions is not None else [],
            "failed": failed if failed is not None else None,
            "failedIndexes": failed_indexes if failed_indexes is not None else "",
            "ready": ready if ready is not None else None,
            "startTime": start_time if start_time is not None else None,
            "succeeded": succeeded if succeeded is not None else None,
            "terminating": terminating if terminating is not None else None,
            "uncountedTerminatedPods": (
                uncounted_terminated_pods
                if uncounted_terminated_pods is not None
                else UncountedTerminatedPods()
            ),
        }
        self._types = {
            "active": (int, None),
            "completedIndexes": (str, None),
            "completionTime": (str, None),
            "conditions": (list, JobCondition),
            "failed": (int, None),
            "failedIndexes": (str, None),
            "ready": (int, None),
            "startTime": (str, None),
            "succeeded": (int, None),
            "terminating": (int, None),
            "uncountedTerminatedPods": (UncountedTerminatedPods, None),
        }

    @property
    def active(self) -> int:
        """
        The number of pending and running pods.
        """
        return typing.cast(
            int,
            self._properties.get("active"),
        )

    @active.setter
    def active(self, value: int):
        """
        The number of pending and running pods.
        """
        self._properties["active"] = value

    @property
    def completed_indexes(self) -> str:
        """
        completedIndexes holds the completed indexes when
        .spec.completionMode = "Indexed" in a text format. The
        indexes are represented as decimal integers separated by
        commas. The numbers are listed in increasing order. Three or
        more consecutive numbers are compressed and represented by
        the first and last element of the series, separated by a
        hyphen. For example, if the completed indexes are 1, 3, 4, 5
        and 7, they are represented as "1,3-5,7".
        """
        return typing.cast(
            str,
            self._properties.get("completedIndexes"),
        )

    @completed_indexes.setter
    def completed_indexes(self, value: str):
        """
        completedIndexes holds the completed indexes when
        .spec.completionMode = "Indexed" in a text format. The
        indexes are represented as decimal integers separated by
        commas. The numbers are listed in increasing order. Three or
        more consecutive numbers are compressed and represented by
        the first and last element of the series, separated by a
        hyphen. For example, if the completed indexes are 1, 3, 4, 5
        and 7, they are represented as "1,3-5,7".
        """
        self._properties["completedIndexes"] = value

    @property
    def completion_time(self) -> str:
        """
        Represents time when the job was completed. It is not
        guaranteed to be set in happens-before order across separate
        operations. It is represented in RFC3339 form and is in UTC.
        The completion time is only set when the job finishes
        successfully.
        """
        return typing.cast(
            str,
            self._properties.get("completionTime"),
        )

    @completion_time.setter
    def completion_time(
        self, value: typing.Union[str, _datetime.datetime, _datetime.date]
    ):
        """
        Represents time when the job was completed. It is not
        guaranteed to be set in happens-before order across separate
        operations. It is represented in RFC3339 form and is in UTC.
        The completion time is only set when the job finishes
        successfully.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["completionTime"] = value

    @property
    def conditions(self) -> typing.List["JobCondition"]:
        """
        The latest available observations of an object's current
        state. When a Job fails, one of the conditions will have
        type "Failed" and status true. When a Job is suspended, one
        of the conditions will have type "Suspended" and status
        true; when the Job is resumed, the status of this condition
        will become false. When a Job is completed, one of the
        conditions will have type "Complete" and status true. More
        info: https://kubernetes.io/docs/concepts/workloads/controll
        ers/jobs-run-to-completion/
        """
        return typing.cast(
            typing.List["JobCondition"],
            self._properties.get("conditions"),
        )

    @conditions.setter
    def conditions(
        self, value: typing.Union[typing.List["JobCondition"], typing.List[dict]]
    ):
        """
        The latest available observations of an object's current
        state. When a Job fails, one of the conditions will have
        type "Failed" and status true. When a Job is suspended, one
        of the conditions will have type "Suspended" and status
        true; when the Job is resumed, the status of this condition
        will become false. When a Job is completed, one of the
        conditions will have type "Complete" and status true. More
        info: https://kubernetes.io/docs/concepts/workloads/controll
        ers/jobs-run-to-completion/
        """
        cleaned: typing.List[JobCondition] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    JobCondition,
                    JobCondition().from_dict(item),
                )
            cleaned.append(typing.cast(JobCondition, item))
        self._properties["conditions"] = cleaned

    @property
    def failed(self) -> int:
        """
        The number of pods which reached phase Failed.
        """
        return typing.cast(
            int,
            self._properties.get("failed"),
        )

    @failed.setter
    def failed(self, value: int):
        """
        The number of pods which reached phase Failed.
        """
        self._properties["failed"] = value

    @property
    def failed_indexes(self) -> str:
        """
        FailedIndexes holds the failed indexes when
        backoffLimitPerIndex=true. The indexes are represented in
        the text format analogous as for the `completedIndexes`
        field, ie. they are kept as decimal integers separated by
        commas. The numbers are listed in increasing order. Three or
        more consecutive numbers are compressed and represented by
        the first and last element of the series, separated by a
        hyphen. For example, if the failed indexes are 1, 3, 4, 5
        and 7, they are represented as "1,3-5,7". This field is
        alpha-level. It can be used when the
        `JobBackoffLimitPerIndex` feature gate is enabled (disabled
        by default).
        """
        return typing.cast(
            str,
            self._properties.get("failedIndexes"),
        )

    @failed_indexes.setter
    def failed_indexes(self, value: str):
        """
        FailedIndexes holds the failed indexes when
        backoffLimitPerIndex=true. The indexes are represented in
        the text format analogous as for the `completedIndexes`
        field, ie. they are kept as decimal integers separated by
        commas. The numbers are listed in increasing order. Three or
        more consecutive numbers are compressed and represented by
        the first and last element of the series, separated by a
        hyphen. For example, if the failed indexes are 1, 3, 4, 5
        and 7, they are represented as "1,3-5,7". This field is
        alpha-level. It can be used when the
        `JobBackoffLimitPerIndex` feature gate is enabled (disabled
        by default).
        """
        self._properties["failedIndexes"] = value

    @property
    def ready(self) -> int:
        """
        The number of pods which have a Ready condition.

        This field is beta-level. The job controller populates the
        field when the feature gate JobReadyPods is enabled (enabled
        by default).
        """
        return typing.cast(
            int,
            self._properties.get("ready"),
        )

    @ready.setter
    def ready(self, value: int):
        """
        The number of pods which have a Ready condition.

        This field is beta-level. The job controller populates the
        field when the feature gate JobReadyPods is enabled (enabled
        by default).
        """
        self._properties["ready"] = value

    @property
    def start_time(self) -> str:
        """
        Represents time when the job controller started processing a
        job. When a Job is created in the suspended state, this
        field is not set until the first time it is resumed. This
        field is reset every time a Job is resumed from suspension.
        It is represented in RFC3339 form and is in UTC.
        """
        return typing.cast(
            str,
            self._properties.get("startTime"),
        )

    @start_time.setter
    def start_time(self, value: typing.Union[str, _datetime.datetime, _datetime.date]):
        """
        Represents time when the job controller started processing a
        job. When a Job is created in the suspended state, this
        field is not set until the first time it is resumed. This
        field is reset every time a Job is resumed from suspension.
        It is represented in RFC3339 form and is in UTC.
        """
        if isinstance(value, _datetime.datetime):
            value = value.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(value, _datetime.date):
            value = value.strftime("%Y-%m-%dT00:00:00Z")
        self._properties["startTime"] = value

    @property
    def succeeded(self) -> int:
        """
        The number of pods which reached phase Succeeded.
        """
        return typing.cast(
            int,
            self._properties.get("succeeded"),
        )

    @succeeded.setter
    def succeeded(self, value: int):
        """
        The number of pods which reached phase Succeeded.
        """
        self._properties["succeeded"] = value

    @property
    def terminating(self) -> int:
        """
        The number of pods which are terminating (in phase Pending
        or Running and have a deletionTimestamp).

        This field is alpha-level. The job controller populates the
        field when the feature gate JobPodReplacementPolicy is
        enabled (disabled by default).
        """
        return typing.cast(
            int,
            self._properties.get("terminating"),
        )

    @terminating.setter
    def terminating(self, value: int):
        """
        The number of pods which are terminating (in phase Pending
        or Running and have a deletionTimestamp).

        This field is alpha-level. The job controller populates the
        field when the feature gate JobPodReplacementPolicy is
        enabled (disabled by default).
        """
        self._properties["terminating"] = value

    @property
    def uncounted_terminated_pods(self) -> "UncountedTerminatedPods":
        """
        uncountedTerminatedPods holds the UIDs of Pods that have
        terminated but the job controller hasn't yet accounted for
        in the status counters.

        The job controller creates pods with a finalizer. When a pod
        terminates (succeeded or failed), the controller does three
        steps to account for it in the job status:

        1. Add the pod UID to the arrays in this field. 2. Remove
        the pod finalizer. 3. Remove the pod UID from the arrays
        while increasing the corresponding
            counter.

        Old jobs might not be tracked using this field, in which
        case the field remains null.
        """
        return typing.cast(
            "UncountedTerminatedPods",
            self._properties.get("uncountedTerminatedPods"),
        )

    @uncounted_terminated_pods.setter
    def uncounted_terminated_pods(
        self, value: typing.Union["UncountedTerminatedPods", dict]
    ):
        """
        uncountedTerminatedPods holds the UIDs of Pods that have
        terminated but the job controller hasn't yet accounted for
        in the status counters.

        The job controller creates pods with a finalizer. When a pod
        terminates (succeeded or failed), the controller does three
        steps to account for it in the job status:

        1. Add the pod UID to the arrays in this field. 2. Remove
        the pod finalizer. 3. Remove the pod UID from the arrays
        while increasing the corresponding
            counter.

        Old jobs might not be tracked using this field, in which
        case the field remains null.
        """
        if isinstance(value, dict):
            value = typing.cast(
                UncountedTerminatedPods,
                UncountedTerminatedPods().from_dict(value),
            )
        self._properties["uncountedTerminatedPods"] = value

    def __enter__(self) -> "JobStatus":
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
        metadata: typing.Optional["ObjectMeta"] = None,
        spec: typing.Optional["JobSpec"] = None,
    ):
        """Create JobTemplateSpec instance."""
        super(JobTemplateSpec, self).__init__(
            api_version="batch/v1", kind="JobTemplateSpec"
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
        resize_policy: typing.Union[
            typing.List["ContainerResizePolicy"],
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        resources: typing.Union[
            "ResourceRequirements",
            _kuber_definitions.InternalValue,
        ] = _kuber_definitions.UNCHANGED_VALUE,
        restart_policy: typing.Union[
            str,
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
            "resize_policy": resize_policy,
            "resources": resources,
            "restart_policy": restart_policy,
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


class PodFailurePolicy(_kuber_definitions.Definition):
    """
    PodFailurePolicy describes how failed pods influence the
    backoffLimit.
    """

    def __init__(
        self,
        rules: typing.Optional[typing.List["PodFailurePolicyRule"]] = None,
    ):
        """Create PodFailurePolicy instance."""
        super(PodFailurePolicy, self).__init__(
            api_version="batch/v1", kind="PodFailurePolicy"
        )
        self._properties = {
            "rules": rules if rules is not None else [],
        }
        self._types = {
            "rules": (list, PodFailurePolicyRule),
        }

    @property
    def rules(self) -> typing.List["PodFailurePolicyRule"]:
        """
        A list of pod failure policy rules. The rules are evaluated
        in order. Once a rule matches a Pod failure, the remaining
        of the rules are ignored. When no rule matches the Pod
        failure, the default handling applies - the counter of pod
        failures is incremented and it is checked against the
        backoffLimit. At most 20 elements are allowed.
        """
        return typing.cast(
            typing.List["PodFailurePolicyRule"],
            self._properties.get("rules"),
        )

    @rules.setter
    def rules(
        self,
        value: typing.Union[typing.List["PodFailurePolicyRule"], typing.List[dict]],
    ):
        """
        A list of pod failure policy rules. The rules are evaluated
        in order. Once a rule matches a Pod failure, the remaining
        of the rules are ignored. When no rule matches the Pod
        failure, the default handling applies - the counter of pod
        failures is incremented and it is checked against the
        backoffLimit. At most 20 elements are allowed.
        """
        cleaned: typing.List[PodFailurePolicyRule] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PodFailurePolicyRule,
                    PodFailurePolicyRule().from_dict(item),
                )
            cleaned.append(typing.cast(PodFailurePolicyRule, item))
        self._properties["rules"] = cleaned

    def __enter__(self) -> "PodFailurePolicy":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodFailurePolicyOnExitCodesRequirement(_kuber_definitions.Definition):
    """
    PodFailurePolicyOnExitCodesRequirement describes the
    requirement for handling a failed pod based on its container
    exit codes. In particular, it lookups the
    .state.terminated.exitCode for each app container and init
    container status, represented by the
    .status.containerStatuses and .status.initContainerStatuses
    fields in the Pod status, respectively. Containers completed
    with success (exit code 0) are excluded from the requirement
    check.
    """

    def __init__(
        self,
        container_name: typing.Optional[str] = None,
        operator: typing.Optional[str] = None,
        values: typing.Optional[typing.List[int]] = None,
    ):
        """Create PodFailurePolicyOnExitCodesRequirement instance."""
        super(PodFailurePolicyOnExitCodesRequirement, self).__init__(
            api_version="batch/v1", kind="PodFailurePolicyOnExitCodesRequirement"
        )
        self._properties = {
            "containerName": container_name if container_name is not None else "",
            "operator": operator if operator is not None else "",
            "values": values if values is not None else [],
        }
        self._types = {
            "containerName": (str, None),
            "operator": (str, None),
            "values": (list, int),
        }

    @property
    def container_name(self) -> str:
        """
        Restricts the check for exit codes to the container with the
        specified name. When null, the rule applies to all
        containers. When specified, it should match one the
        container or initContainer names in the pod template.
        """
        return typing.cast(
            str,
            self._properties.get("containerName"),
        )

    @container_name.setter
    def container_name(self, value: str):
        """
        Restricts the check for exit codes to the container with the
        specified name. When null, the rule applies to all
        containers. When specified, it should match one the
        container or initContainer names in the pod template.
        """
        self._properties["containerName"] = value

    @property
    def operator(self) -> str:
        """
        Represents the relationship between the container exit
        code(s) and the specified values. Containers completed with
        success (exit code 0) are excluded from the requirement
        check. Possible values are:

        - In: the requirement is satisfied if at least one container
        exit code
          (might be multiple if there are multiple containers not
        restricted
          by the 'containerName' field) is in the set of specified
        values.
        - NotIn: the requirement is satisfied if at least one
        container exit code
          (might be multiple if there are multiple containers not
        restricted
          by the 'containerName' field) is not in the set of
        specified values.
        Additional values are considered to be added in the future.
        Clients should react to an unknown operator by assuming the
        requirement is not satisfied.
        """
        return typing.cast(
            str,
            self._properties.get("operator"),
        )

    @operator.setter
    def operator(self, value: str):
        """
        Represents the relationship between the container exit
        code(s) and the specified values. Containers completed with
        success (exit code 0) are excluded from the requirement
        check. Possible values are:

        - In: the requirement is satisfied if at least one container
        exit code
          (might be multiple if there are multiple containers not
        restricted
          by the 'containerName' field) is in the set of specified
        values.
        - NotIn: the requirement is satisfied if at least one
        container exit code
          (might be multiple if there are multiple containers not
        restricted
          by the 'containerName' field) is not in the set of
        specified values.
        Additional values are considered to be added in the future.
        Clients should react to an unknown operator by assuming the
        requirement is not satisfied.
        """
        self._properties["operator"] = value

    @property
    def values(self) -> typing.List[int]:
        """
        Specifies the set of values. Each returned container exit
        code (might be multiple in case of multiple containers) is
        checked against this set of values with respect to the
        operator. The list of values must be ordered and must not
        contain duplicates. Value '0' cannot be used for the In
        operator. At least one element is required. At most 255
        elements are allowed.
        """
        return typing.cast(
            typing.List[int],
            self._properties.get("values"),
        )

    @values.setter
    def values(self, value: typing.List[int]):
        """
        Specifies the set of values. Each returned container exit
        code (might be multiple in case of multiple containers) is
        checked against this set of values with respect to the
        operator. The list of values must be ordered and must not
        contain duplicates. Value '0' cannot be used for the In
        operator. At least one element is required. At most 255
        elements are allowed.
        """
        self._properties["values"] = value

    def __enter__(self) -> "PodFailurePolicyOnExitCodesRequirement":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodFailurePolicyOnPodConditionsPattern(_kuber_definitions.Definition):
    """
    PodFailurePolicyOnPodConditionsPattern describes a pattern
    for matching an actual pod condition type.
    """

    def __init__(
        self,
        status: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
    ):
        """Create PodFailurePolicyOnPodConditionsPattern instance."""
        super(PodFailurePolicyOnPodConditionsPattern, self).__init__(
            api_version="batch/v1", kind="PodFailurePolicyOnPodConditionsPattern"
        )
        self._properties = {
            "status": status if status is not None else "",
            "type": type_ if type_ is not None else "",
        }
        self._types = {
            "status": (str, None),
            "type": (str, None),
        }

    @property
    def status(self) -> str:
        """
        Specifies the required Pod condition status. To match a pod
        condition it is required that the specified status equals
        the pod condition status. Defaults to True.
        """
        return typing.cast(
            str,
            self._properties.get("status"),
        )

    @status.setter
    def status(self, value: str):
        """
        Specifies the required Pod condition status. To match a pod
        condition it is required that the specified status equals
        the pod condition status. Defaults to True.
        """
        self._properties["status"] = value

    @property
    def type_(self) -> str:
        """
        Specifies the required Pod condition type. To match a pod
        condition it is required that specified type equals the pod
        condition type.
        """
        return typing.cast(
            str,
            self._properties.get("type"),
        )

    @type_.setter
    def type_(self, value: str):
        """
        Specifies the required Pod condition type. To match a pod
        condition it is required that specified type equals the pod
        condition type.
        """
        self._properties["type"] = value

    def __enter__(self) -> "PodFailurePolicyOnPodConditionsPattern":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class PodFailurePolicyRule(_kuber_definitions.Definition):
    """
    PodFailurePolicyRule describes how a pod failure is handled
    when the requirements are met. One of onExitCodes and
    onPodConditions, but not both, can be used in each rule.
    """

    def __init__(
        self,
        action: typing.Optional[str] = None,
        on_exit_codes: typing.Optional["PodFailurePolicyOnExitCodesRequirement"] = None,
        on_pod_conditions: typing.Optional[
            typing.List["PodFailurePolicyOnPodConditionsPattern"]
        ] = None,
    ):
        """Create PodFailurePolicyRule instance."""
        super(PodFailurePolicyRule, self).__init__(
            api_version="batch/v1", kind="PodFailurePolicyRule"
        )
        self._properties = {
            "action": action if action is not None else "",
            "onExitCodes": (
                on_exit_codes
                if on_exit_codes is not None
                else PodFailurePolicyOnExitCodesRequirement()
            ),
            "onPodConditions": (
                on_pod_conditions if on_pod_conditions is not None else []
            ),
        }
        self._types = {
            "action": (str, None),
            "onExitCodes": (PodFailurePolicyOnExitCodesRequirement, None),
            "onPodConditions": (list, PodFailurePolicyOnPodConditionsPattern),
        }

    @property
    def action(self) -> str:
        """
        Specifies the action taken on a pod failure when the
        requirements are satisfied. Possible values are:

        - FailJob: indicates that the pod's job is marked as Failed
        and all
          running pods are terminated.
        - FailIndex: indicates that the pod's index is marked as
        Failed and will
          not be restarted.
          This value is alpha-level. It can be used when the
          `JobBackoffLimitPerIndex` feature gate is enabled
        (disabled by default).
        - Ignore: indicates that the counter towards the
        .backoffLimit is not
          incremented and a replacement pod is created.
        - Count: indicates that the pod is handled in the default
        way - the
          counter towards the .backoffLimit is incremented.
        Additional values are considered to be added in the future.
        Clients should react to an unknown action by skipping the
        rule.
        """
        return typing.cast(
            str,
            self._properties.get("action"),
        )

    @action.setter
    def action(self, value: str):
        """
        Specifies the action taken on a pod failure when the
        requirements are satisfied. Possible values are:

        - FailJob: indicates that the pod's job is marked as Failed
        and all
          running pods are terminated.
        - FailIndex: indicates that the pod's index is marked as
        Failed and will
          not be restarted.
          This value is alpha-level. It can be used when the
          `JobBackoffLimitPerIndex` feature gate is enabled
        (disabled by default).
        - Ignore: indicates that the counter towards the
        .backoffLimit is not
          incremented and a replacement pod is created.
        - Count: indicates that the pod is handled in the default
        way - the
          counter towards the .backoffLimit is incremented.
        Additional values are considered to be added in the future.
        Clients should react to an unknown action by skipping the
        rule.
        """
        self._properties["action"] = value

    @property
    def on_exit_codes(self) -> "PodFailurePolicyOnExitCodesRequirement":
        """
        Represents the requirement on the container exit codes.
        """
        return typing.cast(
            "PodFailurePolicyOnExitCodesRequirement",
            self._properties.get("onExitCodes"),
        )

    @on_exit_codes.setter
    def on_exit_codes(
        self, value: typing.Union["PodFailurePolicyOnExitCodesRequirement", dict]
    ):
        """
        Represents the requirement on the container exit codes.
        """
        if isinstance(value, dict):
            value = typing.cast(
                PodFailurePolicyOnExitCodesRequirement,
                PodFailurePolicyOnExitCodesRequirement().from_dict(value),
            )
        self._properties["onExitCodes"] = value

    @property
    def on_pod_conditions(
        self,
    ) -> typing.List["PodFailurePolicyOnPodConditionsPattern"]:
        """
        Represents the requirement on the pod conditions. The
        requirement is represented as a list of pod condition
        patterns. The requirement is satisfied if at least one
        pattern matches an actual pod condition. At most 20 elements
        are allowed.
        """
        return typing.cast(
            typing.List["PodFailurePolicyOnPodConditionsPattern"],
            self._properties.get("onPodConditions"),
        )

    @on_pod_conditions.setter
    def on_pod_conditions(
        self,
        value: typing.Union[
            typing.List["PodFailurePolicyOnPodConditionsPattern"], typing.List[dict]
        ],
    ):
        """
        Represents the requirement on the pod conditions. The
        requirement is represented as a list of pod condition
        patterns. The requirement is satisfied if at least one
        pattern matches an actual pod condition. At most 20 elements
        are allowed.
        """
        cleaned: typing.List[PodFailurePolicyOnPodConditionsPattern] = []
        for item in value:
            if isinstance(item, dict):
                item = typing.cast(
                    PodFailurePolicyOnPodConditionsPattern,
                    PodFailurePolicyOnPodConditionsPattern().from_dict(item),
                )
            cleaned.append(typing.cast(PodFailurePolicyOnPodConditionsPattern, item))
        self._properties["onPodConditions"] = cleaned

    def __enter__(self) -> "PodFailurePolicyRule":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class UncountedTerminatedPods(_kuber_definitions.Definition):
    """
    UncountedTerminatedPods holds UIDs of Pods that have
    terminated but haven't been accounted in Job status
    counters.
    """

    def __init__(
        self,
        failed: typing.Optional[typing.List[str]] = None,
        succeeded: typing.Optional[typing.List[str]] = None,
    ):
        """Create UncountedTerminatedPods instance."""
        super(UncountedTerminatedPods, self).__init__(
            api_version="batch/v1", kind="UncountedTerminatedPods"
        )
        self._properties = {
            "failed": failed if failed is not None else [],
            "succeeded": succeeded if succeeded is not None else [],
        }
        self._types = {
            "failed": (list, str),
            "succeeded": (list, str),
        }

    @property
    def failed(self) -> typing.List[str]:
        """
        failed holds UIDs of failed Pods.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("failed"),
        )

    @failed.setter
    def failed(self, value: typing.List[str]):
        """
        failed holds UIDs of failed Pods.
        """
        self._properties["failed"] = value

    @property
    def succeeded(self) -> typing.List[str]:
        """
        succeeded holds UIDs of succeeded Pods.
        """
        return typing.cast(
            typing.List[str],
            self._properties.get("succeeded"),
        )

    @succeeded.setter
    def succeeded(self, value: typing.List[str]):
        """
        succeeded holds UIDs of succeeded Pods.
        """
        self._properties["succeeded"] = value

    def __enter__(self) -> "UncountedTerminatedPods":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
