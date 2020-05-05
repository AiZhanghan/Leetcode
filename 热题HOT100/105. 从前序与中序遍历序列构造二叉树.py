from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """递归 + Hash"""
        self.preorder = preorder
        self.inorder = inorder
        self.dic = {}
        for i, val in enumerate(inorder):
            self.dic[val] = i
        return self.build_tree(0, len(preorder), 0, len(inorder))
    
    def build_tree(self, p_start: int, p_end: int, i_start: int, i_end: int) \
        -> TreeNode:
        if p_start == p_end:
            return
        root = TreeNode(self.preorder[p_start])
        root_index = self.dic[root.val]
        left_length = root_index - i_start
        root.left = self.build_tree(p_start + 1, p_start + 1 + left_length, \
                                    i_start, root_index)
        root.right = self.build_tree(p_start + 1 + left_length, p_end, \
                                     root_index + 1, i_end)
        return root                                     


# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         """递归"""
#         self.preorder = preorder
#         self.inorder = inorder
#         return self.build_tree(0, len(preorder), 0, len(inorder))
    
#     def build_tree(self, p_start: int, p_end: int, i_start: int, i_end: int) \
#         -> TreeNode:
#         if p_start == p_end:
#             return
#         root = TreeNode(self.preorder[p_start])
#         root_index = self.find(i_start, i_end, root.val)
#         left_length = root_index - i_start
#         root.left = self.build_tree(p_start + 1, p_start + 1 + left_length, \
#                                     i_start, root_index)
#         root.right = self.build_tree(p_start + 1 + left_length, p_end, \
#                                      root_index + 1, i_end)
#         return root                                     

#     def find(self, i_start: int, i_end: int, val: int) -> int:
#         for i in range(i_start, i_end):
#             if val == self.inorder[i]:
#                 return i
