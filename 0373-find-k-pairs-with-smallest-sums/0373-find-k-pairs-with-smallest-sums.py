class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        min_heap = []
        for i in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[i], 0, i))

        result = []
        while k > 0 and min_heap:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append((nums1[i], nums2[j]))
            k -= 1
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return result