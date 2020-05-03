from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """DP"""
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        # 第0行
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        # 第0列
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
        