# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
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
        def dfs(head):
            if not head:
                return None
            if head in visited:
                return visited[head]
            clone = Node(head.val)
            visited[head] = clone
            clone.next = dfs(head.next)
            clone.random = dfs(head.random)
            return clone

        visited = {}
        return dfs(head)