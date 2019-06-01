# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:05:57 2019

@author: Administrator
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#        #时间复杂度O(n)
#        #space O(1)
#        count = [0, 0, 0]
#        for i in range(len(nums)):
#            assert 0 <= nums[i] <= 2
#            count[nums[i]] += 1
#        
#        index = 0
#        for i in range(count[0]):
#            nums[index] = 0
#            index += 1
#            
#        for i in range(count[1]):
#            nums[index] = 1
#            index += 1
#        
#        for i in range(count[2]):
#            nums[index] = 2
#            index += 1
        
        #时间复杂度O(n)
        #space O(1)
        #num[0...zero] == 0
        zero = -1
        #nums[two...n - 1] ==2
        second = len(nums)
        i = 0
        while i < second: 
            if nums[i] == 0:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                assert nums[i] == 2
                second -= 1
                nums[i], nums[second] = nums[second], nums[i]
                