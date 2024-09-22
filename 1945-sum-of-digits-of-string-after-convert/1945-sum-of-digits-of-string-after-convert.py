class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        num = int(num_str)

        for _ in range(k):
            num = sum(int(digit) for digit in str(num))

        return num