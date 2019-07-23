# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:36:17 2019

@author: 54949
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        状态：f(m, n):m个0，n个1能组成的最多array中str
        状态方程：f(m, n) = f(m - 1, n)
        '''