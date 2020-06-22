from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        """
        Args:
            root: TreeNode

        Return:
            int
        """
        res = self._rob(root)
        return max(res)

    def _rob(self, root):
        """
        Args:
            root: TreeNode

        Return:
            list[int]
        """
        if not root:
            return [0, 0]
        
        res = [0, 0]
        left = self._rob(root.left)
        right = self._rob(root.right)
        
        res[0] = max(left) + max(right)
        res[1] = left[0] + right[0] + root.val

        return res


# class Solution:
#     def rob(self, root):
#         """
#         Args:
#             root: TreeNode

#         Return:
#             int
#         """
#         self.memo = {}
#         return self._rob(root)
    
#     def _rob(self, root):
#         """
#         Args:
#             root: TreeNode

#         Return:
#             int
#         """
#         if not root:
#             return 0
#         if root in self.memo:
#             return self.memo[root]

#         money = root.val

#         if root.left:
#             money += self.rob(root.left.left) + self.rob(root.left.right)
        
#         if root.right:
#             money += self.rob(root.right.left) + self.rob(root.right.right)
        
#         res = max(money, self.rob(root.left) + self.rob(root.right))
#         self.memo[root] = res

#         return res