class Solution:
    def func(self, nums, M):
        """
        Args:
            nums: list[int]
            M: int
        
        Return:
            int
        """
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = M
        for i in range(1, len(dp)):
            if i - 1 >= 0 and dp[i - 1] >= 2:
                dp[i] = max(dp[i], dp[i - 1] - 2 + nums[i - 1])
            if i - 2 >= 0 and dp[i - 2] >= 3:
                dp[i] = max(dp[i], dp[i - 2] - 3 + nums[i - 1])
        return max(dp[1:])


if __name__ == "__main__":
    M = int(input())
    nums = list(map(int, input().split()))
    # M = 3
    # nums = [1, 3, 1, 2, 4]
    # nums = [1, 3, 2, 3, 1, 1, 1, 5, 10]
    print(Solution().func(nums, M))