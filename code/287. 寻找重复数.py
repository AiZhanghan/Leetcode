class Solution:
    def findDuplicate(self, nums):
        """
        Args:
            nums: list[int]
        
        Return: 
            int
        """
        fast = 0
        slow = 0
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        finder = 0
        while True:
            finder = nums[finder]
            slow = nums[slow]
            if finder == slow:
                break
        
        return slow


# class Solution:
#     def findDuplicate(self, nums):
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
            
#             count = 0
#             for num in nums:
#                 if num <= mid:
#                     count += 1
            
#             if count > mid:
#                 right = mid
#             else:
#                 left = mid + 1
        
#         return left