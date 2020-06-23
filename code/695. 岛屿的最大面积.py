class Solution:
    def maxAreaOfIsland(self, grid):
        """
        Args:
            grid: list[list[int]]

        Return:
            int
        """
        res = 0
        self.grid = grid
        self.visited = [[False for _ in range(len(grid[0]))]
            for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, self.dfs(i, j))
        
        return res

    def dfs(self, i, j):
        """
        Args:
            i: int
            j: int
        
        Return:
            area: int
        """
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) \
            or not self.grid[i][j] or self.visited[i][j]:
            return 0
        self.visited[i][j] = True
        area = 1
        
        area += self.dfs(i + 1, j)
        area += self.dfs(i - 1, j)
        area += self.dfs(i, j + 1)
        area += self.dfs(i, j - 1)
        
        return area
        

if __name__ == "__main__":
    grid = [[1,1],[1,0]]
    print(Solution().maxAreaOfIsland(grid))