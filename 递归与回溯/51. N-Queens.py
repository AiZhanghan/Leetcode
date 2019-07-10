# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:52:39 2019

@author: Administrator
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.__res = []
        
        self.__col = [False for _ in range(n)]
        self.__dia1 = [False for _ in range(2 * n - 1)]
        self.__dia2 = [False for _ in range(2 * n - 1)]
        
        row = []
        self.__put_queen(n, 0, row)
        
        return self.__res
    
    def __put_queen(self, n, index, row):
        
        if index == n:
            self.__res.append(self.__generate_board(n, row))
            return
        
        for i in range(n):
            if(not self.__col[i] and
               not self.__dia1[index + i] and
               not self.__dia2[index - i + n - 1]):
                row.append(i)
                self.__col[i] = True
                self.__dia1[index + i] = True
                self.__dia2[index - i + n - 1] = True
                self.__put_queen(n, index + 1, row)
                self.__col[i] = False
                self.__dia1[index + i] = False
                self.__dia2[index - i + n - 1] = False
                row.pop()
            
    def __generate_board(self, n, row):
        assert len(row) == n
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        for i in range(n):
            board[i][row[i]] = 'Q'
            res.append(''.join(board[i]))
        
        return res
    