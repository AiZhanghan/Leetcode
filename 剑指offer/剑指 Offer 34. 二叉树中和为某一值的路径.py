# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, target):
        """ 
        Args:
            root: TreeNode
            target: int
        
        Return:
            list[list[int]]
        """
        
        self.res = []
        self.dfs(root, [], target)
        return self.res
    
    def dfs(self, root, path, target):
        """
        Args:
            root: TreeNode
            path: list[int]
            target: int
        """
        if not root:
            return

        path.append(root.val)
        target -= root.val

        if target == 0 and not root.left and not root.right:
            self.res.append(path[:])

        self.dfs(root.left, path, target)
        self.dfs(root.right, path, target)
        path.pop()