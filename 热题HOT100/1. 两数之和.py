from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dic:
                return [dic[complement], i]
            dic[num] = i

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         index = [x for x in range(len(nums))]
#         index.sort(key=lambda x: nums[x])
#         left = 0
#         right = len(nums) - 1
#         res = []
#         while left < right:
#             if nums[index[left]] + nums[index[right]] == target:
#                 res = [index[left], index[right]]
#                 break
#             elif nums[index[left]] + nums[index[right]] < target:
#                 left += 1
#             else:
#                 right -= 1
#         return res
