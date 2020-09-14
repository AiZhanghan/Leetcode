# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# class Solution:
#     def firstBadVersion(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             int
#         """
#         left = 1
#         right = n
#         while left <= right:
#             mid = left + (right - left) // 2
#             if isBadVersion(mid):
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return left