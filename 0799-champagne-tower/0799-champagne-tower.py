class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (i + 1) for i in range(100)]
        
        tower[0][0] = poured
        
        for row in range(query_row):
            for glass in range(row + 1):
                if tower[row][glass] > 1:
                    overflow = (tower[row][glass] - 1) / 2
                    tower[row][glass] = 1
                    tower[row + 1][glass] += overflow
                    tower[row + 1][glass + 1] += overflow
        
        return min(1, tower[query_row][query_glass])