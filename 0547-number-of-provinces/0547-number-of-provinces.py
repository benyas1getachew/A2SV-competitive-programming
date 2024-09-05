class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = True
            for other_city in range(n):
                if isConnected[city][other_city] == 1 and not visited[other_city]:
                    dfs(other_city)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces