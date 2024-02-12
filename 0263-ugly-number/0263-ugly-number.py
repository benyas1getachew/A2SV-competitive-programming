class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for prime in [5,3,2]:
            while n % prime == 0:
                n //= prime
        return n == 1