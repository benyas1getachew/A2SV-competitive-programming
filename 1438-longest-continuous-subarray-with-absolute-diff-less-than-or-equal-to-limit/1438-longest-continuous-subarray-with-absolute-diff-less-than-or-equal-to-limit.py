class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_de=deque()
        min_de=deque()
        
        left=0
        max_len=0
        
        for right,num in enumerate(nums):
            
            while max_de and num>max_de[-1]:
                max_de.pop()     
            max_de.append(num)
            while min_de and num<min_de[-1]:
                min_de.pop()   
            min_de.append(num)
            while max_de[0]-min_de[0]>limit:
                if max_de[0]==nums[left]:
                    max_de.popleft()
                if min_de[0]==nums[left]:
                    min_de.popleft()
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len