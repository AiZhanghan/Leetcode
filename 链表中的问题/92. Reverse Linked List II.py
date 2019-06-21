# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:05:19 2019

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #left: m - 1
        #right: n + 1
        if m == n:
            return head
        
        cur = head
        left = None
        for i in range(n - 1):
            if i == m - 2:
                left = cur
            cur = cur.next
        right = cur.next
        cur.next = None
        
        if left and right:
            reversed_fragment = self.reverseList(left.next)
            left.next.next = right
            left.next = reversed_fragment
            return head
            
        if not left:
            reversed_fragment = self.reverseList(head)
            if right:
                head.next = right
                return head
            else:
                return reversed_fragment
        
        
        
    def reverseList(self, head):
        
        pre = None
        cur = head
        
        while cur:
            _next = cur.next
            
            cur.next = pre
            pre = cur
            cur = _next
        
        return pre
    
if __name__ == '__main__':
    
    l = ListNode(3)
