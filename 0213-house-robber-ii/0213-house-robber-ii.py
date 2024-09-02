class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])

            return dp[-1]

        max_profit_case1 = rob_linear(nums[:-1])
        max_profit_case2 = rob_linear(nums[1:])

        return max(max_profit_case1, max_profit_case2)