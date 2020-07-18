class Solution:
    def nthUglyNumber(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        dp = [0 for _ in range(n)]
        dp[0] = 1
        a = 0
        b = 0
        c = 0

        for i in range(1, n):
            n2 = dp[a] * 2
            n3 = dp[b] * 3
            n5 = dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if n2 == dp[i]:
                a += 1
            if n3 == dp[i]:
                b += 1
            if n5 == dp[i]:
                c += 1
        
        return dp[-1]
        