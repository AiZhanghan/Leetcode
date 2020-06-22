# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:37:46 2019

@author: Administrator
"""
from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        #time O(n^2)
        #space O(n)
        res = 0
        for i in range(len(points)):
            record = defaultdict(int)
            for j in range(len(points)):
                if j != i:
                    record[self.__dis(points[i], points[j])] += 1
            
            for item in record.values():
                if item >= 2:
                    res += item * (item - 1)
                
        return res
    
    def __dis(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2