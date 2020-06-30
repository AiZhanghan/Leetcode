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
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node


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
#         if root.val > p.val and root.val > q.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif root.val < p.val and root.val < q.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root