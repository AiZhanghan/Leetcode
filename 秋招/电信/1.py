class Solution:
    def func(self, N):
        """动态规划
        
        Args:
            int
        
        Return:
            int
        """
        dp = [1 for _ in range(N)]
        a = 0
        b = 0
        c = 0
        i = 1

        while i < N:
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if dp[a] * 2 == dp[i]:
                a += 1
            if dp[b] * 3 == dp[i]:
                b += 1
            if dp[c] * 5 == dp[i]:
                c += 1
            i += 1
        return dp[-1]


if __name__ == "__main__":
    N = int(input())
    # N = 7
    print(Solution().func(N))