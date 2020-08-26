# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root, k):
        """
        Args:
            root: ListNode
            k: int
        
        Return:
            List[ListNode]
        """
        cur = root
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        width, remainder = divmod(length, k)

        res = []
        cur = root
        for i in range(k):
            head = cur
            for _ in range(width + (i < remainder) - 1):
                cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            res.append(head)
        return res
