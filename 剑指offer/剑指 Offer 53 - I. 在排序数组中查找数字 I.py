class Solution:
    def search(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            int
        """
        return self._search(nums, target) - self._search(nums, target - 1)
    
    def _search(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# class Solution:
#     def search(self, nums, target):
#         """
#         Args:
#             nums: list[int]
#             target: int
        
#         Return:
#             int
#         """
#         left = 0
#         right = len(nums) - 1
#         # 左边界, 找第一个小于target的数的索引i
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else: # nums[mid] == target
#                 right = mid - 1
#         i = right
#         if left < len(nums) and nums[left] != target:
#             return 0
#         # 右边界, 找第一个大于target的数的索引j
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else: # nums[mid] == target
#                 left = mid + 1
#         j = left
        
#         return j - i - 1