class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        for i in range(len(strs[0])):
            arr=[]
            for j in range(len(strs)):
                arr.append(strs[j][i])
            if arr!=sorted(arr):
                cnt+=1
        return cnt
        