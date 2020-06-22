# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:18:05 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        #The list was divided into two segments, 
        #with prev pointing to the last node in the first,
        #cur to the head of the second
        prev,cur,front = None,head,head
        while front and front.next:
            prev = cur
            cur = cur.next
            front = front.next.next
        prev.next = None
        
        head1 = self.sortList(head)
        head2 = self.sortList(cur)
        
        return self.mergeTwoLists(head1, head2)
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy_head = ListNode(None)
        cur = dummy_head
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            rest = l1
        else:
            rest = l2
        
        cur.next = rest
        
        return dummy_head.next