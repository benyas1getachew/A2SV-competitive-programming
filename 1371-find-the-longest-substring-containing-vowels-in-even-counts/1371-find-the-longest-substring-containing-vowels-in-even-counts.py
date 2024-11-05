class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_map = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        state = 0
        longest = 0
        state_index = {0: -1}

        for i, char in enumerate(s):
            if char in vowel_map:
                state ^= vowel_map[char]
            if state in state_index:
                longest = max(longest, i - state_index[state])
            else:
                state_index[state] = i

        return longest