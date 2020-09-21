# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        Args:
            root: TreeNode
            p: TreeNode
            q: TreeNode
        
        Return:
            TreeNode
        """
        if p.val > q.val:
            p, q = q, p
        while True:
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                return root
        


# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         Args:
#             root: TreeNode
#             p: TreeNode
#             q: TreeNode
        
#         Return:
#             TreeNode
#         """
#         if p.val > q.val:
#             p, q = q, p
        
#         return self.dfs(root, p, q)
    
#     def dfs(self, root, p, q):
#         """
#         Args:
#             root: TreeNode
#             p: TreeNode
#             q: TreeNode
        
#         Return:
#             TreeNode
#         """
#         if root.val < p.val:
#             return self.dfs(root.right, p, q)
#         if root.val > q.val:
#             return self.dfs(root.left, p, q)
#         return root