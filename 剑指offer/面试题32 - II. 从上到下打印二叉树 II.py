from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            list[int]
        """
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            tmp = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)
        return res
            
# class Solution:
#     def levelOrder(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             list[int]
#         """
#         if not root:
#             return []
        
#         res = []
#         q = deque()
#         q.append((root, 0))
#         while q:
#             node, level = q.popleft()
#             if level == len(res):
#                 res.append([])
#             res[level].append(node.val)
#             if node.left:
#                 q.append((node.left, level + 1))
#             if node.right:
#                 q.append((node.right, level + 1))
#         return res
