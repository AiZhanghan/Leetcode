# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def mirrorTree(self, root):
        """
        :param root: TreeNode

        :return: TreeNode
        """
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root


# class Solution:
#     def mirrorTree(self, root):
#         """
#         :param root: TreeNode

#         :return: TreeNode
#         """
#         if not root:
#             return
        
#         root.left, root.right = root.right, root.left
#         self.mirrorTree(root.left)
#         self.mirrorTree(root.right)

#         return root