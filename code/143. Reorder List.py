# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:06:37 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
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
        
        q = head
        while head2 and q:
            p = head2
            head2 = head2.next

            p.next = q.next
            q.next = p
            
            if p.next:
                q = p.next
            else:
                p.next = head2
                break
        
        
        
    def reverseList(self, head):
        
        pre = None
        cur = head
        
        while cur:
            _next = cur.next
            
            cur.next = pre
            pre = cur
            cur = _next
        
        return pre