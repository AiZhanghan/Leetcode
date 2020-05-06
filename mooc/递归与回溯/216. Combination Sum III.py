# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:40:54 2019

@author: Administrator
"""

class Solution:
    def combinationSum3(self, k, n: int):
        
        res = []
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        c = []
        self.__combination_sum3(candidates, n, 0, c, res, k)
        return res
        
    def __combination_sum3(self, candidates, target, start, c, res, k):
        
        if target == 0 and len(c) == k:
            res.append(c[:])
            return
        
        if target < 0 or len(c) >= k:
            return
        
        for i in range(start, len(candidates)):
            c.append(candidates[i])
            if target - candidates[i] < 0:
                c.pop()
                break
            self.__combination_sum3(candidates, target - candidates[i], i + 1, c, res, k)
            c.pop()
        
        return

if __name__ == '__main__':
    k = 3
    n = 9
    res = Solution().combinationSum3(k, n)