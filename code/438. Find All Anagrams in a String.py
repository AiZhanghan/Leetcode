# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:29:28 2019

@author: Administrator
"""
from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
#        #slide window [l...len(p) - 1]
#        res = []
#        for i in range(0, len(s) - len(p) + 1):
#            if sorted(s[i: i + len(p)]) == sorted(p):
#                res.append(i)
#                
#        return res
        
        res = []
        p_counter = Counter(p)
        s_counter = Counter(s[: len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                res.append(i - len(p) + 1)
            s_counter[s[i - len(p) + 1]] -= 1
            if s_counter[s[i - len(p) + 1]] == 0:
                del s_counter[s[i - len(p) + 1]]
        return res
        

    
if __name__ == '__main__':
    s = "abab" 
    p = "ab"
    print(Solution().findAnagrams(s, p))