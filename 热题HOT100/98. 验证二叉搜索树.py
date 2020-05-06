from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, -float("inf"), float("inf"))
    
    def dfs(self, root: TreeNode, low: int, high: int) -> bool:
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self.dfs(root.left, low, root.val) \
            and self.dfs(root.right, root.val, high)


# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         """中序遍历"""
#         if not root:
#             return True
#         inorder = []
#         self.dfs(root, inorder)
#         return self.is_sorted(inorder)

#     def dfs(self, root: TreeNode, inorder: List[int]):
#         if not root:
#             return
#         self.dfs(root.left, inorder)
#         inorder.append(root.val)
#         self.dfs(root.right, inorder)
    
#     def is_sorted(self, inorder: List[int]) -> bool:
#         for i, x in enumerate(inorder[1: ], 1):
#             if x <= inorder[i - 1]:
#                 return False
#         return True