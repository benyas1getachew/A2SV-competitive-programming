class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        result = []

        while positive and negative:
            
            result.append(positive.pop(0))
            result.append(negative.pop(0))

        result.extend(negative)
        result.extend(positive)

        return result