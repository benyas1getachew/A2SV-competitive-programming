class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for row in range(n - 2, -1, -1):
            for col in range(n):
                min_path = matrix[row + 1][col]
                
                if col > 0:
                    min_path = min(min_path, matrix[row + 1][col - 1])
                
                if col < n - 1:
                    min_path = min(min_path, matrix[row + 1][col + 1])
                
                matrix[row][col] += min_path
        
        return min(matrix[0])