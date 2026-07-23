import pytest

from solution import TimeMap


@pytest.fixture
def store() -> TimeMap:
    return TimeMap()


def test_leetcode_example_1(store: TimeMap):
    store.set("foo", "bar", 1)
    assert store.get("foo", 1) == "bar"
    assert store.get("foo", 3) == "bar"
    store.set("foo", "bar2", 4)
    assert store.get("foo", 4) == "bar2"
    assert store.get("foo", 5) == "bar2"


def test_missing_key_returns_empty(store: TimeMap):
    assert store.get("missing", 1) == ""


def test_query_before_first_timestamp(store: TimeMap):
    store.set("foo", "bar", 10)
    assert store.get("foo", 9) == ""
    assert store.get("foo", 10) == "bar"


def test_independent_keys(store: TimeMap):
    store.set("a", "one", 1)
    store.set("b", "two", 1)
    store.set("a", "uno", 2)
    assert store.get("a", 1) == "one"
    assert store.get("a", 2) == "uno"
    assert store.get("b", 2) == "two"


def test_multiple_versions_pick_latest_not_exceeding(store: TimeMap):
    store.set("x", "v1", 1)
    store.set("x", "v2", 3)
    store.set("x", "v3", 7)
    assert store.get("x", 1) == "v1"
    assert store.get("x", 2) == "v1"
    assert store.get("x", 3) == "v2"
    assert store.get("x", 6) == "v2"
    assert store.get("x", 7) == "v3"
    assert store.get("x", 100) == "v3"
