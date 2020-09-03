# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
class Solution:
    def getMinimumDifference(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        self.res = float("inf")
        self.pre = None
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        """
        Args:
            root: TreeNode
        """
        if not root:
            return
        self.dfs(root.left)
        if self.pre:
            self.res = min(self.res, root.val - self.pre.val)
        self.pre = root
        self.dfs(root.right)