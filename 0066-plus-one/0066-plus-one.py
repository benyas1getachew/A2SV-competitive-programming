class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        res=[]
        for i in range(1,len(digits)+1):
            try:
                if digits[-i]==10:
                    digits[-i]=0
                    digits[-i-1]+=1
            except:
                digits.insert(0,1)
                break
        return digits
        