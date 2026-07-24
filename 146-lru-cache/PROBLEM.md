# 146. LRU Cache

Medium — Design / Hash Map / Doubly Linked List

Design a data structure that follows the constraints of a **Least Recently Used (LRU)** cache.

Implement the `LRUCache` class:

- `LRUCache(capacity)` — Initialize the cache with positive size `capacity`.
- `get(key)` — Return the value of `key` if it exists, otherwise return `-1`.
- `put(key, value)` — Update the value of `key` if it exists. Otherwise, add the key-value pair. If the number of keys exceeds `capacity`, evict the **least recently used** key.

Rules:

- Both `get` and `put` must run in **O(1)** average time.
- A key is "used" when it is inserted or accessed via `get` / `put`.
- When capacity is exceeded, remove the key that was used furthest in the past.

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls to `get` and `put`

## Example 1

```
Input:
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

Output:
[null,null,null,1,null,-1,null,-1,3,4]
```

Explanation:

- `LRUCache(2)` — capacity 2
- `put(1, 1)` — cache: `{1=1}`
- `put(2, 2)` — cache: `{1=1, 2=2}`
- `get(1)` → `1` — cache: `{2=2, 1=1}` (1 is now most recent)
- `put(3, 3)` — evicts key `2` — cache: `{1=1, 3=3}`
- `get(2)` → `-1` (not found)
- `put(4, 4)` — evicts key `1` — cache: `{3=3, 4=4}`
- `get(1)` → `-1`
- `get(3)` → `3`
- `get(4)` → `4`

## Hints (DS practice)

- A plain `dict` alone is not enough if you need O(1) eviction of the least recently used key.
- Classic approach: **hash map** (`key → node`) + **doubly linked list** (most recent at one end, least recent at the other).
- On `get`/`put` of an existing key: move that node to the "most recent" end.
- On `put` when at capacity: remove the node at the "least recent" end, then insert the new one.
- Python shortcut (fine to know, but interviewers often want the list): `collections.OrderedDict` with `move_to_end` / `popitem(last=False)`.

## Practice

Edit `solution.py` and run tests:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Debug in Cursor: open `solution.py`, set breakpoints, run **Debug Tests**.
