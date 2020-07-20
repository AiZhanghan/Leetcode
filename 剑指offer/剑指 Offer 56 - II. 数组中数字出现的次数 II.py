class Solution:
    def singleNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones