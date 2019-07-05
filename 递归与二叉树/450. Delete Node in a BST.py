# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:54:36 2019

@author: Administrator
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, node, key):
        
        if node == None:
            return None
        
        if key < node.val:
            node.left = self.deleteNode(node.left, key)
            return node
        elif key > node.val:
            node.right = self.deleteNode(node.right, key)
        else:
            if node.left == None:
                right_node = node.right
                return right_node
            
            if node.right == None:
                left_node = node.left
                return left_node
            
            successor = self.__minimum(node.right)
            
            successor.right = self.__remove_min(node.right)
            successor.left = node.left
            
            return successor
        
        return node
        
    def __minimum(self, node):
        if node.left == None:
            return node
        
        return self.__minimum(node.left)
    
    def __remove_min(self, node):
        if node.left == None:
            right_node = node.right
            return right_node
        
        node.left = self.__remove_min(node.left)
        return node
            