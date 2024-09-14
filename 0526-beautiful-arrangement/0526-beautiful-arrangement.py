class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(i):
            if i > n:
                return 1

            count = 0
            for num in range(1, n+1):
                if not visited[num] and (num % i == 0 or i % num == 0):
                    visited[num] = True
                    count += backtrack(i + 1)
                    visited[num] = False
            return count

        visited = [False] * (n + 1)
        return backtrack(1)