# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:19:23 2019

@author: Administrator
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [char for char in s if char.isalnum()]
        s = ''.join(s)
        s = s.lower()
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        