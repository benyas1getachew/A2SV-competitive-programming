class FrequencyTracker:

    def __init__(self):
        self.arr=[]
        self.dicts={}
        self.d2={}
        self.g=False
    def add(self, number: int) -> None:
        self.g=False
        try:
            self.dicts[number]+=1
        except:
            self.dicts[number]=1
    def deleteOne(self, number: int) -> None:
        
        try:
            self.g=False
            self.dicts[number]-=1
            if self.dicts[number]<=0:
                del self.dicts[number]
        except:
            pass
        
    def hasFrequency(self, frequency: int) -> bool:
        if self.g:
            return frequency in self.d2
        else:
            self.d2={v: k for k, v in self.dicts.items()}
            self.g=True
            return frequency in self.d2
        

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)