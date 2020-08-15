class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        Args:
            A: list[int]
        
        Return:
            int
        """
        res = 0
        dp = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp = dp + 1
                res += dp
            else:
                dp = 0
        return res


# class Solution:
#     def numberOfArithmeticSlices(self, A):
#         """
#         Args:
#             A: list[int]
        
#         Return:
#             int
#         """
#         count = 0
#         for s in range(len(A) - 2):
#             d = A[s + 1] - A[s]
#             for e in range(s + 2, len(A)):
#                 if A[e] - A[e - 1] == d:
#                     count += 1
#                 else:
#                     break
#         return count


