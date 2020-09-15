# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        """
        Args:
            n: int
        
        Return:
            list[TreeNode]
        """
        if n == 0:
            return []

        return self.generate_trees(1, n)
    
    def generate_trees(self, start, end):
        """
        Args:
            start: int
            end: int
        
        Return:
            list[TreeNode]
        """
        if start > end:
            return [None]
            
        if start == end:
            return [TreeNode(start)]
        
        res = []
        for i in range(start, end + 1):
            lefts = self.generate_trees(start, i - 1)
            rights = self.generate_trees(i + 1, end)

            for l in lefts:
                for r in rights:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
