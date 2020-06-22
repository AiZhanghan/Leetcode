class Solution:
    def twoSum(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            list[int]
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [nums[left], nums[right]]


# class Solution:
#     def twoSum(self, nums, target):
#         """
#         Args:
#             nums: list[int]
#             target: int
        
#         Return:
#             list[int]
#         """
#         for i, num in enumerate(nums):
#             left = i + 1
#             right = len(nums) - 1
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if nums[mid] < target - num:
#                     left = mid + 1
#                 elif nums[mid] > target - num:
#                     right = mid - 1
#                 else:
#                     break
#             if left <= right:
#                 return [num, nums[mid]]