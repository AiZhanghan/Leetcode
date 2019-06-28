# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:34:55 2019

@author: Administrator
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                
                c = stack.pop()
                
                if s[i] == ')':
                    match = '('
                elif s[i] == ']':
                    match = '['
                else:
                    assert s[i] == '}'
                    match = '{'
                
                if c != match:
                    return False
        
        if stack:
            return False
        
        return True