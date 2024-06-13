class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1: 
            return -1
        tr={i: 0 for i in range(1, n + 1)} #trusted by
        tr2={i: 0 for i in range(1, n + 1)} # trusts
        for t in trust:
            tr2[t[0]]+=1
            tr[t[1]]+=1
        for k in tr:
            if tr[k]==n-1:
                if tr2[k]>0:
                    break
                else:
                    return k
        return -1
            