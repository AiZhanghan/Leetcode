"""
TODO

有问题, leetcode给出的非完全二叉树的数组表示
"""

import sys
sys.path.append(r"D:\Workspace\python_workspace")
from util.ToDictMixin import ToDictMixin


class TreeNode(ToDictMixin):
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(array):
    """
    Args:
        array: list[Item]
    Return:
        TreeNode
    
    root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    """
    assert array
    
    root = TreeNode(array[0])
    _build_tree(root, array, 0)
    return root


def _build_tree(root, array, root_index):
    """
    Args:
        root: TreeNode
        array: list[Item]
        root_index: int
    """
    left_index = 2 * root_index + 1
    right_index = 2 * root_index + 2
    if left_index < len(array) and array[left_index]:
        root.left = TreeNode(array[left_index])
        _build_tree(root.left, array, left_index)
    if right_index < len(array) and array[right_index]:
        root.right = TreeNode(array[right_index])
        _build_tree(root.right, array, right_index)
    return


if __name__ == "__main__":
    root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print(root.to_dict())
