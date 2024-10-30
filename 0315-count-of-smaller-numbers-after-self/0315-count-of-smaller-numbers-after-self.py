class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = []

        for num in reversed(nums):
            left, right = 0, len(sorted_nums)

            while left < right:
                mid = (left + right) // 2
                if sorted_nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            res.append(left)
            sorted_nums.insert(left, num)

        return res[::-1]