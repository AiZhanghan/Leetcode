# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        Args:
            preorder: list[int]
            inorder: list[int]
        
        Return:
            TreeNode
        """
        self.inorder_index = {key: value for value, key in enumerate(inorder)}
        return self.build_tree(preorder, 0, len(preorder) - 1, 
            0)
    
    def build_tree(self, preorder, pre_start, pre_end,
        in_start):
        """
        Args:
            preorder: list[int]
            pre_start: int
            pre_end: int
            inorder: list[int]
            in_start: int
            in_end: int
        
        Return:
            TreeNode
        """
        if pre_start > pre_end:
            return
        
        root = TreeNode(preorder[pre_start])
        # print(root.val)
        # inorder
        # root_index = inorder.index(root.val)
        root_index = self.inorder_index[root.val]
        left_length = root_index - in_start
        
        root.left = self.build_tree(preorder, pre_start + 1, pre_start + left_length,
            in_start)
        
        root.right = self.build_tree(preorder, pre_start + left_length + 1, pre_end,
            root_index + 1)

        return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    Solution().buildTree(preorder, inorder)