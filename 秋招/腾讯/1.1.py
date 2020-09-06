class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def func(self, nums1, nums2):
        """
        Args:
            nums1: list[int]
            nums2: list[int]
        
        Return:
            list[int]
        """
        head1 = self.build_list(nums1)
        head2 = self.build_list(nums2)
        p1 = head1
        p2 = head2
        res = []
        while p1 and p2:
            if p1.val < p2.val:
                p2 = p2.next
            elif p1.val > p2.val:
                p1 = p1.next
            else:
                res.append(p1.val)
                p1 = p1.next
                p2 = p2.next
        return res

    def build_list(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    n = int(input()) 
    nums1 = list(map(int, input().split()))
    m = int(input()) 
    nums2 = list(map(int, input().split()))
    res = Solution().func(nums1, nums2)
    print(" ".join(map(str, res)))