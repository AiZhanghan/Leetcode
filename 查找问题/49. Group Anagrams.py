# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:32:39 2019

@author: Administrator
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in d.keys():
                d[key] = [i]
            else:
                d[key].append(i)
        return list(d.values())
        