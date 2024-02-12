class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x=0
        while True:
            if n==2**x:
                return True
            elif n>2**x:
                x+=1
            else:
                return False