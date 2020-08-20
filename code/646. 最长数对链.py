class Solution:
    def findLongestChain(self, pairs):
        """
        Args:
            pairs: list[list[int]]
        
        Return:
            int
        """
        pairs.sort()
        dp = [1 for _ in range(len(pairs))]
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)