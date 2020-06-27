# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        Args:
            head: ListNode
            k: int
        
        Return:
            ListNode
        """
        if not head:
            return
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        k = k % length

        first = head
        last = head
        for _ in range(k):
            first = first.next
        while first.next:
            first = first.next
            last = last.next
        
        first.next = head
        head = last.next
        last.next = None

        return head