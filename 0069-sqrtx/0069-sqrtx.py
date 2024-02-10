class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        for i in range(1,x+1):
            if x//i==i:
                return i
            elif x//i<i:
                return i-1