# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:21:43 2019

@author: Administrator
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        m = len(obstacleGrid)
        if not m:
            return
        n = len(obstacleGrid[0])
        
        memo = [[0 for _ in range(n)] for _ in range(m)]
        
        if obstacleGrid[-1][-1] == 0:
            memo[-1][-1] = 1
        else:
            return 0
            
        for i in range(n - 2, -1, -1):
            if obstacleGrid[-1][i] == 1:
                memo[-1][i] = 0
            else:
                memo[-1][i] = memo[-1][i + 1]
            
        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][-1] == 1:
                memo[i][-1] = 0
            else:
                memo[i][-1] = memo[i + 1][-1]
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i + 1][j] + memo[i][j + 1]
        
        return memo[0][0]
    
if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    res = Solution().uniquePathsWithObstacles(obstacleGrid)