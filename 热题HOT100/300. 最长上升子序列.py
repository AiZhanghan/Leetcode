class Solution:
    def lengthOfLIS(self, nums):
        """DP + 二分查找
        
        Args:
            nums: list[int]
        
        Return:
            int
        """
        size = len(nums)
        if size < 2:
            return size
        
        tail = [nums[0]]
        for i in range(1, size):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
                
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = left + (right - left) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)


# class Solution:
#     def lengthOfLIS(self, nums):
#         """DP

#         Args:
#             nums: list[int]
        
#         Return:
#             int
#         """
#         if not nums:
#             return
#         dp = [1 for _ in range(len(nums))]
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)