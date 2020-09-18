class Solution:
    def sumNums(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        return n and (n + self.sumNums(n - 1))


# class Solution:
#     def __init__(self):
#         self.res = 0

#     def sumNums(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             int
#         """
#         n > 1 and self.sumNums(n - 1)
#         self.res += n
#         return self.res