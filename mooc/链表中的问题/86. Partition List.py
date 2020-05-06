# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:12:48 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #less than x
        left_list = ListNode(None)
        left_cur = left_list
        #greater than or equal to x
        right_list = ListNode(None)
        right_cur = right_list
        
        cur = head
        while cur:
            if cur.val < x:
                left_cur.next = ListNode(cur.val)
                left_cur = left_cur.next
            else:
                right_cur.next = ListNode(cur.val)
                right_cur = right_cur.next
            
            cur = cur.next
            
        left_cur.next = right_list.next
        
        return left_list.next
        