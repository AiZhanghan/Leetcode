from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """BFS"""
        if not root:
            return

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         """DFS"""
#         if not root:
#             return
        
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)

#         root.left, root.right = right, left
        
#         return root