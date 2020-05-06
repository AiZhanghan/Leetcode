# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:25:04 2019

@author: 54949
"""

class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        
        memo = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], 1 + memo[j])
        
        return max(memo)

if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    res = Solution().lengthOfLIS(nums)