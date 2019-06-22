# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:51:01 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        answer = ListNode(None)
        answer_cur = answer
        
        l1_cur = l1
        l2_cur = l2
        
        flag = 0
        
        while l1_cur and l2_cur:
            new_val = l1_cur.val + l2_cur.val + flag
            if new_val >= 10:
                flag = 1
                new_val -= 10
            else:
                flag = 0
            
            answer_cur.next = ListNode(new_val)
            answer_cur = answer_cur.next
            l1_cur = l1_cur.next
            l2_cur = l2_cur.next
        
        if l1_cur:
            rest = l1_cur
        else:
            rest = l2_cur
        
        while rest:
            new_val = rest.val + flag
            if new_val >= 10:
                flag = 1
                new_val -= 10
            else:
                flag = 0
            
            answer_cur.next = ListNode(new_val)
            answer_cur = answer_cur.next
            rest = rest.next
        
#        while l1_cur:
#            new_val = l1_cur.val + flag
#            if new_val >= 10:
#                flag = 1
#                new_val -= 10
#            else:
#                flag = 0
#            
#            answer_cur.next = ListNode(new_val)
#            answer_cur = answer_cur.next
#            l1_cur = l1_cur.next
#        
#        while l2_cur:
#            new_val = l2_cur.val + flag
#            if new_val >= 10:
#                flag = 1
#                new_val -= 10
#            else:
#                flag = 0
#            
#            answer_cur.next = ListNode(new_val)
#            answer_cur = answer_cur.next
#            l2_cur = l2_cur.next
        
        if flag:
            answer_cur.next = ListNode(flag)
            answer_cur = answer_cur.next
            
        return answer.next
            