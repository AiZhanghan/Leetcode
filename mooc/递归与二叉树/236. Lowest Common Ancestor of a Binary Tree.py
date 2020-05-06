# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:18:38 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        q_path = self.find_node(root, q)
        p_path = self.find_node(root, p)
        
        q_path_len = len(q_path)
        p_path_len = len(p_path)
        min_path_len = min(q_path_len, p_path_len)
        
        i = 0
        while q_path[i - 1] == p_path[i - 1]:
            i -= 1
            if i == -min_path_len:
                break
        
        return q_path[i]
    
    def find_node(self, root, node):
        
        res = []
        
        if not root:
            return
        
        if root.val == node.val:
            res.append(node)
            return res
        
        left_path = self.find_node(root.left, node)
        
        if left_path:
            res = left_path
            res.append(root)
        else:
            right_path = self.find_node(root.right, node)
            if right_path:
                res = right_path
                res.append(root)
            
        return res
        