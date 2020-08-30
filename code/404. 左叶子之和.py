# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        return self.dfs(root, False)
    
    def dfs(self, root, is_left):
        """
        Args:
            root: TreeNode
            is_left: bool
        
        Return:
            int
        """
        if not root:
            return 0
        leave = 0
        if is_left and not root.left and not root.right:
            leave = root.val
        left = self.dfs(root.left, True)
        right = self.dfs(root.right, False)
        return leave + left + right


# class Solution:
#     def sumOfLeftLeaves(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             int
#         """
#         self.res = 0
#         self.dfs(root)
#         return self.res
    
#     def dfs(self, root):
#         """
#         Args:
#             root: TreeNode
#         """
#         if not root:
#             return
#         if root.left and not root.left.left and not root.left.right:
#             self.res += root.left.val
#         else:
#             self.dfs(root.left)
#         self.dfs(root.right)
        