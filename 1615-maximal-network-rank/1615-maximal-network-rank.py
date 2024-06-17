class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = defaultdict(set)

        for road in roads:
            a, b = road
            degree[a] += 1
            degree[b] += 1
            connected[a].add(b)
            connected[b].add(a)

        max_network_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                current_rank = degree[i] + degree[j]
                if j in connected[i]:
                    current_rank -= 1
                max_network_rank = max(max_network_rank, current_rank)

        return max_network_rank