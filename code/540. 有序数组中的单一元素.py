class Solution:
    def singleNonDuplicate(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left += 2
            else:
                right = mid
            
        return nums[left]


# class Solution:
#     def singleNonDuplicate(self, nums):
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
#             halves_are_even = (right - mid) % 2 == 0
#             if nums[mid] == nums[mid + 1]:
#                 if halves_are_even:
#                     left = mid + 2
#                 else:
#                     right = mid - 1
#             elif nums[mid] == nums[mid - 1]:
#                 if halves_are_even:
#                     right = mid - 2
#                 else:
#                     left = mid + 1
#             else:
#                 return nums[mid]
#         return nums[left]