import collections


class Solution:
    def intersect(self, nums1, nums2):
        """
        Args:
            nums1: list[int]
            nums2: list[int]
        
        Return:
            list[int]
        """
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        counter = collections.Counter(nums1)
        res = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                res.append(num)
                counter[num] -= 1
    
        return res


# class Solution:
#     def intersect(self, nums1, nums2):
#         """
#         Args:
#             nums1: list[int]
#             nums2: list[int]
        
#         Return:
#             list[int]
#         """
#         nums1.sort()
#         nums2.sort()
#         res = []
#         i = 0
#         j = 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 i += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 res.append(nums1[i])
#                 i += 1
#                 j += 1
#         return res