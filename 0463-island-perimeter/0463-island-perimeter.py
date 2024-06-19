class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per=0
        row=(len(grid))
        print(row)
        for i in range(row):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    try:
                        if grid[i][j-1]==1 and j-1>=0:
                            pass
                        else:
                            per+=1
                    except:
                        per+=1
                    try:
                        if grid[i][j+1]==1 :
                            pass
                        else:
                            per+=1
                    except:
                        per+=1
                    try:
                        if grid[i-1][j]==1 and i-1>=0:
                            pass
                        else:
                            per+=1
                    except:
                        per+=1
                    try:
                        if grid[i+1][j]==1:
                            pass
                        else:
                            per+=1
                    except:
                        per+=1
        return per