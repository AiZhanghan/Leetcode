# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """hash"""
        s = set()
        while head:
            if head in s:
                return True
            else:
                s.add(head)
            head = head.next
        return False


# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         """双指针"""
#         first, last = head, head
#         while True:
#             if not (first and first.next):
#                 return False
#             first = first.next.next
#             last = last.next
#             if first == last:
#                 return True