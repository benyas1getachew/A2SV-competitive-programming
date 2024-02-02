class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        result = n
        while result % 2 != 0:
            result += n

        return result