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
        return self._build_tree(0, len(inorder) - 1, 0, len(postorder) - 1)

    def _build_tree(self, in_left, in_right, post_left, post_right):
        if in_left > in_right:
            return
        
        root = TreeNode(self.postorder[post_right])
        root_index = self.dic[root.val]
        
        left_len = root_index - in_left

        root.left  = self._build_tree(in_left, root_index - 1, 
            post_left, post_left + left_len - 1)
        root.right = self._build_tree(root_index + 1, in_right,
            post_left + left_len, post_right - 1)
        
        return root
