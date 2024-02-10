class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=list(a)
        b=list(b)
        
        res_a=0
        cnt=0
        for i in range(1,len(a)+1):
            if int(a[-i])==1:
                res_a+=2**cnt
            cnt+=1
        res_b=0
        cnt=0
        for i in range(1,len(b)+1):
            if int(b[-i])==1:
                res_b+=2**cnt
            cnt+=1
        ans=res_a+res_b
        ans=bin(ans)[2:]
        return ans