from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cost = float("inf")
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit