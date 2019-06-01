# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:18:08 2019

@author: Administrator
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, -1 #s[l...r] is slide window
        res = 0
        
        while l < len(s):
            if r + 1 < len(s) and s[r+1] not in s[l: r + 1]:
                r += 1
            else:
                l += 1
            res = max(res, r - l + 1)
        return res