# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:39:05 2019

@author: Administrator
"""

class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        
        candidates.sort()
        
        if candidates[0] > target:
            return res
        
        c = []
        self.__combination_sum(candidates, target, 0, c, res)
        
        return res
        
    def __combination_sum(self, candidates, target, start, c, res):
        
        if target == 0:
            res.append(c[:])
            return
        
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            c.append(candidates[i])
            self.__combination_sum(candidates, target - candidates[i], i + 1, c, res)
            c.pop()
        
        return
    
if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = Solution().combinationSum2(candidates, target)