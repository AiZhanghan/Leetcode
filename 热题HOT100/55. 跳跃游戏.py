from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        max_dist = 0
        for i, jump in enumerate(nums):
            if i > max_dist:
                return False
            max_dist = max(max_dist, i + jump)
        return True


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) <= 1:
#             return True
#         i = 0
#         while nums[i]:
#             if i + nums[i] >= len(nums) - 1:
#                 return True
#             value = i + nums[i]
#             for j in range(i + 1, i + nums[i] + 1):
#                 if j + nums[j] >= value:
#                     next_ = j
#                     value = j + nums[j]
#             i = next_
#         return False