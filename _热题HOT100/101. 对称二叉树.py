from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """迭代, 队列"""
        if not root:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True


# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         """递归"""
#         if not root:
#             return True
#         return self.is_symmetric(root.left, root.right)
    
#     def is_symmetric(self, root1: TreeNode, root2: TreeNode) -> bool:
#         if not root1 and not root2:
#             return True
#         if not root1 or not root2 or root1.val != root2.val:
#             return False
#         return self.is_symmetric(root1.left, root2.right) \
#             and self.is_symmetric(root1.right, root2.left)