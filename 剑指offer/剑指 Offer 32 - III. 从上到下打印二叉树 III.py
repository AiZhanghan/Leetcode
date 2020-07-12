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
        queue = deque([root])
        count = 1

        while queue:
            next_count = 0
            temp = deque()
            for _ in range(count):
                node = queue.popleft()
                if len(res) % 2:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                    next_count += 1
                if node.right:
                    queue.append(node.right)
                    next_count += 1
            count = next_count
            res.append(list(temp))
        
        return res