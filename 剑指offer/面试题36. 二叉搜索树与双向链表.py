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
        self.pre = head = Node(0)
        self.dfs(root)
        head = head.right
        head.left = self.pre
        self.pre.right = head
        return head
        
    def dfs(self, cur):
        if not cur:
            return
        self.dfs(cur.left)
        self.pre.right = cur
        cur.left = self.pre
        self.pre = cur
        self.dfs(cur.right)
        