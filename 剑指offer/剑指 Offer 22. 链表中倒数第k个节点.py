# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head, k):
        """
        Args:
            head: ListNode
            k: int
        
        Return:
            ListNode
        """
        slow = head
        fast = head

        for _ in range(k):
            if not fast:
                return
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next

        return slow