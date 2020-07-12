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
            list[list[int]]
        """
        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append(root)
        count = 1

        while queue:
            temp = []
            next_count = 0
            
            for _ in range(count):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                    next_count += 1
                if node.right:
                    queue.append(node.right)
                    next_count += 1
            
            count = next_count
            res.append(temp)
        
        return res