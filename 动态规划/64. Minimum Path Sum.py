# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:11:22 2019

@author: Administrator
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return
        n = len(grid[0])
        
        memo = [[None for _ in range(n)] for _ in range(m)]
        memo[m - 1][n - 1] = grid[m - 1][n - 1]
        # take memo[m-1] done
        for i in range(n - 2, -1, -1):
            memo[m - 1][i] = grid[m - 1][i] + memo[m - 1][i + 1]
        # take memo[:][n - 1] done
        for i in range(m - 2, -1, -1):
            memo[i][n - 1] = grid[i][n - 1] + memo[i + 1][n - 1]
            
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                memo[i][j] = grid[i][j] + min(memo[i + 1][j], memo[i][j + 1])
        
        return memo[0][0]
    