# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:08:29 2019

@author: Administrator
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.__m = len(grid)
        if self.__m == 0:
            return 0
        self.__n = len(grid[0])
        
        self.__visited = [[False for _ in range(self.__n)] for _ in range(self.__m)]
        self.__d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        res = 0
        for i in range(self.__m):
            for j in range(self.__n):
                if grid[i][j] == '1' and not self.__visited[i][j]:
                    res += 1
                    self.__dfs(grid, i, j)
        
        return res
    
    def __dfs(self, grid, x, y):
        
        self.__visited[x][y] = True
        for i in range(4):
            new_x = x + self.__d[i][0]
            new_y = y + self.__d[i][1]
            if(self.__in_area(new_x, new_y) and 
               not self.__visited[new_x][new_y] and
               grid[new_x][new_y] == '1'):
                self.__dfs(grid, new_x, new_y)
            
    def __in_area(self, x, y):
        return 0 <= x < self.__m and 0 <= y < self.__n
        