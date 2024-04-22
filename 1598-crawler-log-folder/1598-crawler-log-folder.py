class Solution(object):
    def minOperations(self, logs):
        stack = []
        for element in logs:
            if element == '../':
                if stack:
                    stack.pop()
            elif element == './':
                continue
            else:
                stack.append(element)        
        return len(stack)