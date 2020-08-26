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
        
        carry = 0
        head = None
        while s1 or s2 or carry:
            val = carry
            val += s1.pop() if s1 else 0
            val += s2.pop() if s2 else 0
            
            node = ListNode(val % 10)
            node.next = head
            head = node
            carry = val // 10
        
        return head