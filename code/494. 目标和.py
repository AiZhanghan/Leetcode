# class Solution:
#     def findTargetSumWays(self, nums, S):
#         """
#         Args:
#             nums: list[int]
#             S: int
        
#         Return:
#             int
#         """
#         offset = sum(nums)
#         if abs(S) > offset:
#             return 0
        
#         dp = [[0 for _ in range(2 * offset + 1)] for _ in range(len(nums))]
#         if nums[0] == 0:
#             dp[0][offset] = 2
#         else:
#             dp[0][nums[0] + offset] = 1
#             dp[0][-nums[0] + offset] = 1

#         for i in range(1, len(nums)):
#             for j in range(len(dp[0])):
#                 l = j - nums[i] if j - nums[i] >= 0 else 0
#                 r = j + nums[i] if j + nums[i] < len(dp[0]) else 0
#                 dp[i][j] = dp[i - 1][l] + dp[i - 1][r]
#         return dp[-1][S + offset]


class Solution:
    def findTargetSumWays(self, nums, S):
        """递归

        Args:
            nums: list[int]
            S: int
        
        Return:
            int
        """
        self.d = {}
        self.nums = nums
        self.S = S
        return self.dfs(0, 0)

    def dfs(self, cur, i):
        """
        Args:
            cur: int
            i: int
        """
        if i < len(self.nums) and (cur, i) not in self.d:
            self.d[(cur, i)] = self.dfs(cur + self.nums[i], i + 1) + \
                               self.dfs(cur - self.nums[i], i + 1)
        return self.d.get((cur, i), int(cur == self.S))


if __name__ == "__main__":
    nums = [1,1,1,1,1]
    S = 3
    print(Solution().findTargetSumWays(nums, S))
