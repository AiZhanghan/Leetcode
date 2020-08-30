# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0

        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0
        
        self.res = max(self.res, left + right)
        return max(left, right)


# class Solution:
#     def longestUnivaluePath(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             int
#         """
#         if not root:
#             return 0
#         return max(self.helper(root.left, root.val) + self.helper(root.right, root.val),
#             self.longestUnivaluePath(root.left),
#             self.longestUnivaluePath(root.right))

#     def helper(self, root, val):
#         """
#         Args:
#             root： TreeNode
#             val: int
        
#         Return:
#             int
#         """
#         if not root or root.val != val:
#             return 0
#         return max(self.helper(root.left, val), self.helper(root.right, val))
