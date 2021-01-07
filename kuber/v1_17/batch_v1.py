import typing  # noqa: F401
import datetime as _datetime  # noqa: F401

from kubernetes import client  # noqa: F401
from kuber import kube_api as _kube_api  # noqa: F401

from kuber import definitions as _kuber_definitions  # noqa: F401
from kuber import _types  # noqa: F401
from kuber.v1_17.core_v1 import Container  # noqa: F401
from kuber.v1_17.core_v1 import ContainerPort  # noqa: F401
from kuber.v1_17.core_v1 import EnvFromSource  # noqa: F401
from kuber.v1_17.core_v1 import EnvVar  # noqa: F401
from kuber.v1_17.meta_v1 import LabelSelector  # noqa: F401
from kuber.v1_17.core_v1 import Lifecycle  # noqa: F401
from kuber.v1_17.meta_v1 import ListMeta  # noqa: F401
from kuber.v1_17.meta_v1 import ObjectMeta  # noqa: F401
from kuber.v1_17.core_v1 import PodTemplateSpec  # noqa: F401
from kuber.v1_17.core_v1 import Probe  # noqa: F401
from kuber.v1_17.core_v1 import ResourceRequirements  # noqa: F401
from kuber.v1_17.core_v1 import SecurityContext  # noqa: F401
from kuber.v1_17.meta_v1 import Status  # noqa: F401
from kuber.v1_17.meta_v1 import StatusDetails  # noqa: F401
from kuber.v1_17.core_v1 import VolumeDevice  # noqa: F401
from kuber.v1_17.core_v1 import VolumeMount  # noqa: F401


class Job(_kuber_definitions.Resource):
    """
    Job represents the configuration of a single job.
    """

    def __init__(
        self,
        metadata: "ObjectMeta" = None,
        spec: "JobSpec" = None,
        status: "JobStatus" = None,
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

    def create_resource(self, namespace: "str" = None) -> "JobStatus":
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

    def replace_resource(self, namespace: "str" = None) -> "JobStatus":
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

    def patch_resource(self, namespace: "str" = None) -> "JobStatus":
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

    def get_resource_status(self, namespace: "str" = None) -> "JobStatus":
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

    def read_resource(self, namespace: str = None):
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
        namespace: str = None,
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
        api_client: client.ApiClient = None, **kwargs
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
        last_probe_time: str = None,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type_: str = None,
    ):
        """Create JobCondition instance."""
        super(JobCondition, self).__init__(api_version="batch/v1", kind="JobCondition")
        self._properties = {
            "lastProbeTime": last_probe_time if last_probe_time is not None else None,
            "lastTransitionTime": last_transition_time
            if last_transition_time is not None
            else None,
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
        items: typing.List["Job"] = None,
        metadata: "ListMeta" = None,
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
        api_client: client.ApiClient = None, **kwargs
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
        active_deadline_seconds: int = None,
        backoff_limit: int = None,
        completions: int = None,
        manual_selector: bool = None,
        parallelism: int = None,
        selector: "LabelSelector" = None,
        template: "PodTemplateSpec" = None,
        ttl_seconds_after_finished: int = None,
    ):
        """Create JobSpec instance."""
        super(JobSpec, self).__init__(api_version="batch/v1", kind="JobSpec")
        self._properties = {
            "activeDeadlineSeconds": active_deadline_seconds
            if active_deadline_seconds is not None
            else None,
            "backoffLimit": backoff_limit if backoff_limit is not None else None,
            "completions": completions if completions is not None else None,
            "manualSelector": manual_selector if manual_selector is not None else None,
            "parallelism": parallelism if parallelism is not None else None,
            "selector": selector if selector is not None else LabelSelector(),
            "template": template if template is not None else PodTemplateSpec(),
            "ttlSecondsAfterFinished": ttl_seconds_after_finished
            if ttl_seconds_after_finished is not None
            else None,
        }
        self._types = {
            "activeDeadlineSeconds": (int, None),
            "backoffLimit": (int, None),
            "completions": (int, None),
            "manualSelector": (bool, None),
            "parallelism": (int, None),
            "selector": (LabelSelector, None),
            "template": (PodTemplateSpec, None),
            "ttlSecondsAfterFinished": (int, None),
        }

    @property
    def active_deadline_seconds(self) -> int:
        """
        Specifies the duration in seconds relative to the startTime
        that the job may be active before the system tries to
        terminate it; value must be positive integer
        """
        return typing.cast(
            int,
            self._properties.get("activeDeadlineSeconds"),
        )

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, value: int):
        """
        Specifies the duration in seconds relative to the startTime
        that the job may be active before the system tries to
        terminate it; value must be positive integer
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
    def completions(self) -> int:
        """
        Specifies the desired number of successfully finished pods
        the job should be run with.  Setting to nil means that the
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
        the job should be run with.  Setting to nil means that the
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
    def template(self) -> "PodTemplateSpec":
        """
        Describes the pod that will be created when executing a job.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/jobs-run-to-completion/
        """
        return typing.cast(
            "PodTemplateSpec",
            self._properties.get("template"),
        )

    @template.setter
    def template(self, value: typing.Union["PodTemplateSpec", dict]):
        """
        Describes the pod that will be created when executing a job.
        More info: https://kubernetes.io/docs/concepts/workloads/con
        trollers/jobs-run-to-completion/
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
        after it finishes. This field is alpha-level and is only
        honored by servers that enable the TTLAfterFinished feature.
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
        after it finishes. This field is alpha-level and is only
        honored by servers that enable the TTLAfterFinished feature.
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
        active: int = None,
        completion_time: str = None,
        conditions: typing.List["JobCondition"] = None,
        failed: int = None,
        start_time: str = None,
        succeeded: int = None,
    ):
        """Create JobStatus instance."""
        super(JobStatus, self).__init__(api_version="batch/v1", kind="JobStatus")
        self._properties = {
            "active": active if active is not None else None,
            "completionTime": completion_time if completion_time is not None else None,
            "conditions": conditions if conditions is not None else [],
            "failed": failed if failed is not None else None,
            "startTime": start_time if start_time is not None else None,
            "succeeded": succeeded if succeeded is not None else None,
        }
        self._types = {
            "active": (int, None),
            "completionTime": (str, None),
            "conditions": (list, JobCondition),
            "failed": (int, None),
            "startTime": (str, None),
            "succeeded": (int, None),
        }

    @property
    def active(self) -> int:
        """
        The number of actively running pods.
        """
        return typing.cast(
            int,
            self._properties.get("active"),
        )

    @active.setter
    def active(self, value: int):
        """
        The number of actively running pods.
        """
        self._properties["active"] = value

    @property
    def completion_time(self) -> str:
        """
        Represents time when the job was completed. It is not
        guaranteed to be set in happens-before order across separate
        operations. It is represented in RFC3339 form and is in UTC.
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
        state. More info: https://kubernetes.io/docs/concepts/worklo
        ads/controllers/jobs-run-to-completion/
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
        state. More info: https://kubernetes.io/docs/concepts/worklo
        ads/controllers/jobs-run-to-completion/
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
    def start_time(self) -> str:
        """
        Represents time when the job was acknowledged by the job
        controller. It is not guaranteed to be set in happens-before
        order across separate operations. It is represented in
        RFC3339 form and is in UTC.
        """
        return typing.cast(
            str,
            self._properties.get("startTime"),
        )

    @start_time.setter
    def start_time(self, value: typing.Union[str, _datetime.datetime, _datetime.date]):
        """
        Represents time when the job was acknowledged by the job
        controller. It is not guaranteed to be set in happens-before
        order across separate operations. It is represented in
        RFC3339 form and is in UTC.
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

    def __enter__(self) -> "JobStatus":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
