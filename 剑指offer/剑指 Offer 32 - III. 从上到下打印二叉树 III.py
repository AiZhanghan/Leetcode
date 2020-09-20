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
            List[int]
        """
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            temp = deque()
            # next_queue = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(temp))
        return res