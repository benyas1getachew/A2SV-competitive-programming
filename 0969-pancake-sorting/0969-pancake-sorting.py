class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ku=sorted(arr)
        if arr==ku:
            return []
        n=len(arr)
        def flip(ar,k,l):
            bs=ar[:k]
            bs.reverse()
            ar[:k]=bs
            bs=ar[:l]
            bs.reverse()
            arr[:l]=bs
            return ar
        
        def find(ar,l):
            b=sorted(ar)
            return ar.index(b[-l])
        ps=[]
        for i in range(1,n+1):
            m=find(arr,i)
            
            ps.append(m+1)
            ps.append(n-i+1)
            arr=flip(arr,m+1,n-i+1)
        print(arr)
        return ps