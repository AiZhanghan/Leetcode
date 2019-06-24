# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:36:14 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Command:
    def __init__(self, s, node):
        self.s = s
        self.node = node

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        if not root:
            return res
        
        stack = []
        stack.append(Command('go', root))
        while stack:
            command = stack.pop()
            
            if command.s == 'print':
                res.append(command.node.val)
            else:
                assert command.s == 'go'
                if command.node.right:
                    stack.append(Command('go', command.node.right))
                stack.append(Command('print', command.node))
                if command.node.left:
                    stack.append(Command('go', command.node.left))
        
        return res        
    
#        res = []
#        if root:
#            res = self.inorderTraversal(root.left)
#            res.append(root.val)
#            res += self.inorderTraversal(root.right)
#        
#        return res