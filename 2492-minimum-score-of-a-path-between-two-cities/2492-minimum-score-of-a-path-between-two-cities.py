class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        min_score = float('inf')
        visited = set()
        queue = deque([1])

        while queue:
            city = queue.popleft()

            for neighbor, dist in graph[city]:
                min_score = min(min_score, dist)  
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return min_score