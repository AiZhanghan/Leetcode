# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:23:44 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        q = deque()
        q.append([root, 0])
        
        while q:
            node = q[0][0]
            level = q[0][1]
            q.popleft()
            
            if level == len(res):
                res.append([])
            
            res[level].append(node.val)
            
            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
        
        return res
        