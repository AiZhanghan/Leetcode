# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:22:10 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        odd_list = head
        if odd_list and odd_list.next:
            even_list = odd_list.next
        else:
            return head
        
        odd_cur = odd_list
        even_cur = even_list
        
        while even_cur.next and odd_cur.next:
            odd_cur.next = even_cur.next
            odd_cur = odd_cur.next
            
            if odd_cur.next:
                even_cur.next = odd_cur.next
                even_cur = even_cur.next
                
        if not odd_cur.next:
            even_cur.next = None
            
        odd_cur.next = even_list
            
#        if not odd_cur.next:
#            even_cur.next = None
#            odd_cur.next = even_list
#        else:
#            odd_cur.next = even_list
            
        return head
            