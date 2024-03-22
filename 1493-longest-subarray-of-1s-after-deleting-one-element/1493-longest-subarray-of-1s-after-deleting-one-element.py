class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        ones_count = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                ones_count += 1
            while right - left + 1 - ones_count > 1:
                if nums[left] == 1:
                    ones_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length - 1 if max_length > 0 else 0
