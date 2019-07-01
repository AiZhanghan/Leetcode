# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:24:50 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 
        
        left_node_number = self.node_number(root.left)
        if k == left_node_number + 1:
            res = root.val
        elif k <= left_node_number:
            res = self.kthSmallest(root.left, k)
        else:
            res = self.kthSmallest(root.right, k - left_node_number - 1)
        
        return res
    
    def node_number(self, root):
        if not root:
            return 0
        
        return self.node_number(root.left) + self.node_number(root.right) + 1
    