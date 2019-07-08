# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:56:09 2019

@author: Administrator
"""

class Solution:
    def combinationSum(self, candidates, target):
        
        res = []
        
        candidates.sort()
        
        if candidates[0] > target:
            return res
        
        c = []
        self.__combination_sum(candidates, target, c, res)
        
        return res
        
    def __combination_sum(self, candidates, target, c, res):
        
        if target == 0:
            res.append(c[:])
            return
        
        if target < candidates[0]:
            return
        
        for i in range(0, len(candidates)):
            c.append(candidates[i])
            self.__combination_sum(candidates[i:], target - candidates[i], c, res)
            c.pop()
        
        return

if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    res = Solution().combinationSum(candidates, target)