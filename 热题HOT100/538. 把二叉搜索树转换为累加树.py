# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            TreeNode
        """
        stack = []
        pre = 0
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur.val += pre
            pre = cur.val

            cur = cur.left
        return root


# class Solution:
#     def __init__(self):
#         self.pre = 0

#     def convertBST(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             TreeNode
#         """
#         if not root:
#             return
#         self.convertBST(root.right)
#         root.val += self.pre
#         self.pre = root.val
#         self.convertBST(root.left)
#         return root
