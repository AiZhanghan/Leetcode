# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:30:06 2019

@author: 54949
"""

class Solution:
    
    def canPartition(self, nums):
        
        if sum(nums) % 2:
            return False
        
        n = len(nums)
        c = int(sum(nums) / 2)
        memo = [False for _ in range(c + 1)]
        
        for i in range(c + 1):
            memo[i] = (nums[0] == i)
            
        for i in range(1, n):
            j = c
            while j >= nums[i]:
                memo[j] = memo[j] or memo[j - nums[i]]
                j -= 1
        
        return memo[c]
    
#    def canPartition(self, nums):
#        
#        _sum = sum(nums)
#        if _sum % 2 != 0:
#            return False
#        
#        self.__memo = [[-1 for _ in range(int(_sum / 2) + 1)] for _ in range(len(nums))]
#        return self.__try_partition(nums, len(nums) - 1, int(_sum / 2))
#    
#    def __try_partition(self, nums, index, _sum):
#        
#        if _sum == 0:
#            return True
#        
#        if _sum < 0 or index < 0:
#            return False
#        
#        if self.__memo[index][_sum] != -1:
#            return self.__memo[index][_sum] == 1
#        
#        self.__memo[index][_sum] = (1 if (self.__try_partition(nums, index - 1, _sum) or
#                   self.__try_partition(nums, index - 1, _sum - nums[index])) else 0)
#        
#        return self.__memo[index][_sum] == 1
#    
if __name__ == '__main__':
    nums = [1,2,5]
    res = Solution().canPartition(nums)