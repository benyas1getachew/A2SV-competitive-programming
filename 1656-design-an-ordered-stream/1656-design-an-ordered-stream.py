class OrderedStream:

    def __init__(self, n: int):
        self.n=n
        self.ptr=1
        self.my={i: '' for i in range(1, n+1)}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.my[idKey]=value
        arr=[]
        for i in range(self.ptr,self.n+1):
            if len(self.my[i])>1:
                arr.append(self.my[i])
                self.ptr+=1
            else:
                break
        return arr
            

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)