# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:54:09 2019

@author: Administrator
"""

class Solution:
    #时间复杂度O(n)
    #空间复杂度O(n)
#    def moveZeroes(self, nums) -> None:
#        """
#        Do not return anything, modify nums in-place instead.
#        """
#        non_zero_elements = []
#        
#        for i in range(len(nums)):
#            if nums[i]:
#                non_zero_elements.append(nums[i])
#        
#        for i in range(len(non_zero_elements)):
#            nums[i] = non_zero_elements[i]
#            
#        for i in range(len(non_zero_elements), len(nums)):
#            nums[i] = 0
            
    def moveZeroes(self, nums) -> None:
        #时间复杂度O(n)
        #space O(1)
        #[0...k)顺序存放k个非零元素
        k = 0
#        for i in range(len(nums)):
#            if nums[i]:
#                nums[k] = nums[i]
#                k += 1
#                
#        for i in range(k, len(nums)):
#            nums[i] = 0
        
        for i in range(len(nums)):
            if nums[i]:
                if i != k:
                    nums[i], nums[k] = nums[k], nums[i]
                    k += 1
                else:
                    k += 1
        
if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    
    Solution().moveZeroes(nums=arr)
    
    print(arr)