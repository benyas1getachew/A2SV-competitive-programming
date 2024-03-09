class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt=0
        i=0
        j=0
        k=0
        n=len(chars)
        while i<len(chars):
            if j>=len(chars):
                chars.insert(k,chars[i])
                k+=1
                j+=1
                i+=1
                if cnt>1:
                    values = list(str(cnt))
                    for digit in values:
                        chars.insert(k, digit)
                        k+=1
                        j+=1
                        i+=1
                break
            if chars[i]==chars[j]:
                cnt+=1
                j+=1
            else:
                chars.insert(k,chars[i])
                k+=1
                j+=1
                i+=1
                if cnt>1:
                    values = list(str(cnt))
                    for digit in values:
                        chars.insert(k, digit)
                        k+=1
                        j+=1
                        i+=1
                i=j
                cnt=0
        print(chars)
        t=len(chars)-n
        print(t)
        return t
            