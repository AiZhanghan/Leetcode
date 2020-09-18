class Solution:
    def maxValue(self, grid):
        """
        Args:
            grid: list[list[int]]
        
        Return:
            int
        """
        # 第一行
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
        # 第一列
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]