# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


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
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return res