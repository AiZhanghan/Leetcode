# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:15:48 2019

@author: Administrator
"""
import copy

class Solution:
    
    def permute(self, nums):
    
        self.__res = []
        if not nums:
            return self.__res
        
        self.__used = [False for _ in range(len(nums))]
        self.__generate_permutation(nums, 0, [])
        
        return self.__res
        
        

    def generate_permutation(self, nums, index, p):
        
        if index == len(nums):
            self.__res.append(copy.copy(p))
            
            return
        
        for i in range(len(nums)):
            if not self.__used[i]:
                p.append(nums[i])
                self.__used[i] = True
                self.__generate_permutation(nums, index + 1, p)
                p.pop()
                self.used[i] = False
                
if __name__ == '__main__':
    
    nums = [1, 2, 3]
    res = Solution().permute(nums)
        