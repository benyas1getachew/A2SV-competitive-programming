class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1: 
            return -1
        tr={i: [0,0] for i in range(1, n + 1)} #trusted by
        for t in trust:
            tr[t[0]][0]+=1
            tr[t[1]][1]+=1
        for k in tr:
            if tr[k][1]==n-1:
                if tr[k][0]>0:
                    break
                else:
                    return k
        return -1
            