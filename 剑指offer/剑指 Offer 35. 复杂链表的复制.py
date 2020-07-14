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
        if not head:
            return
        
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old_list = head
        cur_new_list = head.next
        new_head = head.next
        while cur_old_list:
            cur_old_list.next = cur_old_list.next.next
            cur_new_list.next = cur_new_list.next.next \
                if cur_new_list.next else None
            cur_old_list = cur_old_list.next
            cur_new_list = cur_new_list.next

        return new_head


# class Solution:
#     def copyRandomList(self, head):
#         """
#         Args:
#             head: Node
        
#         Return:
#             Node
#         """
#         if not head:
#             return
        
#         self.visited = {}
#         old_node = head
#         new_node = Node(old_node.val)
#         self.visited[old_node] = new_node

#         while old_node:
#             new_node.random = self.get_cloned_node(old_node.random)
#             new_node.next = self.get_cloned_node(old_node.next)

#             old_node = old_node.next
#             new_node = new_node.next
        
#         return self.visited[head]

#     def get_cloned_node(self, node):
#         """
#         Args:
#             node: Node
        
#         Return:
#             Node
#         """
#         if not node:
#             return
        
#         if node not in self.visited:
#             self.visited[node] = Node(node.val)

#         return self.visited[node]
        

# class Solution:
#     def copyRandomList(self, head):
#         """
#         Args:
#             head: Node
        
#         Return:
#             Node
#         """
#         self.visited = {}
#         return self.bfs(head)
    
#     def bfs(self, head):
#         """
#         Args:
#             head: Node

#         Return: 
#             Node
#         """
#         if not head:
#             return
        
#         clone = Node(head.val)
#         queue = collections.deque()
#         queue.append(head)
#         self.visited[head] = clone
#         while queue:
#             temp = queue.popleft()
#             if temp.next and temp.next not in self.visited:
#                 self.visited[temp.next] = Node(temp.next.val)
#                 queue.append(temp.next)
#             if temp.random and temp.random not in self.visited:
#                 self.visited[temp.random] = Node(temp.random.val)
#                 queue.append(temp.random)
#             self.visited[temp].next = self.visited.get(temp.next)
#             self.visited[temp].random = self.visited.get(temp.random)
#         return clone


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

