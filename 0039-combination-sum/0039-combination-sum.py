class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                combination.append(candidate)
                backtrack(remaining - candidate, combination, i)
                combination.pop()

        candidates.sort()  
        result = []
        backtrack(target, [], 0)
        return result