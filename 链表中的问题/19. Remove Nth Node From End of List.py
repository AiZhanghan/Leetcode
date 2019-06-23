# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:40:30 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        assert n >= 0
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        p = dummy_head
        q = dummy_head
        for i in range(n + 1):
            assert q
            q = q.next
        
        while q:
            p = p.next
            q = q.next
            
        p.next = p.next.next
        
        return dummy_head.next