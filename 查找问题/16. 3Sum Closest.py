# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:05:00 2019

@author: Administrator
"""

class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            return sum(nums)
        
        min_distance = float('inf')
        nums.sort()

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            residual = target - nums[i]
            while l < r:
                if abs(target - nums[i] - nums[l] - nums[r]) < min_distance:
                    res = nums[i] + nums[l] + nums[r]
                    min_distance = abs(target - nums[i] - nums[l] - nums[r])
                if nums[l] + nums[r] == residual:
                    return nums[i] + nums[l] + nums[r]
                elif nums[l] + nums[r] < residual:
                    l += 1
                else:
                    r -= 1
            
        return res
    
if __name__ == '__main__':
    nums = [-1,0,1,1,55]
    target = 3
    print(Solution().threeSumClosest(nums, target))