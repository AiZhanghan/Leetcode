# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:23:44 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy_head = ListNode(None)
        dummy_head.next = head
        
        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy_head.next
#        while head and head.val == val:
#            head = head.next
#        
#        if not head:
#            return
#        
#        cur = head
#        while cur.next:
#            if cur.next.val == val:
#                cur.next = cur.next.next
#            else:
#                cur = cur.next
#        
#        return head