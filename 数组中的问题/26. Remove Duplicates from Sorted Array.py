# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:14:06 2019

@author: Administrator
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for j in range(len(nums)):
            if j < 1 or nums[j] > nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    res = Solution().removeDuplicates(nums)
    print(res, nums)