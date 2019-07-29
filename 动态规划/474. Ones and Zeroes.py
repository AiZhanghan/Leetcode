# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:36:17 2019

@author: 54949
"""

class Solution:
    # DP
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        状态：f(len(array), m, n):考虑将array中str放入限制为m, n的背包，使其str数量最多
        状态方程：f(i, m, n) = max(f(i - 1, m, n), 1 + f(i - 1, m - array[i].count(0), n - array[i].count(1)))
        '''
        if not strs:
            return 0
        
        strs_count = []
        for i in range(len(strs)):
            strs_count.append([strs[i].count('0'), strs[i].count('1')])
        strs_count.sort()
        
        memo = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs_count))]
        
        for i in range(m + 1):
            for j in range(n + 1):
                memo[0][i][j] = (1 if i >= strs_count[0][0] and j >= strs_count[0][1] else 0)
        
        for i in range(len(strs_count)):
            for j in range(m + 1):
                for k in range(n + 1):
                    memo[i][j][k] = memo[i - 1][j][k]
                    if j >= strs_count[i][0] and k >= strs_count[i][1]:
                        memo[i][j][k] = max(memo[i][j][k], 1 + memo[i - 1][j - strs_count[i][0]][k - strs_count[i][1]])
        
        return memo[-1][-1][-1]
    
    
    
    
#    # recursion
#    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#        '''
#        状态：f(len(array), m, n):考虑将array中str放入限制为m, n的背包，使其str数量最多
#        状态方程：f(i, m, n) = max(f(i - 1, m, n), 1 + f(i - 1, m - array[i].count(0), n - array[i].count(1)))
#        '''
#        if not strs:
#            return 0
#        
#        strs_count = []
#        for i in range(len(strs)):
#            strs_count.append([strs[i].count('0'), strs[i].count('1')])
#        strs_count.sort()
#        
#        self.memo = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs_count))]
#        
#        return self.find_max_form(strs_count, m, n, len(strs_count) - 1)
#        
#        
#    def find_max_form(self, strs_count, m, n, index):
#        if index < 0 or m < 0 or n < 0:
#            return 0
#        
#        if self.memo[index][m][n] != -1:
#            return self.memo[index][m][n]
#        
#        res = self.find_max_form(strs_count, m, n, index - 1)
#        if m >= strs_count[index][0] and n >= strs_count[index][1]:
#            res = max(res, 1 + self.find_max_form(strs_count, m - strs_count[index][0], n - strs_count[index][1], index - 1))
#        
#        self.memo[index][m][n] = res
#        
#        return res
#    