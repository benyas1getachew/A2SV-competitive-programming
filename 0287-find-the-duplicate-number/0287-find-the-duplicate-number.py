class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dct={}
        for k in nums:
            if k in dct:
                return k
            else:
                dct[k]=1