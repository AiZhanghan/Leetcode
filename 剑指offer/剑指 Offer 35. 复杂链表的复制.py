import collections


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
        visited = {}
        return self.bfs(head)
    
    def bfs(self, head):
        """
        Args:
            head: Node

        Return: 
            Node
        """
        if not head:
            return
        
        clone = Node(head.val)
        queue = collections.deque()
        queue.append(head)
        visited[head] = clone
        while queue:
            temp = queue.popleft()
            if 


# class Solution:
#     def copyRandomList(self, head):
#         """
#         Args:
#             head: Node
        
#         Return:
#             Node
#         """
#         self.visited = {}
#         return self.dfs(head)

#     def dfs(self, head):
#         """
#         Args:
#             head: Node
        
#         Return:
#             Node
#         """
#         if not head:
#             return
        
#         if head in self.visited:
#             return self.visited[head]
        
#         copy = Node(head.val)
#         self.visited[head] = copy
#         copy.next = self.dfs(head.next)
#         copy.random = self.dfs(head.random)

#         return copy

