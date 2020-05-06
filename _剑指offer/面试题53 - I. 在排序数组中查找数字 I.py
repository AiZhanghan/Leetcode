class Solution:
    def search(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            int
        """
        l = 0
        r = len(nums) - 1
        # 找右边界
        while l <= r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        right = l
        # 找左边界
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        left = r
        return right - left - 1

# class Solution:
#     def search(self, nums, target):
#         """
#         Args:
#             nums: list[int]
#             target: int
        
#         Return:
#             int
#         """
#         if not nums:
#             return 0
#         l = 0
#         r = len(nums) - 1
#         while l <= r:
#             mid = l + (r - l) // 2
#             if target < nums[mid]:
#                 r = mid - 1
#             elif target > nums[mid]:
#                 l = mid + 1
#             else:
#                 break
#         res = 0
#         if nums[mid] == target:
#             res += 1
#             cur = mid
#             # 向左搜索
#             while cur - 1 >= 0 and nums[cur - 1] == target:
#                     res += 1
#                     cur -= 1
#             # 向右搜素
#             cur = mid
#             while cur + 1 < len(nums) and nums[cur + 1] == target:
#                     res += 1
#                     cur += 1
#         return res
