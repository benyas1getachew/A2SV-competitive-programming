class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
            char_set = set(sub)
            for c in char_set:
                if c.lower() not in char_set or c.upper() not in char_set:
                    return False
            return True

        if len(s) < 2:
            return ""

        for i in range(len(s)):
            if s[i].lower() not in s or s[i].upper() not in s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s