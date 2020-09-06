import math


class Solution:
    def isPowerOfFour(self, num):
        """
        Args:
            num: int
        
        Return:
            bool
        """
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0


# class Solution:
#     def isPowerOfFour(self, num):
#         """
#         Args:
#             num: int
        
#         Return:
#             bool
#         """
#         return num > 0 and math.log2(num) % 2 == 0


# class Solution:
#     def isPowerOfFour(self, num):
#         """
#         Args:
#             num: int
        
#         Return:
#             bool
#         """
#         if num == 0:
#             return False
#         while num % 4 == 0:
#             num /= 4
#         return num == 1