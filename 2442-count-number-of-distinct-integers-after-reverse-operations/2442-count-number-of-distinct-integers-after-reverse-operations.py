class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse_number(num: int) -> int:
            return int(str(num)[::-1])
        
        distinct_integers = set(nums)
        
        for num in nums:
            reversed_num = reverse_number(num)
            distinct_integers.add(reversed_num)
        
        return len(distinct_integers)