import collections


class Solution:
    def findMaxForm(self, strs, m, n):
        """
        Args:
            strs: list[str]
            m: int
            n: int
        
        Return:
            int
        """
        dp = [[[0 for _ in range(n + 1)] 
            for _ in range(m + 1)] 
            for _ in range(len(strs) + 1)]
        
        for i in range(1, len(strs) + 1):
            zeros = strs[i - 1].count("0")
            ones = strs[i - 1].count("1")
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i - 1][j][k], 
                            dp[i - 1][j - zeros][k - ones] + 1)
        return dp[-1][-1][-1]