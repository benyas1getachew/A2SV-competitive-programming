class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a=[]
        for k in points:
            a.append(k[0])
        a.sort()
        mx=0
        for i in range(len(a)-1):
            if a[i+1]-a[i]>mx:
                mx=a[i+1]-a[i]
        return mx
        