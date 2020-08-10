class Solution:
    def increasingTriplet(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            bool
        """
        if len(nums) < 3:
            return False
        small = float("inf")
        mid = float("inf")
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        return False


# class Solution:
#     def increasingTriplet(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             bool
#         """
#         dp = [1 for _ in range(len(nums))]
#         for i in range(1, len(dp)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     if dp[i] >= 3:
#                         return True
#         return False