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
        self.k = k
        self.res = None
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
    


# class Solution:
#     def kthLargest(self, root, k):
#         """
#         Args:
#             root: TreeNode
#             k: int
        
#         Return:
#             int
#         """
#         _, res = self.dfs(root, k)
#         return res
    
#     def dfs(self, root, k):
#         """
#         Args:
#             root: TreeNode
#             k: int
        
#         Return:
#             count: int
#             res: int
#         """
#         if not root:
#             return 0, None
        
#         r_count, r_res = self.dfs(root.right, k)
#         if r_res:
#             return None, r_res
#         if r_count + 1 == k:
#             return None, root.val
        
#         l_count, l_res = self.dfs(root.left, k - r_count - 1)
#         if l_res:
#             return None, l_res
#         return l_count + r_count + 1, None