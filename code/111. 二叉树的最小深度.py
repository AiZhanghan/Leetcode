# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        res = float("inf")
        if root.left:
            res = min(res, self.minDepth(root.left))
        if root.right:
            res = min(res, self.minDepth(root.right))
        return res + 1