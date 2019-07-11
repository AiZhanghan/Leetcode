# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:56:55 2019

@author: Administrator
"""

class Solution:
    def minimumTotal(self, triangle):
        
        height = len(triangle)
        memo = []
        for i in range(height):
            memo.append([None for _ in range(len(triangle[i]))])
        
        memo[-1] = triangle[-1]
        for i in range(height - 2, -1, -1):
            for j in range(len(triangle[i])):
                memo[i][j] = triangle[i][j] + min(memo[i + 1][j], memo[i + 1][j + 1])
        
        return memo[0][0]
        
        
#    def minimumTotal(self, triangle):
#        
#        self.memo = []
#        self.triangle = triangle
#        for i in range(len(triangle)):
#            self.memo.append([None for _ in range(len(triangle[i]))])
#            
#        res = self.__minimum_total(0, 0)
#        
#        return res
#        
#    def __minimum_total(self,row, col):
#        
#        if row == len(self.triangle) - 1:
#            return self.triangle[row][col]
#        
#        if not self.memo[row + 1][col]:
#            self.memo[row + 1][col] = self.__minimum_total(row + 1, col)
##            print(self.memo)
#        
#        if not self.memo[row + 1][col + 1]:
#            self.memo[row + 1][col + 1] = self.__minimum_total(row + 1, col + 1)
##            print(self.memo)
#        
#        return(self.triangle[row][col] + 
#               min(self.memo[row + 1][col], self.memo[row + 1][col + 1]))

if __name__ == '__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    res = Solution().minimumTotal(triangle)