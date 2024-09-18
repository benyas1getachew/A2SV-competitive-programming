class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n  
        
        length = 0
        i = 1  
        
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  
                else:
                    lps[i] = 0
                    i += 1

        longest_happy_prefix_length = lps[-1]

        if longest_happy_prefix_length == 0:
            return ""  
        else:
            return s[:longest_happy_prefix_length]