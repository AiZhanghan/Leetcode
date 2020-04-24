class Solution:
    def isStraight(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            bool
        """
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5


# class Solution:
#     def isStraight(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             bool
#         """
#         repeat = set()
#         max_, min_ = 0, 14
#         for num in nums:
#             if num == 0:
#                 continue
#             if num in repeat:
#                 return False
#             repeat.add(num)
#             max_ = max(max_, num)
#             min_ = min(min_, num)
#         return max_ - min_ < 5

