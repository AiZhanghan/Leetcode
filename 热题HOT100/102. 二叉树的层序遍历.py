from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.levels = []
        self.dfs(root, 0)
        return self.levels

    def dfs(self, root: TreeNode, level: int):
        if level >= len(self.levels):
            self.levels.append([])
        self.levels[level].append(root.val)
        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)


# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         queue = deque()
#         queue.append(root)
#         while queue:
#             size = len(queue)
#             temp = []
#             for _ in range(size):
#                 node = queue.popleft()
#                 temp.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(temp)
#         return res