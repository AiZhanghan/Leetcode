# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        time: O(N)
        space: O(N)

        Args:
            preorder: list[int]
            inorder: list[int]
        
        Return: TreeNode
        """
        self.dic = {}
        self.preorder = preorder

        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        
        return self._build_tree(0, 0, len(inorder) - 1)

    def _build_tree(self, pre_left, in_left, in_right):
        """
        Args:
            pre_left: int
            in_left: int
            in_right: int
        
        Return:
            TreeNode
        """
        if in_left > in_right:
            return

        root = TreeNode(self.preorder[pre_left])

        root_index = self.dic[root.val]
        
        left_len = root_index - in_left

        root.left = self._build_tree(pre_left + 1, in_left, root_index - 1)
        root.right = self._build_tree(pre_left + 1 + left_len, 
            root_index + 1, in_right)
        
        return root


# class Solution:
#     def buildTree(self, preorder, inorder):
#         """
#         time: O(N)
#         space: O(N)

#         Args:
#             preorder: list[int]
#             inorder: list[int]
        
#         Return: TreeNode
#         """
#         self.preorder = preorder
#         self.inorder = inorder
#         return self._build_tree(0, len(preorder), 0, len(inorder))
    
#     def _build_tree(self, pre_left, pre_right, in_left, in_right):
#         """
#         Args:
#             pre_left: int
#             pre_right: int
#             in_left: int
#             in_right: int
        
#         Return: TreeNode
#         """
#         if pre_left >= pre_right or in_left >= in_right:
#             return
        
#         root = TreeNode(self.preorder[pre_left])
#         # 根节点在inorder中的下标
#         root_index = self.inorder.index(root.val)
#         # 左子树节点数
#         left_len = root_index - in_left

#         root.left = self._build_tree(pre_left + 1, pre_left + 1 + left_len,
#             in_left, root_index)
            
#         root.right = self._build_tree(pre_left + 1 + left_len, pre_right,
#             root_index + 1, in_right)
            
#         return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    res = Solution().buildTree(preorder, inorder)

    print()