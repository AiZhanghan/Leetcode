# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            return self.is_equal(s, t) \
                or self.isSubtree(s.left, t) \
                or self.isSubtree(s.right, t)
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_equal(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            return self.is_equal(s.left, t.left) \
                and self.is_equal(s.right, t.right)
        return False