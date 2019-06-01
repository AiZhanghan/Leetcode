# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:32:22 2019

@author: Administrator
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #time O(n)
        #space O(n)
        
        record = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in record:
                res = [i, record[complement]]
                return res
            
            record[nums[i]] = i
            