# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:53:53 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        res = []
        
        if not root:
            return res
        
        if not root.left and not root.right:
            res.append(str(root.val))
            return res
        
        left_s = self.binaryTreePaths(root.left)
        for i in range(len(left_s)):
            res.append(str(root.val) + '->' + left_s[i])
            
        right_s = self.binaryTreePaths(root.right)
        for i in range(len(right_s)):
            res.append(str(root.val) + '->' + right_s[i])
        
        return res
        