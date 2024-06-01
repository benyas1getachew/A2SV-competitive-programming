# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])  

        while queue:
            level_length = len(queue)
            _, first_position = queue[0]  
            _, last_position = queue[-1]  
            max_width = max(max_width, last_position - first_position + 1)

            for _ in range(level_length):
                node, position = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * position))
                if node.right:
                    queue.append((node.right, 2 * position + 1))

        return max_width