# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:58:54 2019

@author: Administrator
"""

from collections import Counter
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums, k):
        assert k > 0
        
        freq = Counter(nums)
        
        assert k <= len(freq)
        
        pq = PriorityQueue()
        for i in freq.keys():
            if pq.qsize() == k:
                top = pq.get()
                if freq[i] > top[0]:
                    pq.put([freq[i], i])
                else:
                    pq.put(top)
            else:
                pq.put([freq[i], i])
        
        res = []
        while pq.qsize() > 0:
            a = pq.get()
            res.append(a[1])
        
        return res[::-1]
    
if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    res = Solution().topKFrequent(nums, k)