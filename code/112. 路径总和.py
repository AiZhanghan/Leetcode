# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        Args:
            root: TreeNode
            sum: int
        
        Return:
            bool
        """
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == sum
        
        return self.hasPathSum(root.left, sum - root.val) or \
            self.hasPathSum(root.right, sum - root.val)


# class Solution:
#     def hasPathSum(self, root, sum):
#         """
#         Args:
#             root: TreeNode
#             sum: int
        
#         Return:
#             bool
#         """
#         if not root:
#             return False
#         self.res = False
#         self.dfs(root, sum)
#         return self.res
    
#     def dfs(self, root, sum):
#         """
#         Args:
#             root: TreeNode
#             sum = int
#         """
#         if self.res:
#             return
#         if not root.left and not root.right:
#             self.res = (sum == root.val)
#             return
#         if root.left:
#             self.dfs(root.left, sum - root.val)
#         if root.right:
#                 self.dfs(root.right, sum - root.val)
