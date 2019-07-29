# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:44:54 2019

@author: 54949
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort(reverse = True)
        s.sort(reverse = True)
        
        si = 0
        gi = 0
        res = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                res += 1
                si += 1
                gi += 1
            else:
                gi += 1
        
        return res
    