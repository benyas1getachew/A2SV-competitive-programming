class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        to=0
        for i in nums:
            if i==1:
                count=count+1
            else:
                if count>to:
                    to=count
                count=0
        if count>to:
            to=count
        return to