class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        a=sorted(A)
        b=sorted(B)
        for i in range(len(a)):
            if not(a[i]==b[i]):
                return False
        return True
