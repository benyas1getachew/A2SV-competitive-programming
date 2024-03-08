class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        t=True
        k=0
        cnt=0
        mx=0
        f=2
        t=2
        for i in range(1,len(arr)):
            if arr[i-1]<arr[i] and k==0:
                
                cnt+=1
                f=0
                if t==0:
                    t=2
            elif arr[i-1]>arr[i]:
                if f==0:
                    t=0
                k=1
                cnt+=1
                
                print(i,cnt)
            elif arr[i-1]<arr[i] and k==1:
                k=0
                if cnt+1>mx and t==0 and f==0:
                    mx=cnt+1
                cnt=1
                f=0
                if t==0:
                    t=2
            elif arr[i-1]==arr[i]:
                if cnt+1>mx and t==0 and f==0:
                    mx=cnt+1
                cnt=0
                f=2
            if i==len(arr)-1:
                if cnt+1>mx and t==0 and f==0:
                    mx=cnt+1
        
        return mx