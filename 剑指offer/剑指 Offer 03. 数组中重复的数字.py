class Solution:
    def findRepeatNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp