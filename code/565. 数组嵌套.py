class Solution:
    def arrayNesting(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        res = 0
        for i in range(len(nums)):
            count = 0
            j = i
            while nums[j] >= 0:
                count += 1
                temp = nums[j]
                nums[j] = -1
                j = temp
            res = max(res, count)
        return res