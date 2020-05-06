# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:56:18 2019

@author: 54949
"""

class Solution:
    def knapsack01(self, w, v, C):
        '''
        F(n, C)考虑将n个物品放进容量为C的背包，使得价值最大
        F(i, c) = max(F(i - 1, c), v(i) + F(i - 1, c - w(i)))
        '''
        assert len(w) ==len(v)
        n = len(w)
        if n == 0:
            return 0
        
        memo = [-1 for _ in range(C + 1)]
        
        for j in range(C + 1):
            memo[j] = (v[0] if j >= w[0] else 0)
            
        for i in range(n):
            j = C
            while j >= w[i]:
                memo[j] = max(memo[j], v[i] + memo[j - w[i]])
                j -= 1
        
        return memo[(n - 1) % 2][C]
        
#        assert len(w) ==len(v)
#        n = len(w)
#        if n == 0:
#            return 0
#        
#        memo = [[-1 for _ in range(C + 1)] for _ in range(2)]
#        
#        for j in range(C + 1):
#            memo[0][j] = (v[0] if j >= w[0] else 0)
#            
#        for i in range(n):
#            for j in range(C + 1):
#                memo[i % 2][j] = memo[(i - 1) % 2][j]
#                if j >= w[i]:
#                    memo[i % 2][j] = max(memo[i % 2][j], v[i] + memo[(i - 1) % 2][j - w[i]])
#        
#        return memo[(n - 1) % 2][C]
        
#    def knapsack01(self, w, v, C):
#        
#        n = len(w)
#        self.__memo = [[-1 for _ in range(C + 1)] for _ in range(n)]
#        return self.__best_value(w, v, n - 1, C)
#    
#    def __best_value(self, w, v, index, c):
#        if index < 0 or c <= 0:
#            return 0
#        
#        if self.__memo[index][c] != -1:
#            return self.__memo[index][c]
#        
#        res = self.__best_value(w, v, index - 1, c)
#        if c >= w[index]:
#            res =max(res, v[index] + self.__best_value(w, v, index - 1, c - w[index]))
#        
#       self.__ memo[index][c] = res
#       return res
