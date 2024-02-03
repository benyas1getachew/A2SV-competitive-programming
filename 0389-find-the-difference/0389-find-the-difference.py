class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        a=list(t)
        for i in a:
            try:
                s.remove(i)
                t.remove(i)
            except:
                continue
        return t[0]
                    