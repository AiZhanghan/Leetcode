# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            bool
        """
        return self.dfs(root) != -1
    
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
        if left == -1:
            return -1
        right = self.dfs(root.right)
        if right == -1:
            return -1
        
        return max(left, right) + 1 if abs(left - right) < 2 else -1
        

# class Solution:
#     def isBalanced(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             bool
#         """
#         return self.dfs(root)[0]
    
#     def dfs(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             bool
#             int
#         """
#         if not root:
#             return True, 0
        
#         left_balanced, left_depth = self.dfs(root.left)
#         right_balanced, right_depth = self.dfs(root.right)

#         root_balanced = left_balanced and right_balanced and \
#             abs(left_depth - right_depth) <= 1
#         root_depth = max(left_depth, right_depth) + 1
        
#         return root_balanced, root_depth
