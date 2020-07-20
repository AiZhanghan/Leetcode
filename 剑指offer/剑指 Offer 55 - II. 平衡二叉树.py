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
        
        l_depth = self.dfs(root.left)
        if l_depth == -1:
            return -1
        
        r_depth = self.dfs(root.right)
        if r_depth == -1:
            return -1

        is_balanced = abs(l_depth - r_depth) <= 1
        
        return max(l_depth, r_depth) + 1 if is_balanced else -1