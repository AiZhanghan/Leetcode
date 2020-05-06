# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:34:44 2019

@author: 54949
"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        memo = [1 for _ in range(len(nums))]
        state = [None for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    continue
                if state[j] == None:
                    memo[i] = max(memo[i], 1 + memo[j])
                    state[i] = ('up' if nums[i] > nums[j] else 'down')
                elif state[j] == 'up' and nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
                    state[i] = 'down'
                elif state[j] == 'down' and nums[i] > nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
                    state[i] = 'up'
        
        return max(memo)
    