class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """归并

        Args:
            nums1: list[int]
            nums2: list[int]
        
        Return:
            float
        """
        n = len(nums1)
        m = len(nums2)
        left = (n + m + 1) // 2
        right = (n + m + 2) // 2
        return (self.get_kth(nums1, 0, n - 1, nums2, 0, m - 1, left) + \
                self.get_kth(nums1, 0, n - 1, nums2, 0, m - 1, right)) / 2
    
    def get_kth(self, nums1, start1, end1, nums2, start2, end2, k):
        """
        Args:
            nums1: list[int]
            start1: int
            end1: int
            nums2: list[int]
            start2: int
            end2: int
            k: int
        
        Return:
            int
        """
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1

        if len1 > len2:
            return self.get_kth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        
        if k == 1:
            return min(nums1[start1], nums2[start2])
        
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        if nums1[i] > nums2[j]:
            return self.get_kth(nums1, start1, end1, 
                nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.get_kth(nums1, i + 1, end1, 
                nums2, start2, end2, k - (i - start1 + 1))
        

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """归并

#         Args:
#             nums1: list[int]
#             nums2: list[int]
        
#         Return:
#             float
#         """
#         m = len(nums1)
#         n = len(nums2)
#         length = m + n
#         left = -1
#         right = -1
#         a_start = 0
#         b_start = 0
#         for _ in range(int(length // 2) + 1):
#             left = right
#             if a_start < m and (b_start >= n or nums1[a_start] < nums2[b_start]):
#                 right = nums1[a_start]
#                 a_start += 1
#             else:
#                 right = nums2[b_start]
#                 b_start += 1
#         if length & 1 == 0:
#             return (left + right) / 2
#         else:
#             return right


# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """归并

#         Args:
#             nums1: list[int]
#             nums2: list[int]
        
#         Return:
#             float
#         """
#         m = len(nums1)
#         n = len(nums2)
#         nums = [0 for _ in range(m + n)]

#         count = 0
#         i = 0
#         j = 0
#         while count != (m + n):
#             if i == m:
#                 while j != n:
#                     nums[count] = nums2[j]
#                     count += 1
#                     j += 1
#                 break
#             if j == n:
#                 while i != m:
#                     nums[count] = nums1[i]
#                     count += 1
#                     i += 1
#                 break
#             if nums1[i] < nums2[j]:
#                 nums[count] = nums1[i]
#                 count += 1
#                 i += 1
#             else:
#                 nums[count] = nums2[j]
#                 count += 1
#                 j += 1
#         if count % 2 == 0:
#             return (nums[count // 2 - 1] + nums[count // 2]) / 2
#         else:
#             return nums[count // 2]