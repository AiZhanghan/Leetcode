# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            bool
        """
        if not root:
            return True
        
        return self.is_symmetric(root.left, root.right)
    
    def is_symmetric(self, root1, root2):
        """
        Args:
            root1: TreeNode
            root2: TreeNode
        
        Return:
            bool
        """
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        return root1.val == root2.val \
            and self.is_symmetric(root1.left, root2.right) \
            and self.is_symmetric(root1.right, root2.left)
        