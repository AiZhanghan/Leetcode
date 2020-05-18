# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
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
#         self.father = {}
#         visited = set()
#         self.father[root.val] = None
#         self.dfs(root)
#         while p:
#             visited.add(p.val)
#             p = self.father[p.val]
#         while q:
#             if q.val in visited:
#                 return q
#             q = self.father[q.val]    
    
#     def dfs(self, root):
#         """
#         Args:
#             root: TreeNode
#         """
#         if root.left:
#             self.father[root.left.val] = root
#             self.dfs(root.left)
#         if root.right:
#             self.father[root.right.val] = root
#             self.dfs(root.right)


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
#         self.res = None
#         self.dfs(root, p, q)
#         return self.res
    
#     def dfs(self, root, p, q):
#         """
#         Args:
#             root: TreeNode
#             p: TreeNode
#             q: TreeNode
        
#         Return:
#             bool
#         """
#         if not root:
#             return False
#         lson = self.dfs(root.left, p, q)
#         rson = self.dfs(root.right, p, q)
#         if (lson and rson) \
#             or ((lson or rson) and (root.val == p.val or root.val == q.val)):
#             self.res = root
#         return lson or rson or root.val == p.val or root.val == q.val
        

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
#         path_p = [root]
#         self.dfs(root, p, path_p)
#         path_q = [root]
#         self.dfs(root, q, path_q)
#         for i in range(min(len(path_p), len(path_q))):
#             if path_p[i] != path_q[i]:
#                 return path_p[i - 1]
#         return path_p[i]

#     def dfs(self, root, target, path):
#         """
#         Args:
#             root: TreeNode
#             target: TreeNode
#             path: list[TreeNode]
        
#         Return:
#             bool
#         """
#         if root == target:
#             return True
#         if root.left:
#             path.append(root.left)
#             if self.dfs(root.left, target, path):
#                 return True
#             path.pop()
#         if root.right:
#             path.append(root.right)
#             if self.dfs(root.right, target, path):
#                 return True
#             path.pop()
#         return False
