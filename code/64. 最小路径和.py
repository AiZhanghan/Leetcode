class Solution:
    def minPathSum(self, grid):
        """DP
        
        Args:
            grid: list[list[int]]
        
        Return:
            int
        """
        if not grid:
            return 0

        dp = [0 for _ in range(len(grid[0]))]
        dp[0] = grid[0][0]

        for j in range(1, len(grid[0])):
            dp[j] = dp[j - 1] + grid[0][j]
        
        for i in range(1, len(grid)):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, len(grid[0])):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        
        return dp[-1]


# class Solution:
#     def minPathSum(self, grid):
#         """DP
        
#         Args:
#             grid: list[list[int]]
        
#         Return:
#             int
#         """
#         if not grid:
#             return 0

#         m = len(grid)
#         n = len(grid[0])
#         # 第0行
#         for j in range(1, n):
#             grid[0][j] += grid[0][j - 1]
#         # 第0列
#         for i in range(1, m):
#             grid[i][0] += grid[i - 1][0]
        
#         for i in range(1, m):
#             for j in range(1, n):
#                 grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
#         return grid[-1][-1]
        