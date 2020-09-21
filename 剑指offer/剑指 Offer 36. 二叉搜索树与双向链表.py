# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        """
        Args:
            root: Node

        Return:
            Node
        """
        if not root:
            return
        self.head = None
        self.pre = None
        self.dfs(root)
        self.pre.right = self.head
        self.head.left = self.pre
        return self.head
    
    def dfs(self, root):
        """
        Args:
            root: Node
        """
        if not root:
            return
        self.dfs(root.left)
        if not self.head:
            self.head = root
        else:
            self.pre.right = root
            root.left = self.pre
        self.pre = root
        self.dfs(root.right)