# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:45:25 2019

@author: Administrator
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        c = []
        
        nums.sort()
        
        for count in range(len(nums) + 1):
            self.__subsets_with_dup(nums, count, 0, c, res)
        
        return res
    
    def __subsets_with_dup(self, nums, count, start, c, res):
        
        if len(c) == count:
            res.append(c[:])
            return
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            c.append(nums[i])
            self.__subsets_with_dup(nums, count, i + 1, c, res)
            c.pop()
            
        return 
    