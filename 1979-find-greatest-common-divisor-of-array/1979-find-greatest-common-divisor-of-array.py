class Solution:
    def findGCD(self, nums: List[int]) -> int:

        smallest = min(nums)
        largest = max(nums)

        gcd = math.gcd(smallest, largest)

        return gcd





