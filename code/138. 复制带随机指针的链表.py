# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        """
        Args:
            x: int
            next: Node
            random: Node
        """
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        """
        Args:
            head: Node
        
        Return:
            Node
        """
        if not head:
            return
        
        cur = head
        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = cur.next.next
        
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        
        dummy = Node(-1)
        dummy.next = head.next
        cur = head
        cur_copy = dummy.next
        while cur:
            cur.next = cur.next.next
            cur_copy.next = cur_copy.next.next if cur_copy.next else None
            cur = cur.next
            cur_copy = cur_copy.next
        
        return dummy.next