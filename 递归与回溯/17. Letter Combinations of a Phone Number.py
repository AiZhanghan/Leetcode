# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:26:51 2019

@author: Administrator
"""

class Solution:
    
    def __init__(self):
        
        self.__letter_map = [' ',
                             '',
                             'abc',
                             'def',
                             'ghi',
                             'jkl',
                             'mno',
                             'pqrs',
                             'tuv',
                             'wxyz']
    
        self.__res = []
    
    def letterCombinations(self, digits: str) -> List[str]:
         
        self.__res = []
        if not digits:
            return self.__res
         
        self.find_combination(digits, 0, '')
          
        return self.__res
     
    def find_combination(self, digits, index, s):
        
        if index == len(digits):
            self.__res.append(s)
            return
        
        c = digits[index]
        assert '0' <= c <= '9' and c != '1'
        letters = self.__letter_map[int(c)]
        for i in range(len(letters)):
            self.find_combination(digits, index + 1, s + letters[i])
            
        return
    