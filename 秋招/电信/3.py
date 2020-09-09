class Solution:
    def func(self, nums):
        """
        动态规划
        
        Args:
            nums: list[int]
        
        Return:
            int
        """
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    print(Solution().func(nums))