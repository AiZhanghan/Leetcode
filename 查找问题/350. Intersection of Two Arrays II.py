# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:54:16 2019

@author: Administrator
"""
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #o(nlogn)
        record = Counter(nums1)
        
        res = []
        #o(nlogn)
        for i in range(len(nums2)):
            if nums2[i] in record and record[nums2[i]] > 0:
                res.append(nums2[i])
                record[nums2[i]] -= 1
        
        return res