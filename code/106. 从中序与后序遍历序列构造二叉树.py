# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        Args:
            inorder: list[int]
            postorder: list[int]
        
        Return:
            TreeNode
        """
        self.postorder = postorder
        self.dic = {val: i for i, val in enumerate(inorder)}
        return self._build_tree()

    def _build_tree(self, )