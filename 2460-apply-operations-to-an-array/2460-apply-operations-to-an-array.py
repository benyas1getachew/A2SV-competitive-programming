class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            try:
                if nums[i]==nums[i+1]:
                    nums[i]*=2
                    nums[i+1]=0
            except:
                pass
        cnt=0
        for i in range(len(nums)):
            if nums[i]>0:
                nums[cnt],nums[i]=nums[i],nums[cnt]
                cnt+=1
        return nums