# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head):
        """
        time: O(N)
        space: O(N)

        Args:
            head: ListNode
        
        Return: List[int]
        """
        self.res = []
        self._reverse_print(head)
        return self.res

    def _reverse_print(self, head):
        """
        Args:
            head: ListNode
        """
        if not head:
            return
        self._reverse_print(head.next)
        self.res.append(head.val)


# class Solution:
#     def reversePrint(self, head):
#         """
#         time: O(N)
#         space: O(N)

#         Args:
#             head: ListNode
        
#         Return: List[int]
#         """
#         s = []
#         cur = head
#         while cur:
#             s.append(cur.val)
#             cur = cur.next
#         s.reverse()
#         return s