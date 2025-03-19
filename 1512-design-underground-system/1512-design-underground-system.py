class UndergroundSystem:

    def __init__(self):
        self.customer_info = {}
        self.stations = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_info[id] = (stationName, t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starting_station, checkin_time = self.customer_info[id]
        key = (starting_station, stationName)
        total_time, count = self.stations.get(key, (0, 0))
        self.stations[key] = (total_time + (t - checkin_time), count + 1)
        del self.customer_info[id]

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stations[(startStation, endStation)][0] / self.stations[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)