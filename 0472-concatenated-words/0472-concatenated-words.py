class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def canForm(word, wordSet):
            if not word:
                return False
            dp = [False] * (len(word) + 1)
            dp[0] = True  
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordSet:
                        dp[i] = True
                        break
            return dp[-1]

        words.sort(key=len)
        wordSet = set()
        result = []

        for word in words:
            if canForm(word, wordSet):
                result.append(word)
            wordSet.add(word)

        return result