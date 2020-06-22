from List import List, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = slow.next
        slow.next = None
        head2 = self.reverse_list(head2)
        
        cur = head
        cur2 = head2
        while cur2:
            if cur.val != cur2.val:
                return False
            cur = cur.next
            cur2 = cur2.next
        
        return True
    
    def reverse_list(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    

if __name__ == "__main__":
    l = List()
    l.built([1, 2, 2, 1])
    l.print()
    print(Solution().isPalindrome(l.head))