class Solution:
    def maxProfit(self, prices):
        """
        Args:
            prices: list[int]
        
        Return:
            int
        """
        res = 0
        cost = float("inf")
        for price in prices:
            cost = min(cost, price)
            res = max(res, price - cost)
        return res