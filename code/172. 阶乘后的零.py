class Solution:
    def trailingZeroes(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        count = 0
        while n > 0:
            count += n // 5
            n //= 5
        return count


# class Solution:
#     def trailingZeroes(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             int
#         """
#         count = 0
#         for i in range(1, n):
#             N = i
#             while N > 0:
#                 if N % 5 == 0:
#                     count += 1
#                     N //= 5
#                 else:
#                     break
#         return count
    