# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root, k):
        """
        Args:
            root: TreeNode
            k: int
        
        Return:
            int
        """
        self.res = None
        self.k = k
        self.dfs(root)
        return self.res

    def dfs(self, root):
        """
        Args:
            root: TreeNode
        """
        if not root:
            return
        self.dfs(root.right)
        if self.k == 0:
            return
        self.k -= 1
        if self.k == 0:
            self.res = root.val
        self.dfs(root.left)
