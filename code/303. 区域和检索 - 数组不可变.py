class NumArray:

    def __init__(self, nums):
        """
        Args:
            nums: list[int]
        """
        self.dp = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.dp[i + 1] = self.dp[i] + nums[i]

    def sumRange(self, i, j):
        """
        Args:
            i: int
            j: int
        
        Return:
            int
        """
        return self.dp[j + 1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)