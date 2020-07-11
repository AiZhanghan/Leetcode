# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B):
        """
        Args:
            A: TreeNode
            B: TreeNode
        
        Return:
            bool
        """
        if not A or not B:
            return False
        
        return self.recur(A, B) \
            or self.isSubStructure(A.left, B) \
            or self.isSubStructure(A.right, B)

    def recur(self, A, B):
        """
        Args:
            A: TreeNode
            B: TreeNode
        
        Return:
            bool
        """
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)