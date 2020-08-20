class Solution:
    def canPartition(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            bool
        """
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2

        dp = [False for _ in range(target + 1)]
        
        dp[0] = True

        if nums[0] < target:
            dp[nums[0]] = True
        
        for i in range(1, len(nums)):
            j = target
            while nums[i] <= j:
                if dp[target]:
                    return True
                
                dp[j] = dp[j] or dp[j - nums[i]]
                j -= 1
        return dp[target]
        

class Solution:
    def canPartition(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            bool
        """
        if sum(nums) & 1 == 1:
            return False

        target = sum(nums) // 2

        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(target + 1):

                if nums[i] == j:
                    dp[i][j] = True
                    continue
                dp[i][j] = dp[i - 1][j]                    
                if nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                
            if dp[i][target]:
                return True
        
        return dp[-1][-1]