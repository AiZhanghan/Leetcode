class Solution:
    def findErrorNums(self, nums):
        """
        Args:
            nums: list[int]

        Return:
            list[int]
        """
        _sum = 0
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            else:
                dup = abs(nums[i])
            _sum += abs(nums[i])
        return [dup, dup - (_sum - (len(nums) * (len(nums) + 1) // 2))]
            