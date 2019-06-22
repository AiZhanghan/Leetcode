    # -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:59:06 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        begin = head
        while begin:
            end = begin
            while end and end.val == begin.val:
                end = end.next
            
            begin.next = end
            begin = begin.next
            
        return head
        
