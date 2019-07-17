# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:55:11 2019

@author: 54949
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.__memo = {}
        return self.__try_rob(root)
    
    def __try_rob(self, root):
        
        if not root:
            return 0
        
        if root in self.__memo.keys():
            return self.__memo[root]
        
        res = 0
        
        if root.left:
            res += self.__try_rob(root.left.left) + self.__try_rob(root.left.right)
        
        if root.right:
            res += self.__try_rob(root.right.left) + self.__try_rob(root.right.right)
        
        res = max(res + root.val, self.__try_rob(root.left) + self.__try_rob(root.right))
        
        self.__memo[root] = res
        
        return res
    