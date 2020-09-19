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
        return self.max_depth(root) != -1

    def max_depth(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        if not root:
            return 0
        
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1 