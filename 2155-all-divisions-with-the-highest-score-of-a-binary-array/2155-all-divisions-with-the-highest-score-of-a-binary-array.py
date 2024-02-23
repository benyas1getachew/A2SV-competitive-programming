class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        maxs=0
        arr=[]
        dics={}
        dics["r"]=[nums.count(0),nums.count(1)]
        dics["l"]=[0,0]
        for i in range(len(nums)+1):
            tsum=dics["l"][0]+dics["r"][1]
            if maxs==tsum:
                arr.append(i)
            elif tsum>maxs:
                arr=[]
                arr.append(i)
                maxs=tsum
            if i==len(nums):
                break
            if nums[i]==0:
                dics["r"][0]-=1
                dics["l"][0]+=1
            else:
                dics["r"][1]-=1
                dics["l"][1]+=1
                
        return arr