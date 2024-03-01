class Solution:
    def smallestNumber(self, num: int) -> int:
        j=0
        if num==0:
            return 0
        if num<0:
            num=abs(num)
            j=1
        dig= [int(char) for char in str(num)]
        if j==0:
            dig.sort()
            a=dig.copy()
            k=[]
            i=0
            while i<len(dig):
                if len(k)<1 and dig[i]==0:
                    i+=1
                elif len(k)<1 and dig[i]>0:
                    k.append(dig[i])
                    dig.remove(dig[i])
                    i=0
                else:
                    k.append(dig[i])
                    i+=1
            return int(''.join(map(str, k)))
        else:
            dig.sort(reverse=True)
            return -int(''.join(map(str, dig)))

                
            
        