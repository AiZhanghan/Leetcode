# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:41:17 2019

@author: Administrator
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        record1 = set(nums1)
        record2 = set(nums2)
        result_set = record1.intersection(record2)
        return [i for i in result_set]