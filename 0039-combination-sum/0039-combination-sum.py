class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(combination[:])
                return
            for i in range(start, len(candidates)):
                current = candidates[i]
                if current > remaining:
                    break  
                combination.append(current)
                backtrack(remaining - current, combination, i)  
                combination.pop()  
        backtrack(target, [], 0)
        return result
