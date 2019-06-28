# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:43:14 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        min_depth_left = self.minDepth(root.left)
        min_depth_right = self.minDepth(root.right)
        
        if min_depth_left and min_depth_right:
            return min(min_depth_left, min_depth_right) + 1
        else:
            return max(min_depth_left, min_depth_right) + 1
        