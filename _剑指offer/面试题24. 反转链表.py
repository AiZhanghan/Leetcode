from List import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :param head: ListNode

        :return: ListNode
        """
        if not head or not head.next:
            return head

        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret


# class Solution:
#     def reverseList(self, head):
#         """
#         :param head: ListNode

#         :return: ListNode
#         """
#         # 链表为空，或者只有一个结点
#         if not head or not head.next:
#             return head

#         pre = head
#         cur = head.next
#         after = cur.next
#         while after:
#             cur.next = pre
#             pre = cur
#             cur = after
#             after = after.next
#         cur.next = pre
#         head.next = None
#         head = cur
#         return head


if __name__ == "__main__":
    a = List()
    a.built([1, 2, 3, 4, 5])    
    a.print()
    a = List(Solution().reverseList(a.head))
    a.print()