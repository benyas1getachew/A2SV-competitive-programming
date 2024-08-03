class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)

        for ai, bi in richer:
            graph[bi].append(ai)

        answer = [-1] * n

        def dfs(node):
            if answer[node] != -1:
                return answer[node]

            min_person = node
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[min_person]:
                    min_person = candidate

            answer[node] = min_person
            return min_person

        for i in range(n):
            dfs(i)

        return answer
