from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 3:
            return []
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                return res
            if i > 0 and num == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] + num == 0:
                    res.append([num, nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    right -= 1
        return res


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         nums.sort()
#         for i, num in enumerate(nums):
#             left = i + 1
#             right = len(nums) - 1
#             while left < right:
#                 if nums[left] + nums[right] + num == 0:
#                     res.add((num, nums[left], nums[right]))
#                     left += 1
#                     right -= 1
#                 elif nums[left] + nums[right] + num < 0:
#                     left += 1
#                 else:
#                     right -= 1
#         return list(res)