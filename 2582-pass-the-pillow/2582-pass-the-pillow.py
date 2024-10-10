class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1) 
        t = time % cycle_length     
        if t < n: 
            return t + 1
        else:      
            return n - (t - (n - 1))