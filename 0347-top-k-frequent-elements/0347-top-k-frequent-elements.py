class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        return heapq.nlargest(k, frequency.keys(), key=frequency.get)