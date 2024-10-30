from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        sl = SortedList()
        
        for i in range(len(nums1)):
            target = nums1[i] - nums2[i]
            count += sl.bisect_right(target + diff)
            sl.add(target)
        
        return count