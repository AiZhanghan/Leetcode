import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            
        return node.val

# class Solution:
#     def findBottomLeftValue(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             int
#         """
#         res = None
#         queue = collections.deque()
#         queue.append(root)
#         while queue:
#             res = queue[0].val
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return res