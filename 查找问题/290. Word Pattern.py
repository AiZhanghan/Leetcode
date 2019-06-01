# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:09:04 2019

@author: Administrator
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = (i, )
            else:
                pattern_dict[pattern[i]] = pattern_dict[pattern[i]] + (i, )
        
        str_dict = {}
        str_list = str.split()
        for i in range(len(str_list)):
            if str_list[i] not in str_dict:
                str_dict[str_list[i]] = (i, )
            else:
                str_dict[str_list[i]] = str_dict[str_list[i]] + (i, )
        
        return list(pattern_dict.values()) == list(str_dict.values())

if __name__ == '__main__':
    pattern = "abba"
    _str = "dog cat cat dog"
    print(Solution().wordPattern(pattern, _str))