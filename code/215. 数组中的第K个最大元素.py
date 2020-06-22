import random
from typing import List, Tuple


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         self.nums = nums
#         return self.select(0, len(nums) - 1, len(nums) - k)
    
#     def select(self, left, right, k_smallest):
#         if left == right:
#             return self.nums[left]
        
#         pivot_index = random.randint(left, right)
        
#         pivot_index = self.partition(left, right, pivot_index)

#         if k_smallest == pivot_index:
#             return self.nums[pivot_index]
#         elif k_smallest < pivot_index:
#             return self.select(left, pivot_index - 1, k_smallest)
#         else:
#             return self.select(pivot_index + 1, right, k_smallest)
    
#     def partition(self, left, right, pivot_index):
#         pivot = self.nums[pivot_index]

#         self.nums[pivot_index], self.nums[right] = \
#             self.nums[right], self.nums[pivot_index]
        
#         store_index = left
#         for i in range(left, right):
#             if self.nums[i] < pivot:
#                 self.nums[store_index], self.nums[i] = \
#                     self.nums[i], self.nums[store_index]
#                 store_index += 1
        
#         self.nums[right], self.nums[store_index] = \
#             self.nums[store_index], self.nums[right]
        
#         return store_index


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        random.shuffle(nums)
        k = len(nums) - k
        left = 0
        right = len(nums) - 1
        while True:
            lo, hi = self.partition(nums, left, right)
            if lo <= k <= hi:
                return nums[k]
            elif k < lo:
                right = lo - 1
            elif k > hi:
                left = hi + 1
        
    def partition(self, nums: List[int], lo: int, hi: int) -> Tuple[int, int]:
        i = lo
        pivot = nums[random.randint(lo, hi)]
        while i <= hi:
            if nums[i] == pivot:
                i += 1
            elif nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                i += 1
                lo += 1
            elif nums[i] > pivot:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
        return lo, hi


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums, k))