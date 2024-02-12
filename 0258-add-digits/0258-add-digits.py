class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            num=str(num)
            if len(num)<2:
                return int(num)
            cnt=0
            for i in num:
                cnt+=int(i)
            num=cnt