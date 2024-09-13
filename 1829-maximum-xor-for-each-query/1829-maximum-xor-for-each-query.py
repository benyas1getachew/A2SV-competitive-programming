class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        max_val = (1 << maximumBit) - 1  
        xor_all = 0

        for num in nums:
            xor_all ^= num

        answer = []

        for i in range(n):
            answer.append(xor_all ^ max_val)

            xor_all ^= nums[n - 1 - i]

        return answer