class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        candidate_3 = float('-inf')

        for num in reversed(nums):
            if num < candidate_3:
                return True
            while stack and stack[-1] < num:
                candidate_3 = stack.pop()
            stack.append(num)

        return False