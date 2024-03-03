class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        for v in nums1:
            if v in nums2:
                nums3.append(v)
                nums2.remove(v)
        return nums3