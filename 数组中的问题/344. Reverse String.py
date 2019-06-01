# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:41:34 2019

@author: Administrator
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        
        while l < r:
            s[l] ,s[r] = s[r], s[l]
            l += 1
            r -= 1