class Solution:
    def maxProfit(self, prices, fee):
        """
        Args:
            prices: list[int]
            fee: int
        
        Return:
            int
        """
        if not prices:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return dp[-1][1]