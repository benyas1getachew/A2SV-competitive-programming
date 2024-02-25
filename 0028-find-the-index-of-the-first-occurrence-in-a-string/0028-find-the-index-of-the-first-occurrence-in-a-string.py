class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        k=len(needle)
        for a in range(n):
            if haystack[a]==needle[0] and haystack[a:a+k]==needle:
                return a
        return -1