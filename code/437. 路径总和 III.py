# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        Args:
            root: TreeNode
            sum: int
        
        Return:
            int
        """
        prefix_sum_count = {}
        prefix_sum_count[0] = 1
        return self.helper(root, prefix_sum_count, sum, 0)

    def helper(self, node, prefix_sum_count, target, cur_sum):
        """
        Args:
            node: TreeNode
            prefix_sum_count: dict{int: int}
            target: int
            cur_sum: int
        
        Return:
            int
        """
        if not node:
            return 0
        res = 0
        cur_sum += node.val
        res += prefix_sum_count.get(cur_sum - target, 0)
        prefix_sum_count[cur_sum] = prefix_sum_count.get(cur_sum, 0) + 1
        res += self.helper(node.left, prefix_sum_count, target, cur_sum) + \
               self.helper(node.right, prefix_sum_count, target, cur_sum)
        prefix_sum_count[cur_sum] -= 1
        return res


# class Solution:
#     def pathSum(self, root, sum):
#         """
#         Args:
#             root: TreeNode
#             sum: int
        
#         Return:
#             int
#         """
#         if not root:
#             return 0
#         return self.helper(root, sum) + self.pathSum(root.left, sum) \
#                + self.pathSum(root.right, sum)
    
#     def helper(self, root, sum):
#         """
#         Args:
#             root: TreeNode
#             sum: int
        
#         Return:
#             int
#         """
#         if not root:
#             return 0
#         sum -= root.val
#         return (1 if sum == 0 else 0) + self.helper(root.left, sum) \
#                + self.helper(root.right, sum)