class Solution:
    def maxSubArray(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        res = -float("inf")
        state = 0
        for num in nums:
            state = num + (state if state > 0 else 0)
            res = max(res, state)
        return res