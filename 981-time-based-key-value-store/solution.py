from __future__ import annotations


class TimeMap:
    def __init__(self) -> None:
        self.maps = {}

    def set(self, key:str, value: str, ts: int) -> None:
        if key not in self.maps:
            self.maps[key] = {}
        self.maps[key][ts] = value

    def search_ts(self, ts_list, ts) -> int | None:
        left, right = 0, len(ts_list) - 1
        result = None 

        while left <= right:
            mid = (left + right)//2
            if ts_list[mid] <= ts:
                result =  ts_list[mid]
                left = mid + 1
            else:
                right = mid - 1
        return result

    def get(self, key:str, ts: int) -> str:
        value = ""
        if key in self.maps:
            ts = self.search_ts(list(self.maps[key].keys()),ts)
            if ts is not None: 
                value = self.maps[key][ts]
        return value