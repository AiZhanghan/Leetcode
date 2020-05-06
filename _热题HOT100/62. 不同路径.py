class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """DP"""
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]
        

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         """DP"""
#         dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
#         return dp[-1][-1]


if __name__ == "__main__":
    m = 3
    n = 2
    print(Solution().uniquePaths(3, 2))