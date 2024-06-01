# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        bottom_left_value = root.val
        
        while queue:
            node = queue.popleft()
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
                
            bottom_left_value = node.val
        
        return bottom_left_value