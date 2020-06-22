# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:37:20 2019

@author: Administrator
"""

class Solution:
    def numSquares(self, n: int) -> int:
        
        memo = [float('inf') for _ in range(n + 1)]
        memo[0] = 0
        for i in range(1, n + 1):
             for j in range(1, int(i ** 0.5) + 1):
                 memo[i] = min(memo[i], 1 + memo[i - j ** 2])
                
        return memo[n]

if __name__ == '__main__':
    n = 8328
    
    res = Solution().numSquares(n)