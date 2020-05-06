# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:56:39 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        
        list_length, end = self.list_length(head)
        k = k % list_length
        
        cur = head
        for i in range(list_length - k - 1):
            cur = cur.next
        
        end.next = head
        head = cur.next
        cur.next = None
        
        return head
        
    def list_length(self, head):
        n = 0
        cur = head
        while cur and cur.next:
            n += 1
            cur = cur.next
            
        return n + 1, cur