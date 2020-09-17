from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Args:
            nums: list[int]
            k: int
        
        Return:
            list[int]
        """
        res = []
        queue = deque()

        for r in range(len(nums)):
            