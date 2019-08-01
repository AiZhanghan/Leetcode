# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:26:43 2019

@author: 54949
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        
        return max_length
        
#    def lengthOfLongestSubstring(self, s):
#        '''
#        滑动窗口
#        左指针l, 右指针r, s[l...r]中没有重复元素
#        counter(dict)记录s[l...r]中元素
#        '''
#        if not s:
#            return 0
#        
#        res = 1
#        l = 0
#        r = 0
#        counter = {}
#        counter[s[0]] = 1
#        
#        while r < len(s) - 1:
#            if s[r + 1] not in counter.keys() or counter[s[r + 1]] == 0:
#                r += 1
#                counter[s[r]] = 1
#                res = max(res, r - l + 1)
#            else:
#                while counter[s[r + 1]] != 0:
#                    counter[s[l]] -= 1
#                    l += 1
#                    
#        return res

if __name__ == '__main__':
    s = "pwwkew"
    res = Solution().lengthOfLongestSubstring(s)