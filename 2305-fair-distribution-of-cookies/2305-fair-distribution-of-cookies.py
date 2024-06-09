class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(index, distribution):
            if index == len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(distribution))
                return

            for i in range(k):
                distribution[i] += cookies[index]
                backtrack(index + 1, distribution)
                distribution[i] -= cookies[index]
                if distribution[i] == 0:
                    break

        self.min_unfairness = float('inf')
        backtrack(0, [0] * k)
        return self.min_unfairness