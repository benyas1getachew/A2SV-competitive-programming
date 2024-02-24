class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dics={}
        for i in strs:
            for j in range(len(i)):
                try:
                    dics[j].append(i[j])
                except:
                    dics[j]=[i[j]]
        print(dics)
        cnt=0
        for val in dics:
            if dics[val]!=sorted(dics[val]):
                cnt+=1
        return cnt
        