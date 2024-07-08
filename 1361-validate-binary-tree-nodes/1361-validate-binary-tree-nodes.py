class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n 
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                uf[rootY] = rootX
                return True
            return False

        uf = list(range(n))  
        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] != -1:
                    return False 
                parent[leftChild[i]] = i
                if not union(i, leftChild[i]):
                    return False 
            if rightChild[i] != -1:
                if parent[rightChild[i]] != -1:
                    return False  
                parent[rightChild[i]] = i
                if not union(i, rightChild[i]):
                    return False  

        root_count = sum(1 for i in range(n) if parent[i] == -1)
        if root_count != 1:
            return False

        return sum(find(i) == i for i in range(n)) == 1