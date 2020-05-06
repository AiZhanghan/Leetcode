# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        p = l1
        q = l2
        curr = dummy_head
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum_ = carry + x + y
            carry = sum_ // 10
            curr.next = ListNode(sum_ % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry:
            curr.next = ListNode(carry)
        return dummy_head.next
        

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         carry = 0
#         stack = []
#         while l1 and l2:
#             sum_ = l1.val + l2.val + carry
#             carry = sum_ // 10
#             stack.append(sum_ % 10)
#             l1 = l1.next
#             l2 = l2.next

#         if l2:
#             l1 = l2
#         while l1:
#             sum_ = l1.val + carry
#             carry = sum_ // 10
#             stack.append(sum_ % 10)
#             l1 = l1.next
#         if carry:
#             stack.append(carry)
        
#         head = None
#         while stack:
#             node = ListNode(stack.pop())
#             node.next = head
#             head = node
        
#         return head