# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:17:46 2019

@author: Administrator
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def create_list_node(arr, n):
    
    if n == 0:
        return None
    
    head = ListNode(arr[0])
    
    cur_node = head
    for i in range(1, n):
        cur_node.next = ListNode(arr[i])
        cur_node = cur_node.next
        
    return head

def print_linked_list(head):
    
    cur_node = head
    while cur_node:
        print('%d -> ' % (cur_node.val), end = '')
        cur_node = cur_node.next
    
    print('None')
    