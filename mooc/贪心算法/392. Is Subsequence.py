# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:49:00 2019

@author: 54949
"""

class Solution:
    def isSubsequence(self, s, t):
        
        si = 0
        ti = 0
        
        while ti < len(t):
            if si == len(s):
                return True
            
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                ti += 1
        
        if si == len(s):
            return True
        
        return False

if __name__ == '__main__':
    s = 'abc'
    t = 'ahbgdc'
    res = Solution().isSubsequence(s, t)