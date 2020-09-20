# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head):
        """
        Args:
            head: ListNode
        
        Return:
            list[int]
        """

        if not head:
            return []
        res = self.reversePrint(head.next)
        res.append(head.val)
        return res