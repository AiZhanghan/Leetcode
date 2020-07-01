class Solution:
    def maxValue(self, grid):
        """
        Args:
            grid: list[list[int]]
        Return:
            int
        """
        # 行数
        m = len(grid)
        # 列数
        n = len(grid[0])
        # 初始化第一行
        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        # 初始化第一列
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        
        return grid[-1][-1]
