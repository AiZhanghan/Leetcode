# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:10:22 2019

@author: Administrator
"""

class Solution:
    def partition(self, s):
        
        solutions = []
        if not s:
            return solutions
        
        self.__partition(s, solutions, 0, [])
        return solutions
    
    def __partition(self, s, solutions, index, partitioned):
        
        if index == len(s):
            solutions.append(partitioned)
            return
        
        i = 1
        while True:
            if index + i > len(s):
                break
            sub_s = s[index: index + i]
            if not self.__is_palindrome(sub_s):
                i += 1
                continue
            self.__partition(s, solutions, index + i, partitioned + [sub_s])
            i += 1
        
    def __is_palindrome(self, s):
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
if __name__ == '__main__':
    s = "efe"
    res = Solution().partition(s)