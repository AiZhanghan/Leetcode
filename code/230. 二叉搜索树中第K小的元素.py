# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        """
        Args:
            root: TreeNode
            k: int

        Return:
            int
        """
        stack = []
        num = 0
        res = None
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            num += 1
            if num == k:
                res = cur.val
                break
            cur = cur.right
        return res


# class Solution:
#     def kthSmallest(self, root, k):
#         """
#         Args:
#             root: TreeNode
#             k: int

#         Return:
#             int
#         """
#         self.num = 0
#         self.res = None
#         self.dfs(root, k)

#         return self.res
    
#     def dfs(self, root, k):
#         """
#         Args:
#             root: TreeNode
#             k: int
#         """
#         if not root:
#             return
#         self.dfs(root.left, k)
#         self.num += 1
#         if self.num == k:
#             self.res = root.val
#             return
#         self.dfs(root.right, k)


# class Solution:
#     def kthSmallest(self, root, k):
#         """
#         Args:
#             root: TreeNode
#             k: int

#         Return:
#             int
#         """
#         gen = self.mid_order(root)
#         for _ in range(k - 1):
#             next(gen)
#         return next(gen)
    
#     def mid_order(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             int
#         """
#         if not root:
#             return
#         yield from self.mid_order(root.left)
#         yield root.val
#         yield from self.mid_order(root.right)


# class Solution:
#     def kthSmallest(self, root, k):
#         """
#         Args:
#             root: TreeNode
#             k: int

#         Return:
#             int
#         """
#         return self.dfs(root, k)[1]

#     def dfs(self, root, k):
#         """
#         Args:
#             root: TreeNode
#             k: int

#         Return:
#             count: int
#             value: int
#         """
#         if not root:
#             return 0, None
        
#         left_count, left_value = self.dfs(root.left, k)
#         # 左子树中有第k个结点
#         if left_count == k:
#             return k, left_value
#         # 当前root为第k个结点
#         if left_count == k - 1:
#             return k, root.val
#         # 在右子树
#         right_count, right_value = self.dfs(root.right, k - left_count - 1)
#         if right_count == k - left_count - 1:
#             return k, right_value

#         return left_count + right_count + 1, None