# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:23:54 2019

@author: Administrator
"""

class Solution:
    def subsets(self, nums):
        
        res = []
        c = []
        
        for count in range(len(nums) + 1):
            self.__subsets(nums, count, 0, c, res)
            
        return res
        
    def __subsets(self, nums, count, start, c, res):
        
        if len(c) == count:
            res.append(c[:])
            return
        
        for i in range(start, len(nums)):
            c.append(nums[i])
            self.__subsets(nums, count, i + 1, c, res)
            c.pop()
        
        return
    
if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution().subsets(nums)