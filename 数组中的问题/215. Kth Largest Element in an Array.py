# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:31:56 2019

@author: Administrator
"""

class Solution:
    def findKthLargest(self, nums, k) -> int:
        #quick sort partition
        #[1...i-1] > flag
        #[j...len(nums) - 1] <= flag
        i = 1
        j = len(nums)
        
        flag = nums[0]
        while i < j:
            if nums[i] > flag:
                i += 1
            else:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[0], nums[j - 1] = nums[j - 1], nums[0]
        if k - 1 == j - 1:
            return flag
        elif k - 1 < j - 1:
            return self.findKthLargest(nums[0: j - 1], k)
        else:
            return self.findKthLargest(nums[j:], k - j)
            
if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    res = Solution().findKthLargest(nums, k)
    print(res)