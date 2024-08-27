class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=len(nums)
        nums.sort()
        for i in range(k):
            if i != nums[i]:
                return i
        return k