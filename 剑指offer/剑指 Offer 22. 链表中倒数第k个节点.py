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
        first = second = head
        
        try:
            for _ in range(k):
                first = first.next
        except:
            return
        
        while first:
            first = first.next
            second = second.next

        return second
