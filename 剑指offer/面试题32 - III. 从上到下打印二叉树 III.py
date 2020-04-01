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
            # 打印奇数层
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
            # 打印偶数层
            if not q:
                break
            tmp = []
            n = len(q)
            for _ in range(n):
                node = q.pop()
                tmp.append(node.val)
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
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
#         q.append(root)
#         is_even = False
#         while q:
#             tmp = []
#             n = len(q)
#             for _ in range(n):
#                 node = q.popleft()
#                 tmp.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             if is_even:
#                 tmp.reverse()
#             res.append(tmp)
#             is_even = not is_even
#         return res