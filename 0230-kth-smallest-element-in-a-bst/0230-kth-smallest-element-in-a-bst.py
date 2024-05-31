# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def inOrderTraversal(node):
            if node is None or self.result is not None:
                return

            inOrderTraversal(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            inOrderTraversal(node.right)
        inOrderTraversal(root)
        return self.result