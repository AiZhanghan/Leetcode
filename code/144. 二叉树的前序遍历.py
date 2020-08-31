# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            list[int]
        """
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
        

# class Solution:
#     def preorderTraversal(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             list[int]
#         """
#         stack = []
#         res = []
#         while stack or root:
#             if not root:
#                 root = stack.pop()
#             res.append(root.val)
#             if root.right:
#                 stack.append(root.right)
#             root = root.left
#         return res