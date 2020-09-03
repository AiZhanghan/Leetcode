# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root, k):
        """
        Args:
            root: TreeNode
            k: int
        
        Return:
            bool
        """
        visited = set()
        return self.dfs(root, k, visited)
    
    def dfs(self, root, k, visited):
        """
        Args:
            root: TreeNode
            k: int
            visited: set
        
        Return:
            bool
        """
        if not root:
            return False
        if k - root.val in visited:
            return True
        visited.add(root.val)
        return self.dfs(root.left, k, visited) \
            or self.dfs(root.right, k, visited)