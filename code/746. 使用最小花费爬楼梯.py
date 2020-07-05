class Solution:
    def minCostClimbingStairs(self, cost):
        """
        Args:
            list[int]
        
        Return:
            int
        """
        pre = 0
        cur = 0
        for i in range(2, len(cost) + 1):
            pre, cur = cur, min(pre + cost[i - 2], cur + cost[i - 1])
        return cur