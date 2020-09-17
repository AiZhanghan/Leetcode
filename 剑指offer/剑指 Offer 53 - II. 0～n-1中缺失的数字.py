class Solution:
    def missingNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left
              

# class Solution:
#     def missingNumber(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             int
#         """
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             mid = left + (right - left) // 2
#             if mid == nums[mid]:
#                 left = mid + 1
#             else:
#                 right = mid
#         if left == len(nums) - 1 and nums[left] == left:
#             left += 1
#         return left