class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        
        for i in nums:
            if i<pivot:
                a.append(i)
            elif i==pivot:
                b.append(i)
            else:
                c.append(i)
        a.extend(b)
        a.extend(c)
        return a