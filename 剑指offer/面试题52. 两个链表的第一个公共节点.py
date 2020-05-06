# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        Args:
            headA: ListNode
            headB: ListNode

        Return:
            ListNode
        """
        node1 = headA
        node2 = headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1

# class Solution:
#     def getIntersectionNode(self, headA, headB):
#         """
#         Args:
#             headA: ListNode
#             headB: ListNode

#         Return:
#             ListNode
#         """
#         len_a = self.get_length(headA)
#         len_b = self.get_length(headB)
#         if len_a > len_b:
#             headA, headB = headB, headA
#             len_a, len_b = len_b, len_a
        
#         cur_b = headB
#         for _ in range(len_b - len_a):
#             cur_b = cur_b.next
        
#         cur_a = headA
#         while cur_a:
#             if cur_a is cur_b:
#                 return cur_a
#             else:
#                 cur_a = cur_a.next
#                 cur_b = cur_b.next
#         return

#     def get_length(self, head):
#         """
#         Args:
#             head: ListNode

#         Return:
#             int
#         """
#         res = 0
#         cur = head
#         while cur:
#             res += 1
#             cur = cur.next
#         return res