class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dicts={}
        n=(len(nums)//3)
        for i in nums:
            try:
                dicts[i]+=1
            except:
                dicts[i]=1
        
        ans=[]
        for key,val in dicts.items():
            if val > n:
                ans.append(key)
        return ans