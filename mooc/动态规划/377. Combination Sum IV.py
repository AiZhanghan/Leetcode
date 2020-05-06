# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:03:44 2019

@author: 54949
"""

class Solution:
#    def combinationSum4(self, nums, target):
#        
#        if not nums:
#            return 0
#        
#        nums.sort()
#        memo = [0 for _ in range(target + 1)]
#        memo[0] = 1
#        for i in range(1, target + 1):
#            for j in range(0, len(nums)):
#                if nums[j] > i:
#                    break
#                memo[i] += memo[i - nums[j]]
#        
#        return memo[-1]
        
        
#    def combinationSum4(self, nums, target):
#        if not nums:
#            return 0
#        
#        nums.sort()
#        self.memo = [None for _ in range(target + 1)]
#        return self.combination_sum(nums, target)
#    
#    def combination_sum(self, nums, target):
#        '''
#        状态：f(target) = nums中能找到和为target的组合数
#        状态方程：f(target) = f(target - nums[0]) + f(target - nums[1]) + ... + f(target - nums[-1])
#        '''
#        # target == 0， 找到一种， 返回1
#        if target == 0:
#            return 1
#        # target < min(nums), 返回0
#        if target < nums[0]:
#            return 0
#        if self.memo[target]:
#            return self.memo[target]
#        
#        res = 0
#        for i in range(len(nums)):
#            if target - nums[i] < 0:
#                return 0
#            res += self.combination_sum(nums, target - nums[i])
#        
#        self.memo[target] = res
#        
#        return res

if __name__ == '__main__':
    nums = [3,33,333]
    target = 10000
    res = Solution().combinationSum4(nums, target)
    