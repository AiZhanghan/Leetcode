class Solution:
    def isPowerOfTwo(self, n):
        """
        Args:
            n: int
        
        Return:
            bool
        """
        return n > 0 and n & (n - 1) == 0


# class Solution:
#     def isPowerOfTwo(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             bool
#         """
#         if n < 1:
#             return False
#         n = bin(n)[2:]
#         has_one = False
#         for c in n:
#             if c == "1":
#                 if has_one:
#                     return False
#                 has_one = True
#         return True
