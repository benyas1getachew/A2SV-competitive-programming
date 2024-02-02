class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        no=0
        j1=0
        j2=0
        if len(strs)==1:
            j1=len(strs[0])+1
        for i in range(max(len(s) for s in strs)):
            k=strs[0]
            for s in strs:
                try:
                    if s[i]==k[i]:
                        continue
                    else:
                        no=1
                        break
                except:
                    no=1
                    break
            if no==1:
                j2=i
                break
            j2=i+1
        j3=max(j1,j2)
        return strs[0][:j3]