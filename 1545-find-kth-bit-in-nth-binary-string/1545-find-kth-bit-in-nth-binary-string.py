class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(char):
            return '1' if char == '0' else '0'

        def findKthBitRecursive(n, k):
            if n == 1:
                return '0'

            length = (1 << n) - 1  
            mid = length // 2 + 1

            if k == mid:
                return '1'
            elif k < mid:
                return findKthBitRecursive(n - 1, k)
            else:
                k_mirror = length - k + 1
                return invert(findKthBitRecursive(n - 1, k_mirror))

        return findKthBitRecursive(n, k)