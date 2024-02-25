class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for a in range(len(haystack)):
            if haystack[a]==needle[0]:
                if haystack[a:a+len(needle)]==needle:
                    return a
        return -1