class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dct={}
        for i in range(len(nums)):
            try:
                dct[nums[i]].append(i)
            except:
                dct[nums[i]]=[i]
        nums.sort()
        n=len(nums)
        arr=nums.copy()
        for i in range(1,len(nums)+1):
            try:
                while nums[-i]==nums[-i-1]:
                    i+=1
            except:
                pass
            for k in dct[nums[-i]]:
                arr[k]=n-i
        return arr
            