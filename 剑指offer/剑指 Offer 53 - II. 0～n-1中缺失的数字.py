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
            mid = (left + right) // 2
            if nums[mid] == mid:
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
#         for i, num in enumerate(nums):
#             if i != num:
#                 return i
#         return len(nums)