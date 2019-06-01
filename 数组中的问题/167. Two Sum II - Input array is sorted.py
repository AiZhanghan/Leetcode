# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:37:39 2019

@author: Administrator
"""

class Solution:
    #time O(n)
    #space O(1)
    def twoSum(self, numbers, target):
        
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
                    
    #time O(nlogn)
    #space O(1)
    
#    def twoSum(self, numbers, target):
#        for i in range(len(numbers)):
#            j = self.binary_search(numbers, i + 1, len(numbers) - 1, target - numbers[i])
#            if j and i != j:
#                return [i + 1, j + 1]
#            
#    def binary_search(self, numbers, l, r, target):
#        if l > r:
#            return None
#        
##        l = 0
##        r = len(numbers)
#        mid = int(l + (r - l) / 2)
#        if numbers[mid] == target:
#            return mid
#        elif numbers[mid] > target:
#            return self.binary_search(numbers, l, mid - 1, target)
#        else:#numbers[mid] < target
#            return self.binary_search(numbers, mid + 1, r, target)
        
if __name__ == '__main__':
    numbers = [5,25,75]
    target = 100
    res = Solution().twoSum(numbers, target)
    print(res)