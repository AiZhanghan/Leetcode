class Solution:
    def maxProfit(self, prices):
        """
        Args:
            price: list[int]
        
        Return:
            int
        """
        profit = 0
        cost = float("inf")
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit