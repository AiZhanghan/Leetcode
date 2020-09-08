# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            list[int]
        """
        res = []
        stack = []
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            temp = stack[-1]
            # 有未遍历的右子树
            if temp.right and temp.right != pre:
                root = temp.right
            else:
                res.append(temp.val)
                pre = temp
                stack.pop()
        return res



# class Solution:
#     def postorderTraversal(self, root):
#         """
#         Args:
#             root: TreeNode
        
#         Return:
#             list[int]
#         """
#         if not root:
#             return []
#         res = []
#         stack = []
#         stack.append(root)
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
        
#         return res[::-1]