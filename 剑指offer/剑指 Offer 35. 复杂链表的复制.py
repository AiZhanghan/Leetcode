# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
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
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = cur.next.next
        
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        
        new_head = head.next
        cur = head
        new_cur = new_head
        while cur:
            cur.next = cur.next.next
            new_cur.next = new_cur.next.next if new_cur.next else None
        
        return new_head