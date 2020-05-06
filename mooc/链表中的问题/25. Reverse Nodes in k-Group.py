# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:10:16 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        p = dummy_head
        
        while p.next:
            left = p.next
            right = left
            for _ in range(k - 1):
                if not right.next:
                    return dummy_head.next
                right = right.next
            
            end = right.next
            right.next = None
            
            self.reverseList(left)
            
            p.next = right
            left.next = end
            p = left
        
        return dummy_head.next
        
    def reverseList(self, head):
        
        pre = None
        cur = head
        
        while cur:
            _next = cur.next
            
            cur.next = pre
            pre = cur
            cur = _next
        
        return pre