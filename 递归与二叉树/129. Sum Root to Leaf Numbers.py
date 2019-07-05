# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:36:04 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        path = self.path(root)
        for i in range(len(path)):
            temp = 0
            for j in range(len(path[i])):
                temp = temp * 10 + path[i][j]
            res += temp
        
        return res
        
    def path(self, root):
        
        res = []
        
        if not root:
            return res
        
        if not root.left and not root.right:
            res.append([root.val])
            return res
        
        left_path = self.path(root.left)
        for i in range(len(left_path)):
            temp = [root.val]
            for j in range(len(left_path[i])):
                temp.append(left_path[i][j])
            res.append(temp)
            
        right_path = self.path(root.right)
        for i in range(len(right_path)):
            temp = [root.val]
            for j in range(len(right_path[i])):
                temp.append(right_path[i][j])
            res.append(temp)
        
        return res
            