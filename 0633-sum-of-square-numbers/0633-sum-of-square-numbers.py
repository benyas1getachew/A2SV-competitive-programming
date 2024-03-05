class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        dct={}
        for i in range((c//2)+2):
            dct[i*i]=i
            if c-(i*i) in dct:
                return True
            elif (i*i)>c:
                    break
        return False