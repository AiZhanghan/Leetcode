# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:30:29 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node or not node.next:
            return
        
        node.val = node.next.val
        node.next = node.next.next
        

        