class Solution:
    def maxProfit(self, prices):
        """
        Args:
            prices: list[int]
        
        Return:
            int
        """
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit