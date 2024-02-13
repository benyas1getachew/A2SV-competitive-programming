class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split(" ")
        ans=[]
        for i in range(1,len(arr)+1):
            if len(arr[-i])>=1:
                ans.append(arr[-i])
        return " ".join(ans)