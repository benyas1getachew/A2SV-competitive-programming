class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h=0
        k=0
        n=len(nums)
        f=len(nums)
        rm=[]
        i=0
        while i< f:
            if nums[i]!=h:
                h=nums[i]
                k=1
            elif k>=2:
                nums.remove(nums[i])
                f-=1
                continue
            else:
                k+=1
            i+=1
        print(nums)
        return len(nums) 
                
                
        