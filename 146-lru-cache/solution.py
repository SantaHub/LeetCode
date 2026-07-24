from __future__ import annotations


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {} # {1: 3}

    def get(self, key: int) -> int:
        value = -1
        if key in self.cache:
            value = self.cache.pop(key)
            self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        key_list = list(self.cache.keys())
        if len(key_list) >= self.capacity: # Make this while if keylist can be off by more than 1.
            self.cache.pop(key_list[0])
        self.cache[key] = value
