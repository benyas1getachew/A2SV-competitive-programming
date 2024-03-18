class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        target_indices = []

        for i, num in enumerate(sorted_nums):
            if num == target:
                target_indices.append(i)

        return target_indices