class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        max_happiness = 0

        for i in range(k):
            effective_happiness = max(0, happiness[i] - i)
            max_happiness += effective_happiness

        return max_happiness