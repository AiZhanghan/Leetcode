# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:08:53 2019

@author: Administrator
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = [-1 for _ in range(n + 1)]
        
        memo[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                memo[i] = max(memo[i], j * (i - j), j * memo[i - j])
                
        return memo[n]
        
#    def integerBreak(self, n: int) -> int:
#        
#        self.memo = [-1 for _ in range(n + 1)]
#        return self.__integer_break(n)
#    
#    def __integer_break(self, n):
#        
#        if n == 1:
#            return 1
#        
#        if self.memo[n] != -1:
#            return self.memo[n]
#        
#        res = -1
#        for i in range(1, n):
#            res = max(res, i * (n - i), i * self.__integer_break(n - i))
#            
#        self.memo[n] = res
#            
#        return res
#    