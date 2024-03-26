class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        arr.append(nums[0])
        for i in range(1,len(nums)):
            arr.append(arr[i-1]+nums[i])
        
        return arr