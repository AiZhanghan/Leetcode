class Solution:
    def numWays(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        # dp = [1 for _ in range(n + 1)]
        pre = pre_pre = 1
        for _ in range(2, n + 1):
            cur = pre + pre_pre
            pre_pre = pre
            pre = cur
        return int(pre % (1000000007))


# class Solution:
#     def numWays(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             int
#         """
#         dp = [1 for _ in range(n + 1)]
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return int(dp[-1] % (1000000007))