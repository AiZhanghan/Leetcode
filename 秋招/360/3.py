# class Solution:
#     def func(self, nums, ops):
#         """
#         Args:
#             nums: list[int]
#             ops: list[int]
        
#         Return:
#             list[int]
#         """
#         for op in ops:
#             if op == 1:
#                 nums = self.op1(nums)
#             else:
#                 nums = self.op2(nums)
#         return nums
    
#     def op1(self, nums):
#         """把排列的第1个数移到末尾

#         Args:
#             nums: list[int]

#         Return:
#             list[int]    
#         """
#         return nums[1:] + nums[:1]
    
#     def op2(self, nums):
#         """交换排列的第1个数与第2个数、第3个数与第4个数...第N-1个数与第N个数

#         Args:
#             nums: list[int]

#         Return:
#             list[int]    
#         """
#         for i in range(0, len(nums), 2):
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#         return nums