class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1} 
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            count += prefix_sum.get(curr_sum - k, 0)  
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        
        return count