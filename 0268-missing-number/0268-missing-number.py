class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = len(nums)
        dicts = {i: 0 for i in range(k+1)}
        
        for num in nums:
            dicts[num] = 1
        
        for i in range(k+1):
            if dicts[i] == 0:
                return i