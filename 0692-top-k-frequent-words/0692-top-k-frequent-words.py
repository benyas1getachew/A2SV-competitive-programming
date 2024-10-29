class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        result = sorted(freq.keys(), key=lambda x: (-freq[x], x))

        return result[:k]