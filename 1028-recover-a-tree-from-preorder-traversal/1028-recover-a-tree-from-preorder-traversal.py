# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = deque()
        i = 0
        
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(value)
            
            if stack:
                while len(stack) > depth:
                    stack.pop()
                
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            
            stack.append(node)
        
        return stack[0]