class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        col=len(grid[0])
        row=len(grid)
        m_sum=0
        for i in range(row):
            for j in range(col):
                if j+2<col and i+2<row:
                    t_sum=grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                    if t_sum>m_sum:
                        m_sum=t_sum
        return m_sum