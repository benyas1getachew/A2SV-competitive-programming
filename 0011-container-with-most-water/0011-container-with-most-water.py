class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        mx=0
        """for i in range(n):
            for j in range(i+1,n):
                k=(j-i)*min(height[j],height[i])
                if k>mx:
                    mx=k"""
        i=0
        j=n-1
        while i<j:
            k=(j-i)*min(height[j],height[i])
            if k>mx:
                mx=k
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        
        return mx