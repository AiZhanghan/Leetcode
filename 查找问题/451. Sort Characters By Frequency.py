# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:16:57 2019

@author: Administrator
"""
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        s_sorted = sorted(s_counter.items(), key = lambda t: t[1], reverse = True)
        
        res = ''
        for i in s_sorted:
            res += i[0] * i[1]
        
        return res