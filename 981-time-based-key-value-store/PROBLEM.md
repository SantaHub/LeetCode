# 981. Time Based Key-Value Store

Medium — Design / Hash Map / Binary Search

Design a time-based key-value store that can keep **multiple values** for the same key at different timestamps, and retrieve the value as of a given time.

Implement the `TimeMap` class:

- `TimeMap()` — Initializes the store.
- `set(key, value, timestamp)` — Store `value` for `key` at `timestamp`.
- `get(key, timestamp)` — Return the value for `key` at the largest `timestamp_prev` such that `timestamp_prev <= timestamp`. If none exists, return `""`.

Rules:

- All `set` timestamps are **strictly increasing** (you can append; the list stays sorted).
- `get` wants the most recent value **at or before** the query time — not an exact match only.
- Different keys are independent.

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits
- `1 <= timestamp <= 10^7`
- All `set` timestamps are strictly increasing
- At most `2 * 10^5` calls to `set` and `get` combined

## Example 1

```
Input:
["TimeMap","set","get","get","set","get","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]

Output:
[null,null,"bar","bar",null,"bar2","bar2"]
```

Explanation:

- `set("foo", "bar", 1)`
- `get("foo", 1)` → `"bar"`
- `get("foo", 3)` → `"bar"` (no entry at 2 or 3; best is timestamp 1)
- `set("foo", "bar2", 4)`
- `get("foo", 4)` → `"bar2"`
- `get("foo", 5)` → `"bar2"`

## Hints (dict + tuple practice)

- Use a **dict** keyed by `key`, mapping to a **list of tuples**: `(timestamp, value)`.
- On `set`, append a new tuple to that key’s list.
- On `get`, look up the list, then find the rightmost tuple whose timestamp `<=` the query time. Unpack with `ts, val = pair`.
- Because timestamps are strictly increasing, a reverse linear scan is fine to start; binary search (`bisect`) is the interview upgrade for the large call limit.

## Practice

Edit `solution.py` and run tests:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Debug in Cursor: open `solution.py`, set breakpoints, run **Debug Tests**.
