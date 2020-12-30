import typing

import kuber
from kuber.latest import core_v1


def _make_pod(name: str) -> core_v1.Pod:
    """Creates a pod with the given name to use in testing."""
    return core_v1.Pod(metadata=core_v1.ObjectMeta(name=name))


def _initialize_bundle() -> kuber.ResourceBundle:
    """Creates an initial bundle populated with pod resources."""
    bundle = kuber.ResourceBundle(bundle_name="test", kubernetes_version="latest")
    bundle.push(_make_pod("p1"))
    bundle.push(_make_pod("p2"))
    bundle.push(_make_pod("p3"))
    bundle.push(_make_pod("p4"))
    bundle.push(_make_pod("p5"))
    return bundle


def _get_names(bundle: kuber.ResourceBundle) -> typing.List[str]:
    return [getattr(r.metadata, "name", "") for r in bundle.resources]


def test_move_to():
    """Should move p5 between p1 and p2."""
    bundle = _initialize_bundle()
    bundle.move_to(1, bundle.get("p5"))
    assert _get_names(bundle) == ["p1", "p5", "p2", "p3", "p4"]


def test_move_to_self_referential():
    """Should move p1 to begining where it started."""
    bundle = _initialize_bundle()
    bundle.move_to(0, bundle.get("p1"))
    assert _get_names(bundle) == ["p1", "p2", "p3", "p4", "p5"]


def test_move_after():
    """Should move p5 between p2 and p3."""
    bundle = _initialize_bundle()
    bundle.move_after(bundle.get("p2"), bundle.get("p5"))
    assert _get_names(bundle) == ["p1", "p2", "p5", "p3", "p4"]


def test_move_to_multiple():
    """Should move p4 and p5 between p1 and p2."""
    bundle = _initialize_bundle()
    bundle.move_to(1, bundle.get("p4"), bundle.get("p5"))
    assert _get_names(bundle) == ["p1", "p4", "p5", "p2", "p3"]


def test_move_after_multiple():
    """Should move p3 and p5 between p1 and p2."""
    bundle = _initialize_bundle()
    bundle.move_after(bundle.get("p2"), bundle.get("p3"), bundle.get("p5"))
    assert _get_names(bundle) == ["p1", "p3", "p5", "p2", "p4"]


def test_insert_after_multiple():
    """Should insert p6 and p7 after p3."""
    bundle = _initialize_bundle()
    bundle.insert_after(bundle.get("p3"), _make_pod("p6"), _make_pod("p7"))
    assert _get_names(bundle) == ["p1", "p2", "p3", "p6", "p7", "p4", "p5"]


def test_insert_after_none():
    """Should insert p6 at the beginning if None is specified."""
    bundle = _initialize_bundle()
    bundle.insert_after(None, _make_pod("p6"))
    assert _get_names(bundle) == ["p6", "p1", "p2", "p3", "p4", "p5"]


def test_add_after():
    """Should add p6 after p4."""
    bundle = _initialize_bundle()
    bundle.add_after(bundle.get("p4"), "v1", "Pod", "p6")
    assert _get_names(bundle) == ["p1", "p2", "p3", "p4", "p6", "p5"]


def test_new_after():
    """Should add p6 after p4."""
    bundle = _initialize_bundle()
    pod = bundle.new_after(bundle.get("p4"), "v1", "Pod", "p6")
    assert _get_names(bundle) == ["p1", "p2", "p3", "p4", "p6", "p5"]
    assert getattr(pod.metadata, "name") == "p6"
