# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:21:00 2019

@author: Administrator
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #i for nums1, j for nums2
        i, j = 0, 0
        nums = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < m:
            nums.append(nums1[i])
            i += 1
        while j < n:
            nums.append(nums2[j])
            j += 1
        for i in range(len(nums)):
            nums1[i] = nums[i]