# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root):
        """
        Args:
            TreeNode
        
        Return:
            TreeNode
        """
        if not root:
            return
            
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left

        return root


# class Solution:
#     def mirrorTree(self, root):
#         """
#         Args:
#             TreeNode
        
#         Return:
#             TreeNode
#         """
#         if not root:
#             return
        
#         temp = root.right
#         root.right = self.mirrorTree(root.left)
#         root.left = self.mirrorTree(temp)
        
#         return root