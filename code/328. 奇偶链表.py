# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        """
        Args:
            head: ListNode
        
        Return:
            ListNode
        """
        odd_dummy = ListNode()
        even_dummy = ListNode()
        cur = head
        odd_cur = odd_dummy
        even_cur = even_dummy
        while cur:
            odd_cur.next = cur
            even_cur.next = cur.next
            
            cur = cur.next.next if cur.next else None
            odd_cur = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even_dummy.next
        return odd_dummy.next