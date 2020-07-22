class Solution:
    def lastRemaining(self, n, m):
        """
        Args:
            n: int
            m: int
        
        Return:
            int
        """
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans


# class Solution:
#     def lastRemaining(self, n, m):
#         """
#         Args:
#             n: int
#             m: int
        
#         Return:
#             int
#         """
#         nums = [x for x in range(n)]
#         i = 0
#         while n > 1:
#             i = (i + m - 1) % n
#             nums.pop(i)
#             n -= 1
#         return nums[0]