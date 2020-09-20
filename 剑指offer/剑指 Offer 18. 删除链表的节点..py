# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head, val):
        """
        Args:
            head: ListNode
            val: int
        
        Return:
            ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.val != val:
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next