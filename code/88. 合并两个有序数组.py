class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        
        Args:
            nums1: list[int]
            m: int
            nums2: list[int]
            n: int
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

            
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         Do not return anything, modify nums1 in-place instead.
        
#         Args:
#             nums1: list[int]
#             m: int
#             nums2: list[int]
#             n: int
#         """
#         i = j = 0
#         nums = []
#         while i < m and j < n:
#             if nums1[i] < nums2[j]:
#                 nums.append(nums1[i])
#                 i += 1
#             else:
#                 nums.append(nums2[j])
#                 j += 1
#         while i < m:
#             nums.append(nums1[i])
#             i += 1
#         while j < n:
#             nums.append(nums2[j])
#             j += 1
#         nums1[:] = nums
        
