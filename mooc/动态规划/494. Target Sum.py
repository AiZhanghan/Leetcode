# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:24:48 2019

@author: 54949
"""

class Solution:
    def findTargetSumWays(self, nums, S):
        '''
        f(index, s): 有多少种组合使得nums[index :]凑成s
        f(index, s) = f(index + 1, s + nums[index]) + f(index + 1, s - nums[index])
        '''
        _sum = sum(nums)
        self.memo = {}
        
        return self.find_target_sum_ways(nums, S, 0, _sum)
    
    def find_target_sum_ways(self, nums, s, index, _sum):
        
        if sum(nums[index:]) < abs(s):
            return 0
        
        if index == len(nums):
            if s == 0:
                return 1
            else:
                return 0
        
        if (index, s + _sum) in self.memo:
            return self.memo[(index, s + _sum)]
        
        res = self.find_target_sum_ways(nums, s + nums[index], index + 1, _sum) +\
                self.find_target_sum_ways(nums, s - nums[index], index + 1, _sum)
        
        self.memo[(index, s + _sum)] = res
        
        return res

if __name__ == '__main__':
    nums = [5,40,23,47,43,19,36,10,28,46,14,11,5,0,5,22,39,30,50,41]
    S = 48
    res = Solution().findTargetSumWays(nums, S)