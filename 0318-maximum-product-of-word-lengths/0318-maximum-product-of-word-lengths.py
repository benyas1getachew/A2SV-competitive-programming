class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        if n < 2:
            return 0

        bitmasks = []
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            bitmasks.append((bitmask, len(word)))

        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i][0] & bitmasks[j][0] == 0:
                    max_product = max(max_product, bitmasks[i][1] * bitmasks[j][1])

        return max_product