# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:33:02 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        dummy_head = ListNode(float('inf'))
        dummy_head.next = head
        cur = dummy_head
        
        while cur.next:
            
            #End points to the next non-repeating node
            end = cur.next.next
            
            if not end:
                return dummy_head.next
            
            if end and cur.next.val != end.val:
                cur = cur.next
            else:
                while end and cur.next.val == end.val:
                    end = end.next
                cur.next = end
        
        return dummy_head.next
            