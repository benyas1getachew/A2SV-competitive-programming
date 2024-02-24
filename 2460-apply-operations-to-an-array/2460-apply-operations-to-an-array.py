class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            try:
                if nums[i]==nums[i+1]:
                    nums[i]*=2
                    nums[i+1]=0
            except:
                pass
        arr=[]
        for i in nums:
            if i>0:
                arr.append(i)
        for i in range(len(nums)-len(arr)):
            arr.append(0)
        return arr