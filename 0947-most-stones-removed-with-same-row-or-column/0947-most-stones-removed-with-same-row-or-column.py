class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}

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

        def add(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0

        for x, y in stones:
            add(x)              
            add(y + 10001)      
            union(x, y + 10001) 

        unique_roots = set()
        for x, y in stones:
            unique_roots.add(find(x))

        return len(stones) - len(unique_roots)