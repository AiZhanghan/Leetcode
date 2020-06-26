class Solution:
    def removeDuplicates(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        i = 0
        for j in range(len(nums)):
            if j < 1 or nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
                
        return i