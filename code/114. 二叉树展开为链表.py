from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        s = []
        s.append(root)
        pre = None
        while s:
            temp = s.pop()
            if pre:
                pre.right = temp
                pre.left = None
            if temp.right:
                s.append(temp.right)
            if temp.left:
                s.append(temp.left)
            pre = temp


# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         to_visit = []
#         cur = root
#         pre = None

#         while cur or to_visit:
#             while cur:
#                 to_visit.append(cur)
#                 cur = cur.right
#             cur = to_visit[-1]
#             if not cur.left or cur.left == pre:
#                 to_visit.pop()
#                 cur.right = pre
#                 cur.left = None
#                 pre = cur
#                 cur = None
#             else:
#                 cur = cur.left


# class Solution:
#     def __init__(self):
#         self.pre = None

#     def flatten(self, root: TreeNode) -> None:
#         """后序遍历的变形, 右左根
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             return
#         self.flatten(root.right)
#         self.flatten(root.left)
#         root.right = self.pre
#         root.left = None
#         self.pre = root


# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         while root:
#             if not root.left:
#                 root = root.right
#                 continue
#             else:
#                 pre = root.left
#                 while pre.right:
#                     pre = pre.right
#                 pre.right = root.right
#                 root.right = root.left
#                 root.left = None
#                 root = root.right

                
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         root, _ = self.dfs(root)
#         return root

#     def dfs(self, root: TreeNode) -> Tuple[TreeNode, TreeNode]:
#         if not root:
#             return None, None

#         left_start, left_end = self.dfs(root.left)
#         right_start, right_end = self.dfs(root.right)
#         root.left = None
#         if left_start and right_start:
#             root.right = left_start
#             left_end.right = right_start
#             return root, right_end
#         elif left_start:
#             root.right = left_start
#             return root, left_end
#         elif right_start:
#             root.right = right_start
#             return root, right_end
#         else:
#             return root, root
    