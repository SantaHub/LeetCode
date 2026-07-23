from __future__ import annotations

class Ride: 
    def __init__(self, checkIn: int,  checkInStation: str) -> None:
        self.checkIn= checkIn
        self.checkInStation = checkInStation
        

class AvgTime:
    def __init__(self, totalDuration: int) -> None:
        self.totalDuration = totalDuration
        self.tripCount = 1
    def addToTrip(self, duration: int) -> None:
        self.totalDuration += duration
        self.tripCount +=1

    def getAvgTime(self) -> float:
        return (self.totalDuration/self.tripCount)

class UndergroundSystem:
    def __init__(self) -> None:
        """
        Track check-ins and completed trip averages between stations.
        Hint: keep customer check-ins in one dict, route totals in another.
        """
        self.activeRides: dict[int, Ride] = {}
        self.avgTime: dict[str, dict[str, AvgTime]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """Record that customer `id` entered `stationName` at time `t`."""
        if id in self.activeRides:
            raise ValueError(f"Customer already in active ride. {id}")
        self.activeRides[id] = Ride(t, stationName)
        if stationName not in self.avgTime:
            self.avgTime[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """
        Customer `id` leaves at `stationName` at time `t`.
        Update average stats for the completed start -> end trip.
        """
        ride = self.activeRides[id]
        duration = t - ride.checkIn
        if ride.checkInStation in self.avgTime and stationName in self.avgTime[ride.checkInStation]:
            self.avgTime[ride.checkInStation][stationName].addToTrip(duration)
        else:
            self.avgTime[ride.checkInStation][stationName] = AvgTime(duration)

        del self.activeRides[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        """Return average travel time from startStation to endStation."""
        return self.avgTime[startStation][endStation].getAvgTime()