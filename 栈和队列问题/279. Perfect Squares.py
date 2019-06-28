# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:54:09 2019

@author: Administrator
"""

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        
        assert n > 0
        
        q = deque()
        q.append([n, 0])
        
        visited = [False for _ in range(n + 1)]
        visited[n] = True
        
        while q:
            num = q[0][0]
            step = q[0][1]
            q.popleft()

            i = 1
            while True:
                a = num - i * i
                if a < 0:
                    break
                if a == 0:
                    return step + 1
                if not visited[num - i * i]:
                    q.append([num - i * i, step + 1])
                    visited[num - i * i] = True
                i += 1
            