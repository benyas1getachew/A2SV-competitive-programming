class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=len(nums)
        for i in range(k+1):
            if not (i in nums):
                return i