# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:57:38 2019

@author: 54949
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: (x[1], x[0]))
        
        res = 1
        pre = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[pre][1]:
                res += 1
                pre = i
        
        return len(intervals) - res
        
    
#    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#        if not intervals:
#            return 0
#        
#        intervals.sort(key = lambda x: (x[0], x[1]))
#        # memo[i]表示使用intervals[0...i]的区间能构成的最长不重叠区间序列
#        memo = [1 for _ in range(len(intervals))]
#        for i in range(1, len(intervals)):
#            for j in range(i):
#                if intervals[i][0] >= intervals[j][1]:
#                    memo[i] = max(memo[i], 1 + memo[j])
#        
#        return len(intervals) - max(memo)