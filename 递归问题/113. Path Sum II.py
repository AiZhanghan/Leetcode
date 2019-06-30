# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:18:47 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        res = []
        
        if not root:
            return res
        
        if not root.left and not root.right and root.val == sum:
            res.append([root.val])
            return res
        
        left_path_sum = self.pathSum(root.left, sum - root.val)
        for i in range(len(left_path_sum)):
            temp = [root.val]
            for j in range(len(left_path_sum[i])):
                temp.append(left_path_sum[i][j])
            res.append(temp)
            
        right_path_sum = self.pathSum(root.right, sum - root.val)
        for i in range(len(right_path_sum)):
            temp = [root.val]
            for j in range(len(right_path_sum[i])):
                temp.append(right_path_sum[i][j])
            res.append(temp)
        
        return res
        