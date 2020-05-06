# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:12:40 2019

@author: Administrator
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.__m = len(board)
        assert self.__m > 0
        self.__n = len(board[0])
        
        self.__visited = [[False for _ in range(self.__n)] for _ in range(self.__m)]
        self.__d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for i in range(self.__m):
            for j in range(self.__n):
                if self.__search_word(board, word, 0, i, j):
                    return True
        
        return False
    
    def __search_word(self, board, word, index, start_x, start_y):
        
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        
        if board[start_x][start_y] == word[index]:
            self.__visited[start_x][start_y] = True
            
            for i in range(4):
                new_x = start_x + self.__d[i][0]
                new_y = start_y + self.__d[i][1]
                if(self.__in_area(new_x, new_y) and 
                   not self.__visited[new_x][new_y] and
                   self.__search_word(board, word, index + 1, new_x, new_y)):
                       return True
            
            self.__visited[start_x][start_y] = False
        
        return False
    
    def __in_area(self, x, y):
        return 0 <= x < self.__m and 0 <= y < self.__n
    