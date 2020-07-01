class Solution:
    def missingNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid != nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
        