class Solution:
    def splitString(self, s: str) -> bool:
        def canSplitFromIndex(index, prev_num):
            if index == len(s):
                return True
            
            current_num = 0
            for i in range(index, len(s)):
                current_num = current_num * 10 + int(s[i])
                
                if current_num + 1 == prev_num:
                    if canSplitFromIndex(i + 1, current_num):
                        return True
            
            return False

        for i in range(len(s) - 1):
            first_num = int(s[:i + 1])
            if canSplitFromIndex(i + 1, first_num):
                return True
        
        return False
