class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        skills.sort()
        target_sum = skills[0] + skills[-1]
        left, right = 0, len(skills) - 1
        total_chemistry = 0
        while left < right:
            if skills[left] + skills[right] != target_sum:
                return -1
            total_chemistry += skills[left] * skills[right]
            left += 1
            right -= 1
        return total_chemistry
