import pytest

from solution import LRUCache


def test_leetcode_example_1():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_get_missing_returns_minus_one():
    cache = LRUCache(1)
    assert cache.get(99) == -1


def test_update_existing_key_does_not_evict():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # update, still capacity 2
    assert cache.get(1) == 10
    assert cache.get(2) == 2


def test_get_marks_key_as_recent():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # 1 becomes most recent
    cache.put(3, 3)  # should evict 2, not 1
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_put_existing_moves_to_recent():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 100)  # 1 becomes most recent
    cache.put(3, 3)  # should evict 2
    assert cache.get(2) == -1
    assert cache.get(1) == 100
    assert cache.get(3) == 3
