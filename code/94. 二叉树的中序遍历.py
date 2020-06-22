from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """迭代"""
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
        

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         """迭代"""
#         WHITE, GRAY = 0, 1
#         res = []
#         stack = [(WHITE, root)]
#         while stack:
#             color, node = stack.pop()
#             if not node:
#                 continue
#             if color == WHITE:
#                 stack.append((WHITE, node.right))
#                 stack.append((GRAY, node))
#                 stack.append((WHITE, node.left))
#             else:
#                 res.append(node.val)
#         return res        


# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         """递归"""
#         self.res = []
#         self.dfs(root)
#         return self.res

#     def dfs(self, root):
#         if not root:
#             return
#         self.dfs(root.left)
#         self.res.append(root.val)
#         self.dfs(root.right)