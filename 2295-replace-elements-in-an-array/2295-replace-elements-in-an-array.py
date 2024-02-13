class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dicts = {v: i for i, v in enumerate(nums)}
        for a, b in operations:
            nums[dicts[a]] = b
            dicts[b] = dicts[a]
        return nums