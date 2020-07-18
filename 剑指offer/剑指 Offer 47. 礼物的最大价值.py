class Solution:
    def maxValue(self, grid):
        """
        Args:
            grid: list[list[int]]
        
        Return:
            int
        """
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        dp = [0 for _ in range(n + 1)]
        
        for i in range(m):
            for j in range(n):
                dp[j + 1] = max(dp[j], dp[j + 1]) + grid[i][j]
            
        return dp[-1]


# class Solution:
#     def maxValue(self, grid):
#         """
#         Args:
#             grid: list[list[int]]
        
#         Return:
#             int
#         """
#         if not grid:
#             return 0
        
#         m = len(grid)
#         n = len(grid[0])

#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         dp[0][0] = grid[0][0]

#         for j in range(1, n):
#             dp[0][j] = dp[0][j - 1] + grid[0][j]
        
#         for i in range(1, m):
#             dp[i][0] = dp[i - 1][0] + grid[i][0]

#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
#         return dp[-1][-1]


# if __name__ == "__main__":
#     grid = [[1,2],[5,6],[1,1]]
#     print(Solution().maxValue(grid))
