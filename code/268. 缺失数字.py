class Solution:
    def missingNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        res = len(nums)
        for i, num in enumerate(nums):
            res = res ^ i ^ num
        return res
    

# class Solution:
#     def missingNumber(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             int
#         """
#         expected_sum = len(nums) * (1 + len(nums)) // 2
#         return expected_sum - sum(nums)