class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        score = 0
        
        for i in range(k):
            score += max_num
            max_num += 1
            
        return score