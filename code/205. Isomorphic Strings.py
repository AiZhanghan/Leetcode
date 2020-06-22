# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:13:43 2019

@author: Administrator
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = (i, )
            else:
                s_dict[s[i]] = s_dict[s[i]] + (i, )
        
        t_dict = {}
        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = (i, )
            else:
                t_dict[t[i]] = t_dict[t[i]] + (i, )
        
        return list(t_dict.values()) == list(s_dict.values())