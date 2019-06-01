# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:54:02 2019

@author: Administrator
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        return s_counter == t_counter