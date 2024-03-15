class Solution:
    def checkPalindromeFormation(self, str1: str, str2: str) -> bool:
        def check1(str1: str, str2: str) -> bool:
            i, j = 0, len(str2) - 1
            while i < j and str1[i] == str2[j]:
                i, j = i + 1, j - 1
            return i >= j or check2(str1, i, j) or check2(str2, i, j)

        def check2(str1: str, i: int, j: int) -> bool:
            return str1[i : j + 1] == str1[i : j + 1][::-1]

        return check1(str1, str2) or check1(str2, str1)
