# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            TreeNode
        """
        return self.sorted_arrat_to_BST(nums, 0, len(nums))
    
    def sorted_arrat_to_BST(self, nums, start, end):
        """
        Args:
            nums: list[int]
            start: int
            end: int
        
        Return:
            TreeNode
        """
        if start >= end:
            return
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.sorted_arrat_to_BST(nums, start, mid)
        root.right = self.sorted_arrat_to_BST(nums, mid + 1, end)
        return root