# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :param root: TreeNode

        :return: bool
        """
        if not root:
            return True
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, root1, root2):
        """
        :param root1: TreeNode
        :param root2: TreeNode

        :return: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return self.is_mirror(root1.left, root2.right) and \
               self.is_mirror(root1.right, root2.left)