class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        def find(x):
            if parents[x] != x:
                origin = parents[x]
                parents[x] = find(parents[x])
                weights[x] *= weights[origin]
            return parents[x]
        
        def union(x, y, val):
            root_x = find(x)
            root_y = find(y)
            
            if root_x != root_y:
                parents[root_x] = root_y
                weights[root_x] = weights[y] * val / weights[x]
        
        parents = {}
        weights = {}
        
        for (A, B), val in zip(equations, values):
            if A not in parents:
                parents[A] = A
                weights[A] = 1.0
            if B not in parents:
                parents[B] = B
                weights[B] = 1.0
            
            union(A, B, val)
            union(B, A, 1 / val)
        
        results = []
        
        for C, D in queries:
            if C not in parents or D not in parents:
                results.append(-1.0)
                continue
            
            root_C = find(C)
            root_D = find(D)
            
            if root_C != root_D:
                results.append(-1.0)
            else:
                results.append(weights[C] / weights[D])
        
        return results