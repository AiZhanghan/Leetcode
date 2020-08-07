class Solution:
    def countPrimes(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        if n <= 2:
            return 0
        
        dp = [True for _ in range(n)]
        dp[0] = dp[1] = False

        i = 2
        while i * i < n:
            if dp[i]:
                for j in range(i * i, n, i):
                    dp[j] = False
            i += 1
        return sum(dp)
