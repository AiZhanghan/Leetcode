# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def sortedListToBST(self, head):
#         """
#         Args:
#             head: ListNode
        
#         Return:
#             TreeNode
#         """
#         if not head:
#             return
#         length = 0
#         self.cur = head
#         while head:
#             length += 1
#             head = head.next
        
#         return self.build_BST(0, length - 1)
    
#     def build_BST(self, start, end):
#         """
#         Args:
#             start: int
#             end: int
        
#         Returnl:
#             TreeNode
#         """
#         if start > end:
#             return
#         mid = (start + end + 1) // 2
#         left = self.build_BST(start, mid - 1)
#         root = TreeNode(self.cur.val)
#         self.cur = self.cur.next
#         root.left = left
#         root.right = self.build_BST(mid + 1, end)
#         return root


class Solution:
    def sortedListToBST(self, head):
        """
        Args:
            head: ListNode
        
        Return:
            TreeNode
        """
        return self.build_BST(head, None)
    
    def build_BST(self, left, right):
        """
        Args:
            left: TreeNode
            right: TreeNode
        
        Return:
            TreeNode
        """
        if left == right:
            return
        mid = self.get_median(left, right)
        root = TreeNode(mid.val)
        root.left = self.build_BST(left, mid)
        root.right = self.build_BST(mid.next, right)
        return root
    
    def get_median(self, left, right):
        """
        Args:
            left: TreeNode
            right: TreeNode
        
        Return:
            TreeNode
        """
        fast = slow = left
        while fast != right and fast.next != right:
            fast = fast.next.next
            slow = slow.next
        return slow


# class Solution:
#     def sortedListToBST(self, head):
#         """
#         Args:
#             head: ListNode
        
#         Return:
#             TreeNode
#         """
#         nums = []
#         cur = head
#         while cur:
#             nums.append(cur.val)
#             cur = cur.next
        
#         return self.sorted_list_to_BST(nums, 0, len(nums))
    
#     def sorted_list_to_BST(self, nums, start, end):
#         """
#         Args:
#             nums: list[int]
#             start: int
#             end: int
        
#         Return:
#             TreeNode
#         """
#         if start >= end:
#             return
#         mid = start + (end - start) // 2
#         root = TreeNode(nums[mid])
#         root.left = self.sorted_list_to_BST(nums, start, mid)
#         root.right = self.sorted_list_to_BST(nums, mid + 1, end)
#         return root
    