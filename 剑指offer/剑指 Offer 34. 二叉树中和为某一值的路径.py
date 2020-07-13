# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        Args:
            root: TreeNode
            sum: int
        
        Return:
            list[list[int]]
        """
        self.res = []
        self.target = sum
        self.dfs(root, [], 0)
        return self.res

    
    def dfs(self, root, path, cur_sum):
        """
        Args:
            root: TreeNode
            path: list[int]
            cur_sum: int
        """
        if not root:
            return
        
        path.append(root.val)
        cur_sum += root.val

        if cur_sum == self.target and not root.left and not root.right:
            self.res.append(path[:])

        self.dfs(root.left, path, cur_sum)
        self.dfs(root.right, path, cur_sum)
        path.pop()
