# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:56:09 2019

@author: Administrator
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        
        while n != 1:
            record.add(n)
            n = self.operate(n)
            if n in record:
                return False
            
        return True
    
    def operate(self, n):
        res = 0
        while n:
            res = res + (n % 10) ** 2
            n = int(n / 10)
        return res