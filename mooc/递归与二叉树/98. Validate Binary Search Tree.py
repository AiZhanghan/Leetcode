# -*- 0oding: utf-8 -*-
"""
Created on Sun Jun 30 11:31:44 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, floor = -float('inf'), ceiling = float('inf')):
        
        if not root:
            return True
        
        if root.val <= floor or root.val >= ceiling:
            return False
        
        return(self.isValidBST(root.left, floor, root.val) and
               self.isValidBST(root.right, root.val, ceiling))
        