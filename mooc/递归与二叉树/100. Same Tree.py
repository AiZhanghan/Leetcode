# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:47:23 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not q and not p:
            return True
        if (p and not q) or (q and not p):
            return False
        if p and q and p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
if __name__ == '__main__':
    p = TreeNode(1)
    q = None
    res = Solution().isSameTree(p, q)