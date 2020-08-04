class Solution:
    def findPeakElement(self, nums):
        """
        Args:
            nums: list[int]
        
        Return: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left