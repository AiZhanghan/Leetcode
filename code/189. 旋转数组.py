class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        
        Args:
            nums: list[int]
            k: int
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        """
        Args:
            nums: list[int]
            start: int
            end: int
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# class Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
        
#         Args:
#             nums: list[int]
#             k: int
#         """
#         n = len(nums)
#         k = k % n
#         if k == 0:
#             return
#         count = 0
#         start = 0
#         temp = nums[start]
#         while count < n:
#             nxt = (start + k) % n
#             while nxt != start:
#                 nums[nxt], temp = temp, nums[nxt]
#                 nxt = (nxt + k) % n
#                 count += 1
#             nums[nxt] = temp
#             start += 1
#             temp = nums[start]
#             count += 1
