import collections


# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        """
        Args:
            val: int
            left: Node
            right: Node
            next: Node
        """
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        """
        Args:
            root: Node
        
        Return:
            Node
        """
        if not root:
            return
        left = root.left
        right = root.right
        while left:
            left.next = right
            left = left.right
            right = right.left
        self.connect(root.left)
        self.connect(root.right)
        return root


# class Solution:
#     def connect(self, root):
#         """
#         Args:
#             root: Node
        
#         Return:
#             Node
#         """
#         if not root:
#             return
#         pre = root
#         while pre.left:
#             temp = pre
#             while temp:
#                 temp.left.next = temp.right
#                 if temp.next:
#                     temp.right.next = temp.next.left
#                 temp = temp.next
#             pre = pre.left
#         return root

# class Solution:
#     def connect(self, root):
#         """
#         Args:
#             root: Node
        
#         Return:
#             Node
#         """
#         if not root:
#             return
#         queue = collections.deque([root])
    
#         while queue:
#             count = len(queue)
#             pre = queue.popleft()
#             for _ in range(count - 1):
#                 cur = queue.popleft()
#                 pre.next = cur
#                 if pre.left:
#                     queue.append(pre.left)
#                 if pre.right:
#                     queue.append(pre.right)
#                 pre = cur
            
#             if pre.left:
#                 queue.append(pre.left)
#             if pre.right:
#                 queue.append(pre.right)
        
#         return root
