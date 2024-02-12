class Solution:
    def doUnion(self,a,n,b,m):
        a.extend(b)
        a=set(a)
        return len(a)
