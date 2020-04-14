class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Args:
            n: int
        
        Return:
            int
        """
        dp = [1] * n
        a = 0
        b = 0
        c = 0
        for i in range(1, n):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if dp[a] * 2 == dp[i]:
                a += 1
            if dp[b] * 3 == dp[i]:
                b += 1
            if dp[c] * 5 == dp[i]:
                c += 1
        return dp[-1]


if __name__ == "__main__":
    n = 10
    print(Solution().nthUglyNumber(n))