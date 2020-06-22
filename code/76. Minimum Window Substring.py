# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:40:47 2019

@author: Administrator
"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or not s:
            return ''
        
        dict_t = Counter(t)
        
        required = len(dict_t)
        
        l, r = 0, 0
        
        formed = 0
        
        window_counts = {}
        
        ans = (float('inf'), None, None)
        
        while r < len(s):
            
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
                
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] <dict_t[character]:
                    formed -= 1
                    
                l += 1
            
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]
        
#    def minWindow(self, s: str, t: str) -> str:
#
#        #slide window[l....r]
#        l = 0
#        r = -1
#        t_counter = Counter(t)
#        if self.is_anagrams(s, t):
#            return s
#        
#        min_window = [0, len(s)]
#        
#        while l < len(s) - len(t):
#            while l < len(s) - len(t) and s[l] not in t_counter:
#                l += 1
#                
#            if r < l - 1:
#                r = l - 1
#                
#            while not self.is_contained(t_counter) and r + 1 < len(s):
#                r += 1
#                if s[r] in t_counter:
#                    t_counter[s[r]] -= 1
#            if min_window[1] - min_window[0] > r - l:
#                min_window = [l, r]
#            
##            assert s[l] in t_counter
#            t_counter[s[l]] += 1
#            l += 1
#            
#        if (len(s[min_window[0]: min_window[1] + 1]) < len(t) or 
#            min_window[1] + 1 - min_window[0] > len(s)):
#            return ''
#        
#        if (len(s[min_window[0]: min_window[1] + 1]) == len(t) and
#            not self.is_anagrams(s[min_window[0]: min_window[1] + 1], t)):
#            return ''
#        
#        return s[min_window[0]: min_window[1] + 1]
#            
#    
#    def is_contained(self, t_counter):
#        for i in t_counter.values():
#            if i > 0:
#                return False
#        return True
#    
#    def is_anagrams(self, t, s):
#        t_counter = Counter(t)
#        s_counter = Counter(s)
#        return s_counter == t_counter
    
if __name__ == '__main__':
#    s = "a"
#    t = "a"
#    s = "ADOBECODEBANC"
#    t = "ABC"
#    s = 'a'
#    t = 'b'
#    s = 'ab'
#    t = 'A'
#    s = 'abc'
#    t = 'cba'
    s = 'bba'
    t = 'ab'

    print(Solution().minWindow(s, t))