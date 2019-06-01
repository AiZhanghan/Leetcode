# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:59:16 2019

@author: Administrator
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                residual = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == residual:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < residual:
                        l += 1
                    else:
                        r -= 1
        return res