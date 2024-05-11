class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)
        left_index = -1
        right_index = -1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right_index = left_index = mid
                while left_index > 0 and nums[left_index - 1] == target:
                    left_index -= 1
                while right_index < len(nums) - 1 and nums[right_index + 1] == target:
                    right_index += 1
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        return [left_index, right_index]