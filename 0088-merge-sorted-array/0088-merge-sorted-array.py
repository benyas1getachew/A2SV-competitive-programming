class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        a=0
        b=0
        if n>0:
            for i in range(len(nums1)):
                if nums1[i]<nums2[a] and b<m:
                    b+=1
                    continue
                else:
                    nums1.insert(i,nums2[a])
                    nums1.pop()
                    a+=1
                    if a==n:
                        break
                