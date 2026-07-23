# 1396. Design Underground System

Medium — Design / Hash Map

An underground subway system tracks customer travel times between stations.

Implement the `UndergroundSystem` class:

- `UndergroundSystem()` — Initializes the system.
- `checkIn(id, stationName, t)` — A customer with id `id` checks in at station `stationName` at time `t`.
- `checkOut(id, stationName, t)` — A customer with id `id` checks out at station `stationName` at time `t`.
- `getAverageTime(startStation, endStation)` — Returns the average travel time between `startStation` and `endStation` for all trips that have completed so far.

Rules:

- A customer can only be checked into **one** station at a time.
- There may be multiple customers traveling at once.
- Travel time for a trip is `checkOutTime - checkInTime`.
- Average is over **all** completed trips between that station pair (order matters: A→B is not B→A).
- You may assume `getAverageTime` is only called for pairs that have at least one completed trip.
- Times `t` are strictly increasing for each customer’s own check-ins/check-outs, but different customers can interleave.

## Constraints

- `1 <= id, t <= 10^6`
- `1 <= stationName.length, startStation.length, endStation.length <= 10`
- All strings consist of uppercase and lowercase English letters and digits
- At most `2 * 10^4` calls in total to `checkIn`, `checkOut`, and `getAverageTime`

## Example 1

```
Input:
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output:
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
```

Explanation:

- Customer 45: Leyton → Waterloo in `15 - 3 = 12`
- Customer 32: Paradise → Cambridge in `22 - 8 = 14`
- Customer 27: Leyton → Waterloo in `20 - 10 = 10`
- `getAverageTime("Paradise","Cambridge")` → `14`
- `getAverageTime("Leyton","Waterloo")` → `(12 + 10) / 2 = 11`
- Customer 10: Leyton → Waterloo in `38 - 24 = 14`
- `getAverageTime("Leyton","Waterloo")` → `(12 + 10 + 14) / 3 = 12`

## Hints

- This is a **class design** problem: store state on `self`, not in globals.
- Use a **dictionary** keyed by customer `id` to remember where/when they checked in.
- Use another **dictionary** keyed by `(startStation, endStation)` to accumulate total travel time and trip count.
- On `checkOut`, look up the check-in, compute duration, update the route stats, then remove that customer from the check-in map.
- `getAverageTime` is just `total_time / trip_count` for that route key.

## Practice

Edit `solution.py` and run tests:

```bash
pytest
```

Debug in Cursor: open `solution.py`, set breakpoints, run **Debug Tests** or **Debug Current Test File**.


## Questions

Hows the contrains important? What does each supposed to tell me?
