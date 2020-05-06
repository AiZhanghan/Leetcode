# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:04:52 2019

@author: Administrator
"""

class Solution:
    #time O(n)
    #space O(1)
    def minSubArrayLen(self, s, nums):
        l, r = 0, -1 #nums[l...r] is the slide window
        _sum = 0
        res = len(nums) + 1
        
        while l < len(nums):
            if r + 1 < len(nums) and _sum < s:
                r += 1
                _sum += nums[r]
            else:
                _sum -= nums[l]
                l += 1
            
            if _sum >= s:
                res = min(res, r - l + 1)
        
        if res == len(nums) + 1:
            return 0
        
        return res
        
if __name__ == '__main__':
    s = 7
    nums = [2,3,1,2,4,3]
    print(Solution().minSubArrayLen(s, nums))