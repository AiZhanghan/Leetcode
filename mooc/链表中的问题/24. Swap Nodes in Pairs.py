# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:57:15 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        p = dummy_head
        while p.next and p.next.next:
            node1 = p.next
            node2 = node1.next
            _next = node2.next
            
            node2.next = node1
            node1.next = _next
            p.next = node2
            
            p = node1
        
        return dummy_head.next