# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:31:00 2019

@author: Administrator
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.__m = len(board)
        if self.__m == 0:
            return 
        self.__n = len(board[0])
        
        self.__visited = [[False for _ in range(self.__n)] for _ in range(self.__m)]
        
        self.__o_region = [[False for _ in range(self.__n)] for _ in range(self.__m)]
        self.__d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                
        for i in range(self.__m):
            for j in range(self.__n):
                if(self.__on_the_border(i, j) and
                   not self.__visited[i][j] and 
                   board[i][j] == 'O'):
                    self.__dfs(board, i, j)
        
        for i in range(self.__m):
            for j in range(self.__n):
                if not self.__o_region[i][j]:
                    board[i][j] = 'X'
                    
    def __dfs(self, board, x, y):
        
        self.__visited[x][y] = True
        self.__o_region[x][y] = True
        for i in range(4):
            new_x = x + self.__d[i][0]
            new_y = y + self.__d[i][1]
            if(self.__in_area(new_x, new_y) and
               not self.__visited[new_x][new_y] and 
               board[new_x][new_y] == 'O'):
                self.__dfs(board, new_x, new_y)
    
    def __on_the_border(self, x, y):
        return x == 0 or x == self.__m - 1 or y == 0 or y == self.__n - 1
    
    def __in_area(self, x, y):
        return 0 <= x < self.__m and 0 <= y < self.__n