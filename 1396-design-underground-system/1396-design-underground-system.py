class UndergroundSystem:

    def __init__(self):
        self.check_in={}
        self.travel_time={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        st,tm=self.check_in[id]
        nw=t-tm
        key=(st,stationName)
        if key in self.travel_time.keys():
            hu,k=self.travel_time[key]
            hu=hu+nw
            k+=1
            self.travel_time[key]=[hu,k]
        else:
            self.travel_time[key]=[nw,1]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        hu,k=self.travel_time[(startStation,endStation)]
        return hu/k


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)