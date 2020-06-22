# class Solution:
#     def lastRemaining(self, n, m):
#         """
#         Args:
#             n: int
#             m: int
        
#         Return:
#             int
#         """
#         arr = [x for x in range(n)]
#         idx = 0
#         while n > 1:
#             idx = (idx + m - 1) % n
#             del arr[idx]
#             n -= 1
#         return arr[0]


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
