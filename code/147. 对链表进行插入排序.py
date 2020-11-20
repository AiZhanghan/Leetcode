# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        Args:
            head: ListNode
        
        Return:
            ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        prev = head
        node = head.next

        while node:
            if node.val < prev.val:
                temp = dummy
                while temp.next.val < node.val:
                    temp = temp.next
                prev.next = node.next
                node.next = temp.next
                temp.next = node
                node = prev.next
            else:
                prev = prev.next
                node = node.next

        return dummy.next
            


# class Solution:
#     def insertionSortList(self, head):
#         """
#         Args:
#             head: ListNode
        
#         Return:
#             ListNode
#         """
#         temp = []
#         cur = head
#         while cur:
#             temp.append(cur.val)
#             cur = cur.next
#         temp.sort()
        
#         dummy = ListNode(-1)
#         cur = dummy
#         for val in temp:
#             cur.next = ListNode(val)
#             cur = cur.next
#         return dummy.next

