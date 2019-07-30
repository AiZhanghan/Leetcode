# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 08:34:14 2019

@author: 54949
"""

class Solution:
    def twoSum(self, nums, target):
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
        
#    def twoSum(self, nums, target):
#        '''
#        暴力解法
#        '''
#        n = len(nums)
#        for i in range(n):
#            for j in range(i + 1, n):
#                if nums[i] + nums[j] == target:
#                    return [i, j]
    
#    def twoSum(self, nums, target):
#        '''
#        排序 + 双指针
#        '''
#        l = 0
#        r = len(nums) - 1
#        sorted_nums = sorted(nums)
#        
#        while l < r:
#            if sorted_nums[l] + sorted_nums[r] == target:
#                break
#            elif sorted_nums[l] + sorted_nums[r] < target:
#                l += 1
#            else:
#                r -= 1
#        
#        res = []
#        for i in range(len(nums)):
#            if nums[i] == sorted_nums[l]:
#                res.append(i)
#                break
#        
#        for i in range(len(nums) - 1, -1, -1):
#            if nums[i] == sorted_nums[r]:
#                res.append(i)
#                break
#        
#        return res
#        

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    res = Solution().twoSum(nums, target)