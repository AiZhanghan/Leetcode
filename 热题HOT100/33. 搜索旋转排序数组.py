from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """二分搜索"""
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         """二分搜索"""
#         if not nums:
#             return -1
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 # mid在左
#                 if nums[left] <= nums[mid]:
#                     left = mid + 1
#                 # mid在右
#                 else:
#                     if nums[right] >= target:
#                         left = mid + 1
#                     else:
#                         right = mid - 1
#             else:
#                 # mid在左
#                 if nums[left] <= nums[mid]:
#                     if nums[left] <= target:
#                         right = mid - 1
#                     else:
#                         left = mid + 1
#                 # mid在右
#                 else:
#                     right = mid - 1
#         return -1
