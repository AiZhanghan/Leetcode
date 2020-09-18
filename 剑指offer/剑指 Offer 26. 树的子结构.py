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
        return self.helper(A, B) or self.isSubStructure(A.left, B) \
            or self.isSubStructure(A.right, B)
        
    def helper(self, A, B):
        """
        Args:
            A: TreeNode
            B: TreeNode
        
        Return:
            bool
        """
        # if not A and not B:
        #     return True
        if not B:
            return True
        if not A:
            return False
        
        return A.val == B.val and self.helper(A.left, B.left) \
            and self.helper(A.right, B.right)
