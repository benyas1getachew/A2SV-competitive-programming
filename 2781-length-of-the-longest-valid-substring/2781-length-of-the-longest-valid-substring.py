class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        invalid = set(forbidden)
        max_len = 0
        r = len(word) - 1
        for l in range(len(word) - 1, -1, -1):
            for k in range(l, min(r, l + 9) + 1):
                if word[l:k + 1] in invalid:
                    r = k - 1
                    break
            max_len = max(max_len, r - l + 1)
        return max_len