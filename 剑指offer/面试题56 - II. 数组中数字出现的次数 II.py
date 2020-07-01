from collections import Counter


class Solution:
    def singleNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        counter = Counter(nums)
        for key, value in counter.items():
            if value == 1:
                return key