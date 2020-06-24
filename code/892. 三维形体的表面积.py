class Solution:
    def surfaceArea(self, grid):
        """
        Args:
            grid: list[list[int]]
        
        Return:
            int
        """
        if not grid:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += self.get_area(grid, i, j)
        return res
    
    def get_area(self, grid, i, j):
        """
        Args:
            grid: list[list[int]]
            i: int
            j: int
        
        Return:
            int
        """
        area = grid[i][j] * 4 + 2
        if i - 1 >= 0 and grid[i - 1][j]:
            area -= min(grid[i][j], grid[i - 1][j]) * 2
        if j - 1 >= 0 and grid[i][j - 1]:
            area -= min(grid[i][j], grid[i][j - 1]) * 2
        return area
        

# class Solution:
#     def surfaceArea(self, grid):
#         """
#         Args:
#             grid: list[list[int]]
        
#         Return:
#             int
#         """
#         if not grid:
#             return 0
#         res = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]:
#                     res += self.get_area(grid, i, j)
#         return res
    
#     def get_area(self, grid, i, j):
#         """
#         Args:
#             grid: list[list[int]]
#             i: int
#             j: int
        
#         Return:
#             int
#         """
#         area = grid[i][j] * 4 + 2
#         if i - 1 >= 0 and grid[i - 1][j]:
#             area -= min(grid[i][j], grid[i - 1][j])
#         if i + 1 < len(grid) and grid[i + 1][j]:
#             area -= min(grid[i][j], grid[i + 1][j])
#         if j - 1 >= 0 and grid[i][j - 1]:
#             area -= min(grid[i][j], grid[i][j - 1])
#         if j + 1 < len(grid[0]) and grid[i][j + 1]:
#             area -= min(grid[i][j], grid[i][j + 1])
#         return area
        