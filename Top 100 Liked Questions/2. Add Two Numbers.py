# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:47:50 2019

@author: 54949
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        root = cur = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
        
        return root.next
        
#    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#        
#        cur1 = l1
#        cur2 = l2
#        
#        dummy = ListNode(-1)
#        cur = dummy
#        
#        flag = 0
#        while cur1 and cur2:
#            new_val = cur1.val + cur2.val + flag
#            if new_val >= 10:
#                flag = 1
#                new_val = new_val % 10
#            else:
#                flag = 0
#            cur.next = ListNode(new_val)
#            
#            cur1 = cur1.next
#            cur2 = cur2.next
#            cur = cur.next
#        
#        res = None
#        if cur1:
#            res = cur1
#        elif cur2:
#            res = cur2
#            
#        while res or flag:
#            new_val = flag + (res.val if res else 0)
#            if new_val >= 10:
#                flag = 1
#                new_val = new_val % 10
#            else:
#                flag = 0
#            cur.next = ListNode(new_val)
#            
#            res = (res.next if res else None)
#            cur = cur.next
#        
#        return dummy.next
#        