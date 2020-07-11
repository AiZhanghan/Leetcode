# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        Args:
            head: ListNode
        
        Return:
            ListNode
        """
        cur = None
        pre = head
        while pre:
            tmp = pre.next
            pre.next = cur
            cur = pre
            pre = tmp
        return cur


# class Solution:
#     def reverseList(self, head):
#         """
#         Args:
#             head: ListNode
        
#         Return:
#             ListNode
#         """
#         if not head or not head.next:
#             return head
#         new_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return new_head