class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix_sum = 0
        result = 0
        
        for num in nums:
            prefix_sum += num
            
            modulo = prefix_sum % k
            if modulo in count:
                result += count[modulo]
            count[modulo] = count.get(modulo, 0) + 1
        
        return result