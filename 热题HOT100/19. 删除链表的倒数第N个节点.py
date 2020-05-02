# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        for _ in range(n):
            first = first.next
        
        last = dummy
        while first.next:
            first = first.next
            last = last.next
        last.next = last.next.next
        return dummy.next