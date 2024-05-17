# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node,c_min,c_max):
            if not node:
                return c_max-c_min
            
            c_min=min(c_min,node.val)
            c_max=max(c_max,node.val)
            
            left=dfs(node.left,c_min,c_max)
            right=dfs(node.right,c_min,c_max)
            
            return max(left,right)
        
        return dfs(root,root.val,root.val)