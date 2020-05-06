from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """DP"""
        max_day, min_day = days[-1], days[0]
        dp = [0 for _ in range(max_day + 31)]
        
        d = max_day
        i = len(days) - 1
        while d >= min_day:
            if d == days[i]:
                dp[d] = min(costs[0] + dp[d + 1], 
                            costs[1] + dp[d + 7], 
                            costs[2] + dp[d + 30])
                i -= 1
            else:
                dp[d] = dp[d + 1]
            d -= 1
        return dp[min_day]