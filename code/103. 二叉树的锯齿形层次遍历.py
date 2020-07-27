import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            list[list[int]]
        """
        if not root:
            return []
        
        res = []
        deque = collections.deque([root])
        count = 1

        while deque:
            temp = collections.deque()
            next_count = 0
            for _ in range(count):
                node = deque.popleft()
                if len(res) % 2:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    deque.append(node.left)
                    next_count += 1
                if node.right:
                    deque.append(node.right)
                    next_count += 1
            res.append(list(temp))
            count = next_count
        
        return res
