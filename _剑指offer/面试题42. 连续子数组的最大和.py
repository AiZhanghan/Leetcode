class Solution:
    def maxSubArray(self, nums):
        """
        Args:
            nums: list[int]
        Return:
            int
        """
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


# class Solution:
#     def maxSubArray(self, nums):
#         """
#         Args:
#             nums: list[int]
#         Return:
#             int
#         """
#         tmp = 0
#         res = -float("inf")
#         for num in nums:
#             tmp += num
#             res = max(res, tmp)
#             if tmp < 0:
#                 tmp = 0
#         return res