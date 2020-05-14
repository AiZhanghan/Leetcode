from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """DP"""
        prev_max = 0
        curr_max = 0
        for num in nums:
            temp = curr_max
            curr_max = max(curr_max, prev_max + num)
            prev_max = temp
        return curr_max


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         """DP"""
#         if not nums:
#             return 0
#         if len(nums) < 2:
#             return nums[0]
#         a = nums[0]
#         b = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             a = max(b, a + nums[i])
#             a, b = b, a
#         return b

        
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         """DP"""
#         if not nums:
#             return 0
#         if len(nums) < 2:
#             return nums[0]
#         dp = [0 for _ in range(len(nums))]
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#         return dp[-1]