# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        Args:
            root: TreeNode
            sum: int
        Return:
            list[list[int]]
        """
        if not root:
            return []
        self.res = []
        self._dfs(root, sum, [])
        return self.res

    def _dfs(self, root, sum, path):
        """
        Args:
            root: TreeNode
            sum: int
            path: list[int]
        """
        path.append(root.val)
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            self.res.append(path[:])
            path.pop()
            return
        if root.left:
            self._dfs(root.left, sum, path)
        if root.right:
            self._dfs(root.right, sum, path)
        path.pop()
        return
    