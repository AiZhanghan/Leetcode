# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:22:37 2019

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
import test_module
from queue import PriorityQueue

class Node:
    def __init__(self, priority, node):
        self.priority = priority
        self.node = node
    
    def __lt__(self, other):
        return self.priority < other.priority

class Solution:
    def mergeKLists(self, lists):
        pq = PriorityQueue()
        for _list in lists:
            if _list:
                pq.put(Node(_list.val, _list))
            
        dummy_head = ListNode(0)
        cur = dummy_head
        while pq.qsize() != 0:
            min_node = pq.get()
            cur.next = min_node.node
            cur = cur.next
            if min_node.node.next:
                pq.put(Node(min_node.node.next.val, min_node.node.next))
        
        return dummy_head.next
            
if __name__ == '__main__':
    arrs = [[1,4,5],[1,3,4],[2,6]]
    heads = []
    for arr in arrs:
        heads.append(test_module.create_list_node(arr, len(arr)))
    
    for head in heads:
        test_module.print_linked_list(head)
    
    res = Solution().mergeKLists(heads)
    test_module.print_linked_list(res)