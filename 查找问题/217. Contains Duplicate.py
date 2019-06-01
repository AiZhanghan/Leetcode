# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:24:53 2019

@author: Administrator
"""
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return len(nums) != len(counter)