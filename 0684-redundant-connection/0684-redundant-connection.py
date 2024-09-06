class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]  
        rank = [1] * (n + 1)  
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
                return True
            else:
                return False

        for u, v in edges:
            if not union(u, v): 
                return [u, v]