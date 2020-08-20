class Solution:
    def maxProfit(self, prices):
        """
        Args:
            prices: list[int]
        
        Return:
            int
        """
        if not prices:
            return 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
        return max(dp[-1][0], dp[-1][2])


# class Solution:
#     def maxProfit(self, prices):
#         """
#         Args:
#             prices: list[int]
        
#         Return:
#             int
#         """
#         dp_i_0 = 0
#         dp_i_1 = -float("inf")
#         dp_pre_0 = 0
#         for i in range(len(prices)):
#             temp = dp_i_0
#             dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
#             dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
#             dp_pre_0 = temp
#         return dp_i_0