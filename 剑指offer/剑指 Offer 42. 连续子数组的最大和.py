class Solution:
    def maxSubArray(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        cumulative_sum = 0
        res = -float("inf")

        for num in nums:
            cumulative_sum = max(cumulative_sum, 0) + num
            res = max(res, cumulative_sum)

        return res
        