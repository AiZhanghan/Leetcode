# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:39:35 2019

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        pre = None
        cur = head
        
        while cur:
            _next = cur.next
            
            cur.next = pre
            pre = cur
            cur = _next
        
        return pre