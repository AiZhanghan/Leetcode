# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:02:06 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        if not root:
            return 0
        
        res = self.find_path(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        
        return res
        
    def find_path(self, node, num):
        
        if not node:
            return 0
        
        res = 0
        if node.val == num:
            res += 1
            
        res += self.find_path(node.left, num - node.val)
        res += self.find_path(node.right, num - node.val)
        
        return res
    