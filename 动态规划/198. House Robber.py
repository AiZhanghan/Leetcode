# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:40:12 2019

@author: 54949
"""

class Solution:
    def rob(self, nums):
        
        n = len(nums)
        if n == 0:
            return 0
        
        memo = [-1 for _ in range(n)]
        memo[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                memo[i] = max(memo[i], nums[j] + (memo[j + 2] if j + 2 < n else 0))
                
        return memo[0]
    
#    def rob(self, nums: List[int]) -> int:
#        
#        self.__memo = [-1 for _ in range(len(nums))]
#        return self.__try_rob(nums, 0)
#        
#    def __try_rob(self, nums, index):
#        
#        if index >= len(nums):
#            return 0
#        
#        if self.__memo[index] != -1:
#            return self.__memo[index]
#        
#        res = 0
#        for i in range(index, len(nums)):
#            res = max(res, nums[i] + self.__try_rob(nums, i + 2))
#        self.__memo[index] = res
#        
#        return res
#            

if __name__ == '__main__':
    nums = [1,2,3,1]
    res = Solution().rob(nums)