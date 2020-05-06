class Solution:
    def exchange(self, nums):
        """
        :param nums: list[int]

        :return: list[int]
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2:
                left += 1
                continue
            if not (nums[right] % 2):
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        
        return nums


# class Solution:
#     def exchange(self, nums):
#         """
#         :param nums: list[int]

#         :return: list[int]
#         """
#         left = 0
#         right = len(nums) - 1
#         while True:
#             while left < right and self.is_odd(nums[left]):
#                 left += 1
#             while left < right and not self.is_odd(nums[right]):
#                 right -= 1
#             if left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#             else:
#                 break
#         return nums

#     def is_odd(self, num):
#         return num % 2 == 1
