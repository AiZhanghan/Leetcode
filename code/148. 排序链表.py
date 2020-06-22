# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """归并排序, 自底向上"""
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        size = 1
        while size < length:
            cur = dummy_head.next
            tail = dummy_head

            while cur:
                left = cur
                right = self.cut(left, size)
                cur = self.cut(right, size)

                tail.next = self.merge(left, right)
                while tail.next:
                    tail = tail.next
            size *= 2
        return dummy_head.next
    
    def cut(self, head: ListNode, n: int) -> ListNode:
        p = head
        for _ in range(n - 1):
            if p:
                p = p.next
            else:
                break
        if not p:
            return
        next_ = p.next
        p.next = None
        return next_
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        p = dummy_head
        while l1 and l2:
            if l1.val <l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummy_head.next


# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         """归并排序, 自底向上"""
#         h = head
#         length = 0
#         intv = 1
#         while h:
#             h = h.next
#             length += 1
#         res = ListNode(0)
#         res.next = head
#         while intv < length:
#             pre = res
#             h = res.next
#             while h:
#                 h1 = h
#                 i = intv
#                 while i and h:
#                     h = h.next
#                     i -= 1
#                 if i:
#                     break
#                 h2 = h
#                 i = intv
#                 while i and h:
#                     h = h.next
#                     i -= 1
#                 c1 = intv
#                 c2 = intv - i
#                 while c1 and c2:
#                     if h1.val < h2.val:
#                         pre.next = h1
#                         h1 = h1.next
#                         c1 -= 1
#                     else:
#                         pre.next = h2
#                         h2 = h2.next
#                         c2 -= 1
#                     pre = pre.next
#                 pre.next = h1 if c1 else h2
#                 while c1 > 0 or c2 > 0:
#                     pre = pre.next
#                     c1 -= 1
#                     c2 -= 1
#                 pre.next = h
#             intv *= 2
#         return res.next


# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         """归并排序, 递归"""
#         if not head or not head.next:
#             return head
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         mid = slow.next
#         slow.next = None

#         left = self.sortList(head)
#         right = self.sortList(mid)

#         dummy = ListNode(0)
#         cur = dummy
#         while left and right:
#             if left.val < right.val:
#                 cur.next = left
#                 left = left.next
#             else:
#                 cur.next = right
#                 right = right.next
#             cur = cur.next
#         cur.next = left if left else right
#         return dummy.next
