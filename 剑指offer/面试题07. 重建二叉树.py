# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        parameter:
            preorder: list[int]
            inorder: list[int]
        return: TreeNode
        """
        n = len(preorder)
        if n != len(inorder):
            return

        return self._buildTree(preorder, inorder, 0, n-1, 0, n-1)
    
    def _buildTree(self, preorder, inorder, pre_left, pre_right, in_left, in_right):
        """
        parameter:
            preorder: list[int]
            inorder: list[int]
            pre_left: int
            pre_right: int
            in_left: int
            in_right: int
        return: TreeNode
        """
        if pre_left > pre_right or in_left > in_right:
            return
        
        root = TreeNode(preorder[pre_left])
        # 根节点在inorder中的下标
        root_pos_in = inorder.index(preorder[pre_left])
        # 左子树节点数
        left_length = root_pos_in - in_left

        root.left = self._buildTree(preorder, inorder, 
            pre_left+1, pre_left+left_length,
            in_left, root_pos_in-1)
            
        root.right = self._buildTree(preorder, inorder, 
            pre_left+left_length+1, pre_right,
            root_pos_in+1, in_right)
            
        return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    res = Solution().buildTree(preorder, inorder)

    print()