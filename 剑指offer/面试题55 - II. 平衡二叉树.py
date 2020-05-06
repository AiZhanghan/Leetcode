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
        
        left_depth = self.dfs(root.left)
        if left_depth == -1:
            return -1
        
        right_depth = self.dfs(root.right)
        if right_depth == -1:
            return -1
        
        return max(left_depth, right_depth) + 1 \
               if abs(left_depth - right_depth) <= 1 else -1
    
        