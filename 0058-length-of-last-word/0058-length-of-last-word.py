class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=list(s.split())
        return len(a[-1])