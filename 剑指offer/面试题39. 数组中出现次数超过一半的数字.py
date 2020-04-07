"""
1. 哈希表
2. 排序
3. 摩尔投票
"""


# from collections import Counter


class Solution:
    def majorityElement(self, nums):
        """
        Args:
            nums: list[int]
        return:
            bool
        """
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        return x


# class Solution:
#     def majorityElement(self, nums):
#         """
#         Args:
#             nums: list[int]
#         return:
#             bool
#         """
#         counter = Counter(nums)
#         for key, value in counter.items():
#             if value > len(nums) // 2:
#                 return key