class Solution:
    def change(self, amount, coins):
        """
        Args:
            amount: int
            coins: list[int]
        
        Return:
            int
        """
        dp = [[0 for _ in range(amount + 1)] 
            for _ in range(len(coins) + 1)]
        
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == "__main__":
    amount = 5
    coins = [1,2,5]
    print(Solution().change(amount, coins))