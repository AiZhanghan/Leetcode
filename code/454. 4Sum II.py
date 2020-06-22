# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:20:36 2019

@author: Administrator
"""

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        #time O(n^2)
        #space O(n^2)
        record = {}
        for i in range(len(C)):
            for j in range(len(D)):
                if C[i] + D[j] not in record:
                    record[C[i] + D[j]] = 1
                else:
                    record[C[i] + D[j]] += 1
        
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if 0 - A[i] - B[j] in record:
                    res += record[0 - A[i] - B[j]]
                    
        return res