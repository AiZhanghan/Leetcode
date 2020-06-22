# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Args:
            root: TreeNode
        
        Return:
            int
        """
        self.res = 0
        self.depth(root)
        return self.res
    
    def depth(self, root):
        """
        Args:
            root: TreeNode
        """
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.res = max(self.res, l + r)
        return max(l, r) + 1
        

# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             int
#         """
#         res, _ = self.dfs(root)
#         return res
    
#     def dfs(self, root):
#         """
#         Args:
#             root
        
#         Return:
#             max_diameter: int
#             max_depth: int
#         """
#         if not root:
#             return 0, 0
#         left_max_diameter, left_max_depth = self.dfs(root.left)
#         right_max_diameter, right_max_depth = self.dfs(root.right)
#         max_diameter = max(left_max_diameter, right_max_diameter, 
#                            left_max_depth + right_max_depth)
#         max_depth = max(left_max_depth, right_max_depth) + 1
#         return max_diameter, max_depth
