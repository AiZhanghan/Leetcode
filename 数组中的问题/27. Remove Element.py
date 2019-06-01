# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:23:45 2019

@author: Administrator
"""

class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0
        lenth = len(nums)
        
        while i < lenth:
            if nums[i] == val:
                nums[i], nums[lenth - 1] = nums[lenth - 1], nums[i]
                lenth -= 1
            else:
                i += 1
        return lenth
    
if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    res = Solution().removeElement(nums, val)
    print(res, nums)