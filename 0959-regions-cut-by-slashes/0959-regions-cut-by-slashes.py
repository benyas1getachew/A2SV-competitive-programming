class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))
        rank = [1] * (4 * n * n)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(index + 0, index + 3)
                    union(index + 1, index + 2)
                elif grid[i][j] == '\\':
                    union(index + 0, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index + 0, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)

                if j + 1 < n:
                    union(index + 1, 4 * (i * n + (j + 1)) + 3)
                if i + 1 < n:
                    union(index + 2, 4 * ((i + 1) * n + j) + 0)
        
        return len(set(find(x) for x in range(4 * n * n)))