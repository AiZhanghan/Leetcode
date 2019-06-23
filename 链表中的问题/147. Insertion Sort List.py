# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:36:50 2019

@author: Administrator
"""
import test_module
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        
        answer = ListNode(-9999999999999999)
        
        while head:
            p = head
            head = head.next
            p.next = None
            
            cur = answer
            while cur.next and cur.next.val <= p.val:
                    cur = cur.next
            p.next = cur.next
            cur.next = p
        
        return answer.next
            
if __name__ == '__main__':
    arr = [4,2,1,3]
    head = test_module.create_list_node(arr, 4)
    
    head2 = Solution().insertionSortList(head)
    test_module.print_linked_list(head2)
    