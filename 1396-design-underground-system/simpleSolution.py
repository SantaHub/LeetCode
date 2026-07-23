class UndergroundSystem:
    def __init__(self):
        self.active_ride = {}
        self.avg_time = {}

    def checkIn(self, id: int, station_name: str, time: int) -> None:
        if id in self.active_ride:
            raise ValueError(f"{id} already checked in")

        self.active_ride[id] = (station_name, time)
        if station_name not in self.avg_time:
            self.avg_time[station_name] = {}
    
    def checkOut(self, id:int , station_name:str, time:int) -> None:
        if id not in self.active_ride:
            raise ValueError(f"{id} Customer was not checkedin")
        
        in_station, in_time  = self.active_ride[id]
        avg_time_obj = self.avg_time[in_station]
        duration = time - in_time
        count = 1
        if station_name in avg_time_obj:
            total_duration, total_count =  self.avg_time[in_station][station_name]
            duration += total_duration
            count += total_count

        del self.active_ride[id]
        self.avg_time[in_station][station_name] = (duration, count)

    def getAverageTime(self, in_station: str, out_station: str) -> float:
        duration, count = self.avg_time[in_station][out_station]
        return duration/count

        

