# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:05:22 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stack = self.list_to_stack(l1)
        l2_stack = self.list_to_stack(l2)
        
        answer_stack = []
        flag = 0
        
        while l1_stack and l2_stack:
            new_val = l1_stack.pop() + l2_stack.pop() + flag
            if new_val >= 10:
                flag = 1
                new_val -= 10
            else:
                flag = 0
            
            answer_stack.append(new_val)
        
        if l1_stack:
            rest = l1_stack
        else:
            rest = l2_stack
            
        while rest:
            new_val = rest.pop() + flag
            if new_val >= 10:
                flag = 1
                new_val -= 10
            else:
                flag = 0
            
            answer_stack.append(new_val)
            
        if flag:
            answer_stack.append(1)
        
        return self.stack_to_list(answer_stack)
        
    def list_to_stack(self, head):
        stack = []
        
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        return stack
    
    def stack_to_list(self, stack):
        head = ListNode(stack.pop())
        
        cur = head  
        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next
        
        return head
            