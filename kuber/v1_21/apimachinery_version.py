import typing

from kubernetes import client

from kuber import definitions as _kuber_definitions


class Info(_kuber_definitions.Definition):
    """
    Info contains versioning information. how we'll want to
    distribute that information.
    """

    def __init__(
        self,
        build_date: str = None,
        compiler: str = None,
        git_commit: str = None,
        git_tree_state: str = None,
        git_version: str = None,
        go_version: str = None,
        major: str = None,
        minor: str = None,
        platform: str = None,
    ):
        """Create Info instance."""
        super(Info, self).__init__(api_version="apimachinery/version", kind="Info")
        self._properties = {
            "buildDate": build_date if build_date is not None else "",
            "compiler": compiler if compiler is not None else "",
            "gitCommit": git_commit if git_commit is not None else "",
            "gitTreeState": git_tree_state if git_tree_state is not None else "",
            "gitVersion": git_version if git_version is not None else "",
            "goVersion": go_version if go_version is not None else "",
            "major": major if major is not None else "",
            "minor": minor if minor is not None else "",
            "platform": platform if platform is not None else "",
        }
        self._types = {
            "buildDate": (str, None),
            "compiler": (str, None),
            "gitCommit": (str, None),
            "gitTreeState": (str, None),
            "gitVersion": (str, None),
            "goVersion": (str, None),
            "major": (str, None),
            "minor": (str, None),
            "platform": (str, None),
        }

    @property
    def build_date(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("buildDate"),
        )

    @build_date.setter
    def build_date(self, value: str):
        """"""
        self._properties["buildDate"] = value

    @property
    def compiler(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("compiler"),
        )

    @compiler.setter
    def compiler(self, value: str):
        """"""
        self._properties["compiler"] = value

    @property
    def git_commit(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("gitCommit"),
        )

    @git_commit.setter
    def git_commit(self, value: str):
        """"""
        self._properties["gitCommit"] = value

    @property
    def git_tree_state(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("gitTreeState"),
        )

    @git_tree_state.setter
    def git_tree_state(self, value: str):
        """"""
        self._properties["gitTreeState"] = value

    @property
    def git_version(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("gitVersion"),
        )

    @git_version.setter
    def git_version(self, value: str):
        """"""
        self._properties["gitVersion"] = value

    @property
    def go_version(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("goVersion"),
        )

    @go_version.setter
    def go_version(self, value: str):
        """"""
        self._properties["goVersion"] = value

    @property
    def major(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("major"),
        )

    @major.setter
    def major(self, value: str):
        """"""
        self._properties["major"] = value

    @property
    def minor(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("minor"),
        )

    @minor.setter
    def minor(self, value: str):
        """"""
        self._properties["minor"] = value

    @property
    def platform(self) -> str:
        """"""
        return typing.cast(
            str,
            self._properties.get("platform"),
        )

    @platform.setter
    def platform(self, value: str):
        """"""
        self._properties["platform"] = value

    def __enter__(self) -> "Info":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
