class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(c):
            return c in 'aeiou'

        def starts_and_ends_with_vowel(word):
            return is_vowel(word[0]) and is_vowel(word[-1])
        n = len(words)
        vowel_counts = [0] * (n + 1)
        for i in range(n):
            vowel_counts[i + 1] = vowel_counts[i] + (1 if starts_and_ends_with_vowel(words[i]) else 0)
        
        result = []
        for li, ri in queries:
            result.append(vowel_counts[ri + 1] - vowel_counts[li])
        
        return result