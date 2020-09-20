class Solution:
    def lastRemaining(self, n, m):
        """
        Args:
            n: int
            m: int
        
        Return:
            int
        """
        nums = [i for i in range(n)]
        index = 0
        while n > 1:
            index = (index + m - 1) % n
            nums.pop(index)
            n -= 1
        return nums[0]


# class Solution:
#     def lastRemaining(self, n, m):
#         """
#         Args:
#             n: int
#             m: int
        
#         Return:
#             int
#         """
#         res = 0
#         for i in range(2, n + 1):
#             res = (res + m) % i
#         return res