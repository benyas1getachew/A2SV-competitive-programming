class Solution:
    def isHappy(self, n: int) -> bool:
        res=[]
        res.append(n)
        while True:
            ls=list(map(int, str(res[-1])))
            if len(ls)>1:
                new=sum(i**2 for i in ls)
            else:
                new=ls[0]**2  
                print(ls[0])
            if new in res and new!=1:
                return False
            elif new==1:
                return True
            else:
                res.append(new)