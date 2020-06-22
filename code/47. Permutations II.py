# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:12:19 2019

@author: Administrator
"""
import copy

class Solution:
    
    def permuteUnique(self, nums):
    
        self.__res = []
        if not nums:
            return self.__res
        
        nums.sort()
        self.__used = [False for _ in range(len(nums))]
        self.__generate_permutation(nums, 0, [])
        
        return self.__res
        
        

    def __generate_permutation(self, nums, index, p):
        
        if index == len(nums):
            self.__res.append(copy.copy(p))
            
            return
        
        for i in range(len(nums)):
            if self.__used[i]:
                continue
            if i != 0 and nums[i] == nums[i - 1] and not self.__used[i - 1]:
                continue
            p.append(nums[i])
            self.__used[i] = True
            self.__generate_permutation(nums, index + 1, p)
            p.pop()
            self.__used[i] = False
            
if __name__ == '__main__':
    
    nums = [1, 2, 1]
    res = Solution().permuteUnique(nums)
        