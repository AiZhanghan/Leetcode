# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        Args:
            head: ListNode
        
        Return:
            ListNode
        """
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            head = head.next
        return head


# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         Args:
#             head: ListNode
        
#         Return:
#             ListNode
#         """
#         cur = head
#         while cur and cur.next:
#             if cur.val == cur.next.val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next
#         return head


# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         Args:
#             head: ListNode
        
#         Return:
#             ListNode
#         """
#         cur = head
#         while cur:
#             val = cur.val
#             _next = cur.next
#             while _next and _next.val == val:
#                 _next = _next.next
#             cur.next = _next
#             cur = cur.next
#         return head