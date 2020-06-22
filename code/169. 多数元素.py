import random
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """摩尔投票法"""
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
        

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         """分治"""
#         return self.majority_element(nums, 0, len(nums) - 1)
    
#     def majority_element(self, nums: List[int], lo: int, hi: int) -> int:
#         if lo == hi:
#             return nums[lo]
        
#         mid = lo + (hi - lo) // 2
#         left = self.majority_element(nums, lo, mid)
#         right = self.majority_element(nums, mid + 1, hi)

#         if left == right:
#             return left
        
#         left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
#         right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

#         return left if left_count > right_count else right


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         """随机化"""
#         majority_count = len(nums) // 2
#         while True:
#             candidate = random.choice(nums)
#             if sum(1 for num in nums if num == candidate) > majority_count:
#                 return candidate


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         """计数"""
#         dic = {}
#         max_ = 0
#         for num in nums:
#             if num in dic:
#                 dic[num] += 1
#             else:
#                 dic[num] = 1
#             if dic[num] > max_:
#                 res = num
#                 max_ = dic[num]
#         return res


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         """计数"""
#         dic = {}
#         for num in nums:
#             if num in dic:
#                 dic[num] += 1
#             else:
#                 dic[num] = 1
        
#         for key in dic:
#             if dic[key] > len(nums) // 2:
#                 return key


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         """排序"""
#         nums.sort()
#         return nums[len(nums) // 2]