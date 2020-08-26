# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Args:
            l1: ListNode
            l2: ListNode
        
        Return:
            ListNode
        """
        s1 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        s2 = []
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        dummy = ListNode(-1)
        while s1 and s2:
            dummy.