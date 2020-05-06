# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:06:31 2019

@author: Administrator
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[m - 1] = [1 for i in range(n)]
        for i in range(m):
            dp[i][-1] = 1
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]
    