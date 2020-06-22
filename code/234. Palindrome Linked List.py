# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:44:10 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        #The list was divided into two segments, 
        #with prev pointing to the last node in the first,
        #cur to the head of the second
        prev,cur,front = None,head,head
        while front and front.next:
            prev = cur
            cur = cur.next
            front = front.next.next
        prev.next = None
        
        head2 = self.reverseList(cur)
        
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        
        return True
        
    def reverseList(self, head):
        
        pre = None
        cur = head
        
        while cur:
            _next = cur.next
            
            cur.next = pre
            pre = cur
            cur = _next
        
        return pre