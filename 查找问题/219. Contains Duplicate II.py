# -*- coding: utf-8 -*-
"""
Created on Thu May 30 22:22:55 2019

@author: Administrator
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = set()
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            
            record.add(nums[i])
            
            if len(record) == k + 1:
                record.remove(nums[i - k])
                
        return False