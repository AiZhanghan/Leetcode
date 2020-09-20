class Solution:
    def twoSum(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            list[int]
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp < target:
                left += 1
            elif temp > target:
                right -= 1
            else:
                return [nums[left], nums[right]]
        return []