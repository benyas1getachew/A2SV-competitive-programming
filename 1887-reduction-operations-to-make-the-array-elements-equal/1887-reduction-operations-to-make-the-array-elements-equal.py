class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        se=sorted(set(nums), reverse=True)
        cnt=0
        k=0
        t=0
        while k<len(nums):
            try:
                if nums[k]==se[t] and len(se)>1:
                    cnt+=len(se)-1-t
                    k+=1
                else:
                    t+=1
            except:
                break
        return cnt
            