class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 0,0  0,1  1,0  2,0  1,1  0,2  1,2  2,1  2,2
        arr=[]
        up=True
        right=False
        left=False
        down=False
        i=0
        j=0
        c=0
        
        arr.append(mat[i][j])
        while c<len(mat)*len(mat[0]):
            if up:
                try:
                    i-=1
                    j+=1
                    if i<0:
                        raise ValueError("Number cannot be negative")
                    x=mat[i][j]
                    
                    arr.append(mat[i][j])
                except:
                    try:
                        i+=1
                        x=mat[i][j]
                        arr.append(mat[i][j])
                        up=False
                    except:
                        try:
                            i+=1
                            j-=1
                            arr.append(mat[i][j])
                            up=False
                        except:
                            break
            else:
                try:
                    i+=1
                    j-=1
                    if j<0:
                        raise ValueError("Number cannot be negative")
                    x=mat[i-1][j+1]
                    arr.append(mat[i][j])
                except:
                    try:
                        j+=1
                        x=mat[i][j]
                        arr.append(mat[i][j])
                        up=True
                    except:
                        try:
                            i-=1
                            j+=1
                            arr.append(mat[i][j])
                            up=True
                        except:
                            break
            c+=1
        return arr
                    
                    
                