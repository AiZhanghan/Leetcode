# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:25:53 2019

@author: Administrator
"""

class Solution:
    def combine(self, n, k):
        
        res = []
        if n <= 0 or k <= 0 or k > n:
            return res
        
        c = []
        self.__generate_combinations(n, k, 1, c, res)
        
        return res
        
    def __generate_combinations(self, n, k, start, c, res):
        
        if len(c) == k:
            res.append(c[:])
            return
        
        for i in range(start, n - (k - len(c)) + 1 + 1):
            c.append(i)
            self.__generate_combinations(n, k, i + 1, c, res)
            c.pop()
        
        return

if __name__ == '__main__':
    n = 4
    k = 2
    res = Solution().combine(n, k)
    