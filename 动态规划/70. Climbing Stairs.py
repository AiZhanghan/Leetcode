# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:43:02 2019

@author: Administrator
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = []
        memo.append(1)
        memo.append(1)
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]
#        self.__memo = [-1 for _ in range(n + 1)]
#        return self.__calc_ways(n)
#    
#    def __calc_ways(self, n):
#        
#        if n == 1:
#            return 1
#        if n == 2:
#            return 2
#        
#        if self.__memo[n] == -1:
#            self.__memo[n] = self.__calc_ways(n - 1) + self.__calc_ways(n - 2)
#        
#        return self.__memo[n]
