class Solution:
    def uniquePaths(self, m, n):
        """DP
        
        Args:
            m: int
            n: int
        
        Return:
            int
        """
        dp = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == "__main__":
    m = 3
    n = 2
    print(Solution().uniquePaths(3, 2))