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
        
        self.pre = None
        self.head = None
        self.dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head

        return self.head
    
    def dfs(self, cur):
        """
        Args:
            cur: Node
        """
        if not cur:
            return
        
        self.dfs(cur.left)
        if self.pre:
            self.pre.right = cur
            cur.left = self.pre
        else:
            self.head = cur
        self.pre = cur
        self.dfs(cur.right)
        