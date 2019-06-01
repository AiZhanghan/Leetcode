# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:27:22 2019

@author: Administrator
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        record = set()
        
        for i in range(len(nums)):
            
            if nums[i] in record:
                return True
            
            record.add(nums[i])
            
            if len(record) == k + 1:
                record.remove(nums[i - k])
                
        return False