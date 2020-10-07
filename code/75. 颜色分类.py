from typing import List


class Solution:
    def sortColors(self, nums):
        """
        三路快排
        Do not return anything, modify nums in-place instead.
        
        Args:
            nums: list[int]
        """
        # [0, l) == 0
        # [r, len(nums) - 1) == 2
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1