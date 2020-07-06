class Solution:
    def findMin(self, nums):
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
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# class Solution:
#     def findMin(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             int
#         """
#         if not nums:
#             return
        
#         left = 0
#         right = len(nums) - 1
#         mid = left + (right - left) // 2
#         while left != mid:
#             if nums[left] < nums[right]:
#                 return nums[left]

#             if nums[left] < nums[mid]:
#                 left = mid
#             elif nums[left] > nums[mid]:
#                 right = mid
#             mid = left + (right - left) // 2

#         return min(nums[left],nums[right])


# if __name__ == "__main__":
#     nums = [4,5,6,7,0,1,2]
#     print(Solution().findMin(nums))
