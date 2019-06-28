# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:01:51 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        return self.is_mirror(root.left, root.right)
    
    def is_mirror(self, left, right):
        
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val == right.val:
            out_pair = self.is_mirror(left.left, right.right)
            in_pair = self.is_mirror(left.right, right.left)
            return out_pair and in_pair
        else:
            return False
        