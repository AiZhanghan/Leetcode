class Solution:
    def numSquares(self, n):
        """DP

        Args:
            n: int
        
        Return:
            int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i - j * j] + 1, dp[i])
                j += 1
        return dp[-1]