# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        """
        Args:
            root: TreeNode
        
        Return:
            list[int]
        """
        if not root:
            return []
        
        self.res = []
        self.pre = None
        self.cur_count = 1
        self.max_count = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        """
        Args:
            root:TreeNode
        """
        if not root:
            return
        
        self.dfs(root.left)

        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            self.cur_count = 1
        
        if self.cur_count == self.max_count:
            self.res.append(root.val)
        elif self.cur_count > self.max_count:
            self.res = [root.val]
            self.max_count = self.cur_count
        
        self.pre = root
        
        self.dfs(root.right)

        