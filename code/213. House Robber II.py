# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:20:49 2019

@author: 54949
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.__rob_line(nums[:-1]), self.__rob_line(nums[1:]))
        
    def __rob_line(self, nums):
        
        n = len(nums)
        if n == 0:
            return 0
        
        memo = [-1 for _ in range(n)]
        memo[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                memo[i] = max(memo[i], nums[j] + (memo[j + 2] if j + 2 < n else 0))
                
        return memo[0]
    