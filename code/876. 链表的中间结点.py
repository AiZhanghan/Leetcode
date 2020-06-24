# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        Args:
            head: ListNode
        
        Return；
            ListNode
        """
        first = head
        last = head
        while first and first.next:
            first = first.next.next
            last = last.next
        return last