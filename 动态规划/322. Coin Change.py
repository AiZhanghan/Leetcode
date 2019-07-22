# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:06:54 2019

@author: 54949
"""

class Solution:
    
    def coinChange(self, coins, amount):
        coins.sort()
        memo = [float('inf') for _ in range(amount + 1)]
        memo [0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    memo[i] = min(memo[i], memo[i - coins[j]])
                else:
                    break
            memo[i] += 1
        return (memo[-1] if memo[-1] < float('inf') else -1)
        
    
#    def coinChange(self, coins, amount):
#        coins.sort()
#        self.memo = [None for _ in range(amount + 1)]
#        res = self.coin_change(coins, amount)
#        if res < float('inf'):
#            return res
#        else:
#            return -1
#        
#    def coin_change(self, coins, amount):
#        
#        if amount == 0:
#            return 0
#        
#        if amount < coins[0]:
#            return float('inf')
#        
#        if self.memo[amount]:
#            return self.memo[amount]
#        
#        count = float('inf')
#        for i in range(len(coins)):
#            count = min(count, self.coin_change(coins, amount - coins[i]))
#        count += 1
#        
#        self.memo[amount] = count
#        return count
#    
if __name__ == '__main__':
    coins = [2]
    amount = 3
    res = Solution().coinChange(coins, amount)
    